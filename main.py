from tkinter import *
import time
mainWindow = Tk()
rootFrame = Frame(mainWindow)
rootFrame['borderwidth'] = 5
rootFrame['relief'] = 'sunken'

TeamAWordList=["a", "b", "c"]
TeamBWordList=["d", "e", "f"]

def createWindow():
    mainWindow.title("Random Word Generator")
    mainWindow.geometry("800x600")

def createMainMenu():
    print("Generating Main Menu...")

    # Text variables:
    mainMenuTitleText = "Random Word Generator"
    mainMenuAuthorText = "Author, 2022 Author@GitHub.com"

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

    # Row 0:
    gameMenuTeamText = "Select the playing team"
    gameMenuTeamLabel = Label(rootFrame, text=gameMenuTeamText, font=('Helvetica', 24))
    gameMenuTeamLabel.pack()

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
    destroyMainWindowWidgets()
    createInGameMenu(teamName)

def createInGameMenu(teamName):
    print("Game for Team " + teamName + " started...")
    continueGame = True
    global teamScore
    teamScore = 0
    global wordCounter
    wordCounter = 0
    global passedWords
    passedWords = 0
    global maximumScore
    maximumScore = 3

    inGameMenuFrame = Frame(rootFrame)

    # Row 0:
    inGameMenuWordFrame = Frame(inGameMenuFrame)
    inGameMenuWordGuideText = "Your word is..."
    inGameMenuWordGuideLabel = Label(inGameMenuWordFrame, text=inGameMenuWordGuideText, font=('Helvetica', 14))
    inGameMenuWordToGuessText = "Sample"
    inGameMenuWordToGuessLabel = Label(inGameMenuWordFrame, text=inGameMenuWordToGuessText, font=('Helvetica', 48))

    if teamName == "A":
        inGameMenuWordToGuessLabel.configure(text="Sample A")
    elif teamName == "B":
        inGameMenuWordToGuessLabel.configure(text="Sample B")

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

    resultMenuFrame = Frame(rootFrame)

    # Row 0:
    resultMenuScoreFrame = Frame(resultMenuFrame)
    resultMenuTotalScoreText = "Total Score: " + str(teamScore) +"/"+str(maximumScore)
    resultMenuTotalScoreLabel = Label(resultMenuScoreFrame, text=resultMenuTotalScoreText, font=('Helvetica', 14))
    resultMenuPassedWordsText = "Total Passed Words: " + str(passedWords) + "/" + str(maximumScore)
    resultMenuPassedWordsLabel = Label(resultMenuScoreFrame, text=resultMenuPassedWordsText, font=('Helvetica', 14))
    # TODO: implement timer and update text
    resultMenuTimerText = "Time: mm:ss"
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

def countdownLabel(timer, updatedLabel):
    for currentTime in range(timer+1):
        updatedLabel.configure(text=str(timer-currentTime))
        rootFrame.update()
        time.sleep(1)

def countdownTimer(timer, updateLabel):
    mainWindow.update()

def checkGameOver():
    if teamScore == maximumScore or wordCounter == maximumScore:
        print("Game Over")
        # TODO: display result page
        destroyMainWindowWidgets()
        createResultMenu()
    else:
        print("Keep going")
        # TODO: update word

def updateWord(updatedLabel, wordToUpdate):
    print("Updating word")
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
    checkGameOver()

# Callback for 'Correct Button' in 'inGameMenu':
def inGameMenuCorrectButtonCallback(teamName, wordToGuessLabel):
    print("Team " + teamName + " correctly guessed the word")
    global wordCounter
    wordCounter += 1
    global teamScore
    teamScore += 1
    print("Current word count: " +str(wordCounter))
    print("Current score: " + str(teamScore))

    checkGameOver()

# Below is main...
print("Generating Window...")
createWindow() # generate window
createMainMenu() # generate the main menu
mainWindow.mainloop()