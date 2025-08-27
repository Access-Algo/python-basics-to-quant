import argparse

parser = argparse.ArgumentParser(description="Provides a personal greeting")
parser.add_argument("-n", metavar="--name", required = True, help="Name of the person to greet")
args= parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)