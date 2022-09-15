from tkinter import *
import time, random

mainWindow = Tk()
rootFrame = Frame(mainWindow)
rootFrame['borderwidth'] = 5
rootFrame['relief'] = 'sunken'

filenameA = "testWordList1.txt"
filenameB = "testWordList2.txt"
TeamAWordList = open(filenameA).read().splitlines()
TeamBWordList = open(filenameB).read().splitlines()

def createWindow():
    mainWindow.title("Random Word Generator")
    mainWindow.geometry("800x600")

def createMainMenu():
    print("Generating Main Menu...")

    # Text variables:
    mainMenuTitleText = "Random Word Generator"
    mainMenuAuthorText = "Gateau, 2022 GateauDaze@GitHub.com"

    # Row 0:
    mainMenuTitleButtonFrame = Frame(rootFrame)
    mainMenuTitleLabel = Label(mainMenuTitleButtonFrame, text=mainMenuTitleText, font=('Helvetica', 24))
    mainMenuNextButton = Button(mainMenuTitleButtonFrame, text="Start", font=('Helvetica', 14), command=mainMenuStartButtonCallback)
    # display Title and Button underneath...
    mainMenuTitleLabel.pack()
    mainMenuNextButton.pack()
    mainMenuTitleButtonFrame.pack()

    # Row 1:
    # Author information...
    mainMenuAuthorLabel = Label(rootFrame, text=mainMenuAuthorText)
    mainMenuAuthorLabel.pack()

    # Pack widgets
    rootFrame.pack(ipadx=5, ipady=5, anchor=CENTER, expand=True)


def createGameMenu():
    print("Creating a game window...")
    global maximumScore
    maximumScore = IntVar()

    # Row 0:
    gameMenuTeamWordCountFrame = Frame(rootFrame)
    gameMenuTeamText = "Select the playing team"
    gameMenuTeamLabel = Label(gameMenuTeamWordCountFrame, text=gameMenuTeamText, font=('Helvetica', 24))
    gameMenuTeamLabel.grid(column=0, row=0)
    gameMenuWordCountScaleFrame = Frame(gameMenuTeamWordCountFrame)
    gameMenuWordCountLabel = Label(gameMenuWordCountScaleFrame, text="Word count: ", font=('Helvetica', 14))
    gameMenuWordCountScale = Scale(gameMenuWordCountScaleFrame, from_=1, to=100, variable = maximumScore, orient=HORIZONTAL, length=200)
    gameMenuWordCountLabel.grid(column=0, row=0)
    gameMenuWordCountScale.grid(column=1, row=0)
    gameMenuWordCountScaleFrame.grid(column=0, row=1)
    gameMenuTeamWordCountFrame.pack()

    # Row 1:
    gameMenuTeamButtonFrame = Frame(rootFrame)
    gameMenuTeamAButton = Button(gameMenuTeamButtonFrame, text="Team A", font=('Helvetica', 14), command=gameMenuTeamAButtonCallback)
    gameMenuTeamBButton = Button(gameMenuTeamButtonFrame, text="Team B", font=('Helvetica', 14), command=gameMenuTeamBButtonCallback)
    gameMenuMainMenuButton = Button(gameMenuTeamButtonFrame, text="Main Menu", font=('Helvetica', 14), command=gameMenuMainMenuButtonCallback)
    gameMenuTeamAButton.grid(column=0, row=0)
    gameMenuMainMenuButton.grid(column=1, row=0)
    gameMenuTeamBButton.grid(column=2, row=0)
    gameMenuTeamButtonFrame.pack()

    # Pack widgets
    rootFrame.pack(ipadx=5, ipady=5, anchor=CENTER, expand=True)

def createTeamMenu(teamName):
    print("Creating Team " + teamName  +" Menu...")
    print("Word Count: " + str(maximumScore.get()))
    # Row 0:
    teamAGameStartIn = 3
    teamAMenuAlertCountdownFrame = Frame(rootFrame)
    teamAMenuAlertText = "Team " +teamName +" Game Starts in..."
    teamAMenuAlertLabel = Label(teamAMenuAlertCountdownFrame, text=teamAMenuAlertText, font=('Helvetica', 14))
    teamAMenuCountdownLabel = Label(teamAMenuAlertCountdownFrame, text=str(teamAGameStartIn), font=('Helvetica', 48))
    teamAMenuAlertLabel.grid(column=0, row=0)
    teamAMenuCountdownLabel.grid(column=0, row=1)
    teamAMenuAlertCountdownFrame.pack()

    # Pack widgets
    rootFrame.pack(ipadx=5, ipady=5, anchor=CENTER, expand=True)

    # countdown before game starts...
    countdownLabel(teamAGameStartIn, teamAMenuCountdownLabel)
    rootFrame.after(teamAGameStartIn*1000, destroyMainWindowWidgets)
    rootFrame.after(teamAGameStartIn*1000, lambda:createInGameMenu(teamName))

def createInGameMenu(teamName):
    print("Game for Team " + teamName + " started...")
    global startTime
    startTime = time.time()
    
    global currentWordList
    if teamName == "A":
        currentWordList = TeamAWordList
    elif teamName == "B":
        currentWordList = TeamBWordList

    global teamScore
    teamScore = 0
    
    global wordCounter
    wordCounter = 0
    
    global passedWords
    passedWords = 0

    global maximumScore

    if len(currentWordList) < maximumScore.get():
        maximumScore.set(len(currentWordList)) 

    # Shuffle word list
    random.shuffle(currentWordList)

    inGameMenuFrame = Frame(rootFrame)

    # Row 0:
    inGameMenuWordFrame = Frame(inGameMenuFrame)
    inGameMenuWordGuideText = "Your word is..."
    inGameMenuWordGuideLabel = Label(inGameMenuWordFrame, text=inGameMenuWordGuideText, font=('Helvetica', 14))
    inGameMenuWordToGuessText = "Sample"
    inGameMenuWordToGuessLabel = Label(inGameMenuWordFrame, text=inGameMenuWordToGuessText, font=('Helvetica', 48))

    inGameMenuWordToGuessLabel.configure(text=currentWordList[wordCounter])

    inGameMenuWordGuideLabel.grid(column=0, row=0)
    inGameMenuWordToGuessLabel.grid(column=0, row=1)
    inGameMenuWordFrame.grid(column=0, row=0)

    # Row 1:
    inGameMenuButtonFrame = Frame(inGameMenuFrame)
    inGameMenuPassButton = Button(inGameMenuButtonFrame, text="Pass!", font=('Helvetica', 14), command=lambda:inGameMenuPassButtonCallback(teamName, inGameMenuWordToGuessLabel))
    inGameMenuCorrectButton = Button(inGameMenuButtonFrame, text="Correct!", font=('Helvetica', 14), command=lambda:inGameMenuCorrectButtonCallback(teamName, inGameMenuWordToGuessLabel))

    inGameMenuPassButton.grid(column=0, row=0)
    inGameMenuCorrectButton.grid(column=1, row=0)
    inGameMenuButtonFrame.grid(column=0, row=1)
    inGameMenuFrame.pack()

    # Pack widgets
    rootFrame.pack(ipadx=5, ipady=5, anchor=CENTER, expand=True)

def createResultMenu():
    print("Creating results page...")
    endTime = time.time()
    resultMenuFrame = Frame(rootFrame)

    # Row 0:
    resultMenuScoreFrame = Frame(resultMenuFrame)
    resultMenuTotalScoreText = "Total Score: " + str(teamScore) +"/"+str(wordCounter)
    resultMenuTotalScoreLabel = Label(resultMenuScoreFrame, text=resultMenuTotalScoreText, font=('Helvetica', 14))
    resultMenuPassedWordsText = "Total Passed Words: " + str(passedWords) + "/" + str(wordCounter)
    resultMenuPassedWordsLabel = Label(resultMenuScoreFrame, text=resultMenuPassedWordsText, font=('Helvetica', 14))
    # TODO: implement timer and update text
    elapsedTime = endTime - startTime
    minutes = (int)(elapsedTime // 60)
    seconds = (int)(elapsedTime % 60)
    resultMenuTimerText = "Time: "+"{:02d}".format(minutes)+":"+"{:02d}".format(seconds)
    resultMenuTimerLabel = Label(resultMenuScoreFrame, text=resultMenuTimerText, font=('Helvetica', 14))
    resultMenuTotalScoreLabel.grid(column=0, row=0)
    resultMenuPassedWordsLabel.grid(column=0, row=1)
    resultMenuTimerLabel.grid(column=0, row=2)
    resultMenuScoreFrame.grid(column=0, row=0)
    # Row 1:
    # Return to Main Menu
    resultMenuToMainMenuFrame = Frame(resultMenuFrame)
    resultMenuToMainMenuButton = Button(resultMenuToMainMenuFrame, text="To Main Menu", font=('Helvetica', 14), command=gameMenuMainMenuButtonCallback)
    resultMenuToMainMenuButton.pack()
    resultMenuToMainMenuFrame.grid(column=0, row=1)
    resultMenuFrame.pack()

    # Pack widgets
    rootFrame.pack(ipadx=5, ipady=5, anchor=CENTER, expand=True)
    

# Functions for window control
def destroyMainWindowWidgets():
    print("Destroying all widgets in screen...")
    widgetList = rootFrame.pack_slaves()
    for widgets in widgetList:
        widgets.pack_forget()

def countdownLabel(remainingTime, updateLabel):
    updateLabel.configure(text=str(remainingTime))
    rootFrame.update()
    if remainingTime != 0:
        print("Countdown Remaining Time: " + str(remainingTime))
        remainingTime -=1
        rootFrame.after(1000, lambda:countdownLabel(remainingTime, updateLabel))
    else:
        print("Countdown complete")

def countdownTimer(timer, updateLabel):
    mainWindow.update()

def checkGameOver():
    if teamScore == maximumScore.get() or wordCounter == len(currentWordList):
        print("Game Over")
        return True
    else:
        print("Keep going")
        return False

def updateWord(updatedLabel, wordToUpdate):
    print("Updating word to: " + wordToUpdate)
    updatedLabel.configure(text=wordToUpdate)
    rootFrame.update()

# Callback for Main Menu:
def mainMenuStartButtonCallback():
    print("Main menu start button pressed...")
    destroyMainWindowWidgets()
    createGameMenu()

# Callback for Team A Button in Game Menu:
def gameMenuTeamAButtonCallback():
    print("Team A Button pressed...")
    destroyMainWindowWidgets()
    createTeamMenu("A")

# Callback for Team B Button in Game Menu:
def gameMenuTeamBButtonCallback():
    print("Team B Button pressed...")
    destroyMainWindowWidgets()
    createTeamMenu("B")

# Callback for 'To Main Menu' Button in Game Menu: 
def gameMenuMainMenuButtonCallback():
    print("Going back to main menu...")
    destroyMainWindowWidgets()
    createMainMenu()

# Callback for 'Pass Button' in 'inGameMenu':
def inGameMenuPassButtonCallback(teamName, wordToGuessLabel):
    print("Team " + teamName + " passed a word")
    global passedWords
    passedWords += 1
    global wordCounter
    wordCounter += 1
    print("Current word count: " + str(wordCounter))
    gameOverState = checkGameOver()
    if gameOverState == True:
        destroyMainWindowWidgets()
        createResultMenu()
    elif gameOverState == False:
        if teamName == "A":
            updateWord(wordToGuessLabel, TeamAWordList[wordCounter])
        elif teamName == "B":
            updateWord(wordToGuessLabel, TeamBWordList[wordCounter])

# Callback for 'Correct Button' in 'inGameMenu':
def inGameMenuCorrectButtonCallback(teamName, wordToGuessLabel):
    print("Team " + teamName + " correctly guessed the word")
    global wordCounter
    wordCounter += 1
    global teamScore
    teamScore += 1
    print("Current word count: " +str(wordCounter))
    print("Current score: " + str(teamScore))
    gameOverState = checkGameOver()
    if gameOverState == True:
        destroyMainWindowWidgets()
        createResultMenu()
    elif gameOverState == False:
        if teamName == "A":
            updateWord(wordToGuessLabel, TeamAWordList[wordCounter])
        elif teamName == "B":
            updateWord(wordToGuessLabel, TeamBWordList[wordCounter])

# Below is main...
print("Generating Window...")
createWindow() # generate window
createMainMenu() # generate the main menu
mainWindow.mainloop()