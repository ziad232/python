from tkinter import *
import random


window = Tk()
window.title("TIC_TAC_TOE")


def nextturn(row, col):
    global player
    global i
    global y
    if gamebtns[row][col]["text"] == "" and checkwinner() == False:
        if player == players[0]:
            gamebtns[row][col]["text"] = player
            if checkwinner() == False:
                player = players[1]
                label.config(text=(f"{player} turn"))
            elif checkwinner() == True:
                i += 1
                label.config(text=(f"{player} win"))
                score.config(text=(f"One [x] {i}"))
            elif checkwinner() == "tie":
                label.config(text=(f"tie"))
        elif player == players[1]:
            gamebtns[row][col]["text"] = player
            if checkwinner() == False:
                player = players[0]
                label.config(text=(f"{player} turn"))
            elif checkwinner() == True:
                y += 1
                label.config(text=(f"{player} win"))
                score2.config(text=(f"Two [o] {y}"))
            elif checkwinner() == "tie":
                label.config(text=(f"tie"))


def checkwinner():
    for row in range(3):
        if gamebtns[row][0]["text"] == gamebtns[row][1]["text"] == gamebtns[row][2]["text"] != "":
            gamebtns[row][0].config(bg="cyan")
            gamebtns[row][1].config(bg="cyan")
            gamebtns[row][2].config(bg="cyan")
            return True
    for col in range(3):
        if gamebtns[0][col]["text"] == gamebtns[1][col]["text"] == gamebtns[2][col]["text"] != "":
            gamebtns[0][col].config(bg="cyan")
            gamebtns[1][col].config(bg="cyan")
            gamebtns[2][col].config(bg="cyan")
            return True
    if gamebtns[0][0]["text"] == gamebtns[1][1]["text"] == gamebtns[2][2]["text"] != "":
        gamebtns[0][0].config(bg="cyan")
        gamebtns[1][1].config(bg="cyan")
        gamebtns[2][2].config(bg="cyan")
        return True
    if gamebtns[0][2]["text"] == gamebtns[1][1]["text"] == gamebtns[2][0]["text"] != "":
        gamebtns[0][2].config(bg="cyan")
        gamebtns[1][1].config(bg="cyan")
        gamebtns[2][0].config(bg="cyan")
        return True
    if empty() == True:
        for row in range(3):
            for col in range(3):
                gamebtns[row][col].config(bg="red")
        return "tie"
    else:
        return False


def restart():
    label.config(text=(f"{player} turn"))
    for row in range(3):
        for col in range(3):
            gamebtns[row][col].config(text="", bg="#f2f2f2")


def reset():
    restart()
    global i
    i=0
    score.config(text=(f"One [x] {i}"))
    global y
    y=0
    score2.config(text=(f"Two [o] {y}"))


def empty():
    place = 9
    for row in range(3):
        for col in range(3):
            if gamebtns[row][col]["text"] != "":
                place -= 1

    if place == 0:
        return True
    else:
        return False


i = 0
y = 0
button2 = Button(text="reset", font=("consolas", 20), command=reset)
button2.pack()
players = ["x", "o"]
player = random.choice(players)
label = Label(text=(f"{player} turn"), font=("consolas", 40))
label.pack()
score = Label(text=(f"One [x] {i}"), font=("consolas", 40))
score.pack()
score2 = Label(text=(f"Two [o] {y}"), font=("consolas", 40))
score2.pack()

button = Button(text="restart", font=("consolas", 20), command=restart)
button.pack()


btnsframe = Frame(window)
btnsframe.pack()
gamebtns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for row in range(3):
    for col in range(3):
        gamebtns[row][col] = Button(btnsframe, text="", font=(
            "consolas", 40), command=lambda row=row, col=col: nextturn(row, col), width=4, height=1)
        gamebtns[row][col].grid(row=row, column=col)

window.mainloop()
