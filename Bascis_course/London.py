from random import choice 

capital = "London"
Bird = "sparrow"
flower = "rose"
song = "classical"

def randomfacts():
    funfact = ["London smells like freshly baked bread.",
               "The sparrow is a small, plump bird.",
               "Roses are red, violets are blue.",
               "Classical music is soothing and calming."]
    return choice(funfact)
print(randomfacts())