import pyjokes  # pyright: ignore[reportMissingImports]
import pyttsx3  # type: ignore
import os

engine = pyttsx3.init()

joke = pyjokes.get_joke()


# this like for jokes

# this is prakash akash

"""
asjdjashdasnd
askjdkjasdn
assjdnlajd
"""


print("joke=======>", joke)

dir = os.getcwd()

print("dir:::===>", dir)

print("kandl", os.listdir("/"))


contents = os.listdir(dir)

# Print the list of names
print(contents)


engine.say("hi, mera name prakash hai , aur tumahra name kya hai")

engine.runAndWait()
