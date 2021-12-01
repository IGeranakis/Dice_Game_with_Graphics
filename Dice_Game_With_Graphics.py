from tkinter import *
from random import randint
from PIL import ImageTk,Image
root = Tk()
root.title("Dice Game")
root.iconbitmap(r'dice_kNq_icon.ico')
root.geometry('300x300')
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
def AnnounceTheWinner(frame,player1):
    frame.grid_forget()
    WinnerFrame = Frame(root, bg = "Black")
    if(player1 == 4):
        WinnerLabel = Label(WinnerFrame, text = "CPU is the Winner", bg = "Dark Green", padx = 50, pady = 25)
        WinnerLabel.pack()
    else:
        WinnerLabel = Label(WinnerFrame, text = "User is the Winner", bg = "Dark Green", padx = 50, pady = 25)
        WinnerLabel.pack()
    gobackbtn = Button(WinnerFrame, text = "Return to main menu", command = lambda: Goback(WinnerFrame))
    gobackbtn.pack()
    WinnerFrame.grid(row = 0 , column = 0, sticky = "nsew")
def Other_Rounds(frame,player1,player2):
    frame.grid_forget()
    newRound = Frame(root, bg = "black")
    CPULabel = Label(newRound, text = "CPU GAME")
    CPULabel.pack()
    UserScoreLabel = Label(newRound, text = "User Score : " + str(player2))
    UserScoreLabel.pack()
    CPUScoreLabel = Label(newRound, text = "CPU Score : " + str(player1))
    CPUScoreLabel.pack()
    Gobackbtn = Button(newRound, text = "Back", command = lambda: Goback(newRound))
    Gobackbtn.pack()
    CPUbtn = Button(newRound, text = "Continue", command = lambda: CPUChoice(newRound,CPUbtn,player1,player2))
    CPUbtn.pack() 
    newRound.grid(row = 0 , column = 0 , sticky = "nsew")
def Winner(frame,Dice1, Dice2,player2,player1):
    if(Dice1 > Dice2):
        player1 = player1 + 1
        newLabel = Label(frame, text = "CPU Wins")
    elif(Dice1 < Dice2):
        player2 = player2 + 1
        newLabel = Label(frame, text = "User Wins")
    else:
        newLabel = Label(frame, text = "Draw")
    newLabel.pack()
    if(player1 != 4 and player2 != 4):
        newbtn = Button(frame, text = "Continue", command = lambda: Other_Rounds(frame,player1,player2))
        newbtn.pack()
    else:
        btn = Button(frame, text = "Continue", command = lambda: AnnounceTheWinner(frame,player1))
        btn.pack()
def UserRound(newbtn,frame,user,cpu,NewLabel,CpuDice):
    Dice = randint(1,6)
    NewLabel.pack_forget()
    newbtn.pack_forget()
    label = Show_Dice(frame,Dice)
    label.pack()
    Winner(frame,CpuDice,Dice,cpu,user)
def Show_Dice(frame,dice):
    if(dice == 1):
        Myimage = PhotoImage(file = 'Dice1.png')
        Mylabel = Label(frame, image = Myimage)
        Mylabel.photo = Myimage
    elif(dice == 2):
        Myimage = PhotoImage(file = 'Dice2.png')
        Mylabel = Label(frame, image = Myimage)
        Mylabel.photo = Myimage
    elif(dice == 3):
        Myimage = PhotoImage(file = 'Dice3.png')
        Mylabel = Label(frame, image = Myimage)
        Mylabel.photo = Myimage
    elif(dice == 4):
        Myimage = PhotoImage(file = 'Dice4.png')
        Mylabel = Label(frame, image = Myimage)
        Mylabel.photo = Myimage
    elif(dice == 5):
        Myimage = PhotoImage(file = 'Dice5.png')
        Mylabel = Label(frame, image = Myimage)
        Mylabel.photo = Myimage
    elif(dice == 6):
        Myimage = PhotoImage(file = 'Dice6.png')
        Mylabel = Label(frame, image = Myimage)
        Mylabel.photo = Myimage
    Mylabel.pack()
    return Mylabel
def CPURound(btn,frame,user,cpu, label):
    Dice = randint(1,6)
    label.pack_forget()
    NewLabel = Show_Dice(frame,Dice)
    CPUDice = Dice
    btn.pack_forget()
    LabelUser = Label(frame, text = "User Turn click Next to find out your dice Number")
    LabelUser.pack()
    newbtn = Button (frame, text = "Next", command = lambda : UserRound(newbtn,frame,user,cpu,NewLabel,CPUDice))
    newbtn.pack()

def CPUChoice(frame1,btn,user,cpu):
    CPUTurnLabel = Label(frame1, text = "CPU's turn click continue to find out the dice Number of CPU")
    CPUTurnLabel.pack()
    btn.pack_forget()
    continuebtn = Button(frame1, text = "continue", command = lambda: CPURound(continuebtn,frame1,user,cpu,CPUTurnLabel))
    continuebtn.pack()
def Goback(frame):
    frame.grid_forget()
    MainScene.grid(row = 0 , column = 0 , sticky = "nsew")
def Instructions(event):
    MainScene.grid_forget()
    #============= Creating Instruction Scene =================================

    InstructionScene = Frame(root, bg = "black")
    #======== Creating Labels ==============================================

    InstructionLabel1 = Label(InstructionScene, text = "Welcome to the Dice game")
    InstructionLabel1.pack()
    InstructionLabel2 = Label(InstructionScene, text = "In this game there are 2 players")
    InstructionLabel2.pack()
    InstructionLabel3 = Label(InstructionScene, text = "The Players roll their Dices and whoever has bigger number than the other wins the round")
    InstructionLabel3.pack()
    InstructionLabel4 = Label(InstructionScene, text = "It is a best of 7 game")
    InstructionLabel4.pack()
    InstructionLabel5 = Label(InstructionScene, text = "Good Luck")
    InstructionLabel5.pack()
    #======== Creating Button==========================================================
      
    Instructionbtn = Button(InstructionScene, text = "Go back", command = lambda: Goback(InstructionScene))
    Instructionbtn.pack(side = BOTTOM)
    InstructionScene.grid(row = 0, column = 0, sticky = "nsew")

def CPU_Choice(event):
    MainScene.grid_forget()
    CPUGameScene = Frame(root, bg = "black")
    CPULabel = Label(CPUGameScene, text = "CPU GAME")
    CPULabel.pack()
    UserScore = 0
    CPUScore = 0
    UserScoreLabel = Label(CPUGameScene, text = "User Score : " + str(UserScore))
    UserScoreLabel.pack()
    CPUScoreLabel = Label(CPUGameScene, text = "CPU Score : " + str(CPUScore))
    CPUScoreLabel.pack()
    Gobackbtn = Button(CPUGameScene, text = "Back", command = lambda: Goback(CPUGameScene))
    Gobackbtn.pack()
    CPUbtn = Button(CPUGameScene, text = "Continue", command = lambda: CPUChoice(CPUGameScene,CPUbtn,UserScore,CPUScore))
    CPUbtn.pack() 
    CPUGameScene.grid(row = 0 , column = 0 , sticky = "nsew")
def AnnounceThePlayerWinner(Scene,Player1,Player2,Player1Score):
    Scene.grid_forget()
    WinnerScene = Frame(root, bg = "black")
    if(Player1Score == 4):
        WinnerLabel = Label(WinnerScene, text = "" + str(Player1) + " is the Winnner")
        WinnerLabel.pack()
    else:
        WinnerLabel = Label(WinnerScene, text = "" + str(Player2) + " is the Wineer") 
        WinnerLabel.pack()
    gobackbtn = Button(WinnerScene, text = "Return to Main Menu", command = lambda: Goback(WinnerScene))
    gobackbtn.pack()
    WinnerScene.grid(row = 0 , column = 0 , sticky = "nsew")
def OtherRoundsPlayers(Scene,Player1,Player2,Player1Score,Player2Score):
    Scene.grid_forget()
    OtherRoundsScene = Frame(root, bg = "black")
    PlayersLabel = Label(OtherRoundsScene, text = "2 Players Game")
    PlayersLabel.pack()
    Player1ScoreLabel = Label(OtherRoundsScene, text = "" + str(Player1) + " Score : " + str(Player1Score))
    Player1ScoreLabel.pack()
    Player2ScoreLabel = Label(OtherRoundsScene, text = "" + str(Player2) + " Score : " +str(Player2Score))
    Player2ScoreLabel.pack()
    Gobackbtn = Button(OtherRoundsScene, text = "Back", command = lambda: Goback(OtherRoundsScene))
    Gobackbtn.pack()
    Continuebtn = Button(OtherRoundsScene, text = "Continue", command = lambda: PlayersRound(OtherRoundsScene,Player1,Player2,Player1Score,Player2Score))
    Continuebtn.pack()
    OtherRoundsScene.grid(row = 0 , column = 0 , sticky = "nsew")
def PlayersWinner(Scene,Player1Dice,Dice,Player1,Player2,Player1Score,Player2Score):
    if(Player1Dice > Dice):
        Player1Score = Player1Score + 1
        newlabel = Label(Scene, text = "" + str(Player1) + " Wins")
    elif(Player1Dice < Dice):
        Player2Score = Player2Score + 1
        newlabel = Label(Scene, text = "" + str(Player2) + " Wins" )
    else:
        newlabel = Label(Scene, text = "Draw")
    newlabel.pack()
    if(Player1Score !=4 and Player2Score != 4):
        newbtn = Button(Scene, text = "Continue", command = lambda: OtherRoundsPlayers(Scene,Player1,Player2,Player1Score,Player2Score))
        newbtn.pack()
    else:
        btn = Button(Scene, text = "Continue", command = lambda: AnnounceThePlayerWinner(Scene,Player1,Player2,Player1Score))
        btn.pack()
def Player2Round(Scene,newbtn,Player1Dice,Player1,Player2,Player1Score,Player2Score,Player2Label,Show_Label):
    Show_Label.pack_forget()
    Dice = randint(1,6)
    newbtn.pack_forget()
    Player2Label.pack_forget()
    label = Show_Dice(Scene,Dice)
    label.pack()
    PlayersWinner(Scene,Player1Dice,Dice,Player1,Player2,Player1Score,Player2Score)
def Player1Round(btn,Scene,Player1,Player2,Player1Score,Player2Score,label):
    Dice = randint(1,6)
    label.pack_forget()
    Show_Label = Show_Dice(Scene,Dice)
    Player1Dice = Dice
    btn.pack_forget()
    Player2Label = Label(Scene, text = "" + str(Player2) + " Turn click continue to find out the Dice Number of " + str(Player2))
    Player2Label.pack()
    newbtn = Button(Scene, text = "Continue", command = lambda: Player2Round(Scene,newbtn,Player1Dice,Player1,Player2,Player1Score,Player2Score,Player2Label,Show_Label))
    newbtn.pack()
def PlayersRound(frame,Player1, Player2,Player1Score,Player2Score):
    frame.grid_forget()
    PlayersRoundScene = Frame(root, bg = "black")
    Player1ScoreLabel = Label(PlayersRoundScene, text = "" + str(Player1) + " Score : " + str(Player1Score))
    Player1ScoreLabel.pack()
    Player2ScoreLabel = Label(PlayersRoundScene, text = "" + str(Player2) + " Score : " + str(Player2Score))
    Player2ScoreLabel.pack()
    PlayersGameLabel = Label(PlayersRoundScene, text = "2 Players Game")
    PlayersGameLabel.pack()
    Player1TurnLabel = Label(PlayersRoundScene, text = " " + str(Player1) + " Turn click continue to find out the Dice Number of " + str(Player1))
    Player1TurnLabel.pack()
    Continuebtn = Button(PlayersRoundScene, text = "Continue", command = lambda: Player1Round(Continuebtn,PlayersRoundScene,Player1,Player2,Player1Score,Player2Score,Player1TurnLabel))
    Continuebtn.pack()
    Gobackbtn = Button(PlayersRoundScene, text = "Back", command = lambda: Goback(PlayersRoundScene))
    Gobackbtn.pack()
    PlayersRoundScene.grid(row = 0 , column = 0 , sticky = "nsew")
def PlayersChoice(event):
    MainScene.grid_forget()
    Player1Score = 0
    Player2Score = 0
    PlayersChoiceScene = Frame(root, bg = "black")
    LabelPlayer1Name = Label(PlayersChoiceScene, text = "Player1 Name : ")
    LabelPlayer1Name.grid(row = 0, column = 0, sticky = "nsew")
    Player1NameEntry = Entry(PlayersChoiceScene, width = 30)
    Player2NameEntry = Entry(PlayersChoiceScene, width = 30)
    Player1NameEntry.grid(row = 0 , column = 1, sticky = "nsew")
    LabelPlayer2Name = Label(PlayersChoiceScene, text = "Player2 Name : ")
    LabelPlayer2Name.grid(row = 1, column = 0 , sticky ="nsew")
    Player2NameEntry.grid(row = 1, column = 1, sticky = "nsew")
    Submitbtn = Button(PlayersChoiceScene, text = "Submit", command = lambda: PlayersRound(PlayersChoiceScene,Player1NameEntry.get(),Player2NameEntry.get(),Player1Score,Player2Score))
    Submitbtn.grid(row = 3, column = 0 , sticky = "nsew")
    Gobackbtn = Button(PlayersChoiceScene, text = "Back", command = lambda: Goback(PlayersChoiceScene))
    Gobackbtn.grid(row = 6, column = 0, sticky = "nsew")
    PlayersChoiceScene.grid(row = 0, column = 0 , sticky = "nsew")
#=================Create mainScene==================================

MainScene = Frame(root, bg = "Black")
MainLabel = Label(MainScene, text = "Welcome to the Dice Game", bg = "black", fg = "white")
MainLabel.pack(fill = X)
CPUbtn = Button(MainScene, text = "Play against CPU", padx = 25, pady = 20)
CPUbtn.pack()
PlayersGamebtn = Button(MainScene, text = "2 players game", padx = 25, pady = 20)
Instructionsbtn = Button(MainScene, text = "Instructions", padx = 25, pady = 20)
CPUbtn.bind("<Button-1>", CPU_Choice)
CPUbtn.pack()
PlayersGamebtn.pack()
PlayersGamebtn.bind("<Button-1>", PlayersChoice)
Instructionsbtn.pack()
Instructionsbtn.bind("<Button-1>", Instructions)
exitbtn = Button(MainScene, text = "Exit", command = root.quit, padx = 25, pady = 20)
exitbtn.pack()
MainScene.grid(row = 0, column = 0, sticky = "nsew")
root.mainloop()