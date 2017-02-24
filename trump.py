# import random number generator
from random import randint
# imports the web browser module to display the trump memes
import webbrowser
# asks the user what they want.. meme or soundboard
from playsound import playsound
#import os to read directories
import os

# random trump memes
def openMeme():
    imageURLS = ["https://www.askideas.com/media/48/Yeah-If-The-Lazy-Mexicans-Could-Quit-Raping-Everybody-ThatD-Be-Great-Funny-Donald-Trump-Meme-Image.jpg",
                 "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQykTd_m0BcCttNbVBA5JgzGapItFEVvYP_BieoWW2hwaluvJbDdA",
                 "http://10goneviral.com/wp-content/uploads/2016/12/donald-trump-memes-from-around-the-internet-36.jpg",
                 "https://i.imgflip.com/14c231.jpg",
                 "https://s-media-cache-ak0.pinimg.com/originals/b2/f7/01/b2f701278f51ee1ef315f4a5860f9e04.jpg"]
    randomIndex = randint(0, len(imageURLS))
    randomImage = imageURLS[randomIndex]
    webbrowser.open(randomImage, new=0, autoraise=True)


# random trump sounds
def playTrump():
    sounds = os.listdir("sounds")
    randomIndex = randint(0, len(sounds))
    randomSound = sounds[randomIndex]
    playsound.playsound('sounds/' + randomSound)

action = input("What would you like to do? \n1.)Meme\n2.)Sound\n").lower()
if action == "1":
    openMeme()
if action == "2":
    playTrump()
