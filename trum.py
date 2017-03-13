# import random number generator
import random
# imports the web browser module to display the trump memes
import webbrowser
# import os to read directories
import os
# used for the sleep function to wait a specific time, then execute the next line
import time

# seeds the random class with a constantly changing number, the current time in seconds.
random.seed(time.ctime())

imageURLS = ["https://www.askideas.com/media/48/Yeah-If-The-Lazy-Mexicans-Could-Quit-Raping-Everybody-ThatD-Be-Great-Funny-Donald-Trump-Meme-Image.jpg",
                 "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQykTd_m0BcCttNbVBA5JgzGapItFEVvYP_BieoWW2hwaluvJbDdA",
                 "http://10goneviral.com/wp-content/uploads/2016/12/donald-trump-memes-from-around-the-internet-36.jpg",
                 "https://i.imgflip.com/14c231.jpg",
                 "https://s-media-cache-ak0.pinimg.com/originals/b2/f7/01/b2f701278f51ee1ef315f4a5860f9e04.jpg",
                 "http://www.kappit.com/img/pics/201607_0836_hiaac_sm.jpg",
                 "http://www.kappit.com/img/pics/201605_1155_gggef_sm.jpg",
                 "http://www.kappit.com/img/pics/201603_1308_affee.jpg",
                 "http://www.kappit.com/img/pics/201603_1708_gbbea.jpg",
                 "http://www.kappit.com/img/pics/201603_2319_gchch_sm.jpg",
                 "https://i.redditmedia.com/WiKzLjiI9I18FTVv81NShiCd11QeTbOOfir9D8rLA7Y.png?w=615&s=f990fff5a6bc857aa2ca10cad4cfa891"]


# random trump memes
def openMeme():
    randomIndex = random.randint(0, len(imageURLS))
    randomImage = imageURLS[randomIndex]
    webbrowser.open(randomImage, new=0, autoraise=True)


# random trump sounds
def playTrump():
    sounds = os.listdir("sounds")
    randomIndex = random.randint(0, len(sounds))
    randomSound = sounds[randomIndex]
    os.system("afplay sounds/" + str(randomSound))


# opens a random anti-trump article
def readStory():
    storyURLS = ["http://www.aljazeera.com/news/2017/02/srinivas-kuchibhotla-wife-questioned-safety-170225052932076.html",
    "http://www.bbc.com/news/world-us-canada-38785028"]
    randomIndex = random.randint(0, len(storyURLS))
    randomStory = storyURLS[randomIndex]
    webbrowser.open(randomStory, new=0, autoraise=True)


# every 2 minutes, display a "virus warning" and open a meme
def virusTrump():
    while True:
        openMeme()
        os.system("osascript -e 'tell app \"System Events\" to display dialog \"The TrumPy virus has been found "
                  "on your computer. The virus was left untreated and has taken over key parts of your Macs "
                  "file system.\"'")

        for i in range(0,10):
            os.system("afplay /System/Library/Sounds/Ping.aiff")


action = input("What would you like to do? \n1.)Meme\n2.)Sound\n3.)Read Story\n4.)Spam Trump\n").lower()

if action == "1":
    openMeme()
if action == "2":
    playTrump()
if action == "3":
    readStory()
if action == "4":
    virusTrump()
