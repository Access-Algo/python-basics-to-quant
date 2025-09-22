"""
Rebalancing Flow Study (SPY vs TLT) — Corvin's Strategy #4
----------------------------------------------------------
Plain-English idea:
- Big 60/40 (stocks/bonds) portfolios rebalance near month-end.
- If SPY outperforms TLT during the month (MTD), funds will likely SELL SPY and BUY TLT to get back to 60/40.
- We try to "front-run" that flow by going LONG the loser and SHORT the winner from the penultimate trading day close (T-1) to month-end close (T).

What this script does:
1) Download daily SPY & TLT prices with yfinance.
2) For each month, compute the MTD relative performance up to T-1: RelPerf = MTD(SPY) - MTD(TLT).
3) If RelPerf > 0: SPY outperformed → we SHORT SPY and LONG TLT (expecting rebalancing sells SPY / buys TLT).
   If RelPerf < 0: TLT outperformed → we SHORT TLT and LONG SPY.
4) Enter at T-1 close, exit at T close. Optionally apply simple vol targeting to scale trade size.
5) Report stats and plot equity vs SPY benchmark over the last 10 years.

Notes:
- This is a minimal, transparent backtest for learning. No commissions/slippage modeled.
- Extend windows (e.g., hold last 2-3 days), test different lookbacks (MTD vs last 10 trading days), etc.
"""

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import yfinance as yf
from scipy import stats
import matplotlib.pyplot as plt

# ============================
# USER PARAMETERS (tweak here)
# ============================
TICKERS         = ["SPY", "TLT"]       # Stock & Long-bond proxies
DATA_START      = "2005-01-01"         # Start date for history
VOL_TARGET_ON   = True                 # Toggle naive vol targeting
TARGET_DAILY_VOL= 0.01                 # Target daily vol per leg (1%)
VOL_LOOKBACK    = 60                   # Lookback days for vol estimation
LAST_N_YEARS    = 10                   # Plot/compare last N years
PRINT_TAIL      = 10                   # How many recent trades to display

# ============================
# 1) DOWNLOAD DATA
# ============================
# We use adjusted close to account for dividends/splits automatically.
px = yf.download(TICKERS, start=DATA_START, interval="1d", auto_adjust=True, progress=False)["Close"].dropna()

# Basic daily returns
rets = px.pct_change().dropna()

# ============================
# 2) FIND MONTH-ENDS & T-1 DAYS
# ============================
# Define month-end trading days (EoM) by taking the last index in each (year, month) group.
cal = px.index
eom = cal.to_series().groupby([cal.year, cal.month]).idxmax().values
eom = pd.to_datetime(eom)

# Make a mask to mark EoM days
eom_mask = pd.Series(False, index=cal)
eom_mask.loc[eom] = True

# Penultimate trading day (T-1) is simply the prior trading day before each EoM
tminus1 = cal.to_series().shift(1).where(eom_mask).dropna()
tminus1 = pd.DatetimeIndex(tminus1.values)

# Keep only those T-1 dates that exist in px (defensive)
signal_dates = tminus1.intersection(px.index)

# ============================
# 3) COMPUTE MTD RELATIVE PERF AT T-1
# ============================
def mtd_relperf(date):
    """
    Compute month-to-date relative outperformance up to the T-1 day.
    RelPerf = MTD(SPY) - MTD(TLT)
    MTD return = (Price_{T-1} / Price_{month_start}) - 1
    """
    month_start = pd.Timestamp(year=date.year, month=date.month, day=1)
    seg = px.loc[month_start:date]
    if seg.empty:
        return np.nan
    spyr = seg["SPY"].iloc[-1] / seg["SPY"].iloc[0] - 1.0
    tltr = seg["TLT"].iloc[-1] / seg["TLT"].iloc[0] - 1.0
    return spyr - tltr

rel = pd.Series({d: mtd_relperf(d) for d in signal_dates}).dropna()

# ============================
# 4) BUILD TRADES: T-1 CLOSE -> T CLOSE
# ============================
trades = []
for d in rel.index:
    # Entry at T-1 close
    if d not in px.index:
        continue
    # Exit is next trading day (should be EoM)
    try:
        e_idx = cal.get_loc(d)
        x = cal[e_idx + 1]
    except Exception:
        continue

    # Make sure exit is the same month (safety)
    if d.month != x.month:
        continue

    # Sign of relative performance:
    # +1 => SPY outperformed TLT => expect rebalancing to SELL SPY / BUY TLT.
    # We FRONT-RUN by SHORTING SPY and LONGING TLT over the rebalance window.
    s = np.sign(rel.loc[d])
    long_leg  = "TLT" if s > 0 else "SPY"
    short_leg = "SPY" if s > 0 else "TLT"

    # Long-leg return: from entry (T-1 close) to exit (T close)
    lr = px[long_leg].loc[x] / px[long_leg].loc[d] - 1.0
    # Short-leg return: (entry at T-1 close, cover at T close)
    sr = px[short_leg].loc[d] / px[short_leg].loc[x] - 1.0

    pair_ret = lr + sr  # equal notional long/short

    # Optional naive vol targeting per leg: scale notional so each leg targets TARGET_DAILY_VOL
    if VOL_TARGET_ON:
        vol_l = rets[long_leg].loc[:d].tail(VOL_LOOKBACK).std()
        vol_s = rets[short_leg].loc[:d].tail(VOL_LOOKBACK).std()
        # Avoid division by zero; if vol missing, skip scaling
        if pd.notna(vol_l) and vol_l > 0 and pd.notna(vol_s) and vol_s > 0:
            scale_l = TARGET_DAILY_VOL / vol_l
            scale_s = TARGET_DAILY_VOL / vol_s
            pair_ret *= 0.5 * (scale_l + scale_s)  # average of the two scaled legs

    trades.append({
        "entry": d,
        "exit": x,
        "rel_mtd": rel.loc[d],
        "long_leg": long_leg,
        "short_leg": short_leg,
        "ret": pair_ret
    })

df = pd.DataFrame(trades).set_index("exit").sort_index()

if df.empty:
    raise SystemExit("No trades generated. Check data availability or logic.")

# ============================
# 5) ACCOUNT BALANCE SIMULATION ($100k start, 2% per trade)
# ============================

initial_balance = 100_000   # Starting capital in $
risk_fraction   = 0.10     # Risk 2% of account per trade

balances = [initial_balance]
for r in df["ret"]:
    equity_now = balances[-1]
    # Only 10% of current equity is put at risk for this trade
    risk_cap   = equity_now * risk_fraction
    pnl        = risk_cap * r     # $ P&L for this trade
    balances.append(equity_now + pnl)

# Account curve in DOLLARS (no normalization)
acct_curve = pd.Series(balances[1:], index=df.index)

# If you still want a normalized curve for stats, keep both:
equity = acct_curve / initial_balance  # normalized (growth of $1)


# Limit to the last N years for plotting/reporting, but keep full stats as needed
cutoff_date = equity.index.max() - pd.DateOffset(years=LAST_N_YEARS)
equity_10y = equity[equity.index >= cutoff_date]

# Annualization helper using trading days (~252/yr) across whole sample
def annualize(ret_series):
    if ret_series.empty:
        return np.nan
    total = ret_series.iloc[-1]
    years = len(ret_series) / 252.0
    return total**(1/years) - 1 if years > 0 else np.nan

# Full-period stats
cagr_full = annualize(equity)
maxdd_full = (equity / equity.cummax() - 1.0).min()
hit_full = (df["ret"] > 0).mean()
tstat_full = stats.ttest_1samp(df["ret"], 0, nan_policy="omit").statistic

# Build a simple benchmark: buy-and-hold SPY, reindexed to the same trade timestamps
# For fairness, we compound SPY only on the same exit dates as our strategy (discrete sampling).
spy_on_exits = px["SPY"].reindex(df.index)
spy_ret_step = spy_on_exits.pct_change().fillna(0)  # step returns between trade exits
spy_equity = (1 + spy_ret_step).cumprod()
spy_equity_10y = spy_equity[spy_equity.index >= cutoff_date]

# ============================
# 6) OUTPUT SUMMARY
# ============================
print("=== Rebalance Strategy: SPY/TLT (T-1 close -> Month-End close) ===")
print(f"Trades: {len(df)}")
print(f"Hit Rate: {hit_full:.1%}")
print(f"CAGR (full sample): {cagr_full:.2%}")
print(f"Max Drawdown (full sample): {maxdd_full:.2%}")
print(f"t-stat of returns: {tstat_full:.2f}")
print("\nRecent trades:")
print(df[["entry","rel_mtd","long_leg","short_leg","ret"]].tail(PRINT_TAIL))

# ============================
# 7) PLOT (account dollars over last N years)
# ============================
cutoff_date = acct_curve.index.max() - pd.DateOffset(years=LAST_N_YEARS)
acct_last = acct_curve[acct_curve.index >= cutoff_date]
if acct_last.empty:
    acct_last = acct_curve.copy()

plt.figure(figsize=(10, 5))
plt.plot(acct_last.index, acct_last.values, label="Rebalance Strategy (Account $)")
plt.title(f"Account Balance — Last {LAST_N_YEARS} Years (Start ${initial_balance:,}, 10% risk/trade)")
plt.xlabel("Date")
plt.ylabel("Account Balance ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Trades:", len(df))
print("Nonzero returns:", (df["ret"].abs() > 1e-12).sum())
print("First 3 trades:\n", df[["entry","rel_mtd","long_leg","short_leg","ret"]].head(3))
print("First acct values:", acct_curve.head(3).to_string())

