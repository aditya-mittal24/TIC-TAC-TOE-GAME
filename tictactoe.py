from tkinter import *
root= Tk()
root.title("Tic Tac Toe")
player_no=1
inp1="1"
inp2="2"
inp3="3"
inp4="4"
inp5="5"
inp6="6"
inp7="7"
inp8="8"
inp9="9"

def button_click(button_no):
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global status
    global player_no
    global inp1
    global inp2
    global inp3
    global inp4
    global inp5
    global inp6
    global inp7
    global inp8
    global inp9
    status.grid_forget()
    if button_no==1:
        button1.grid_forget()
        if player_no==1:
            button1 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp1="X"
        elif player_no==2:
            button1 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp1="O"
    if button_no==2:
        button2.grid_forget()
        if player_no==1:
            button2 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp2 = "X"
        elif player_no==2:
            button2 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp2 = "O"
    if button_no==3:
        button3.grid_forget()
        if player_no==1:
            button3 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp3 = "X"
        elif player_no==2:
            button3 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp3 = "O"
    if button_no==4:
        button4.grid_forget()
        if player_no==1:
            button4 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp4 = "X"
        elif player_no==2:
            button4 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp4 = "O"
    if button_no==5:
        button5.grid_forget()
        if player_no==1:
            button5 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp5 = "X"
        elif player_no==2:
            button5 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp5 = "O"
    if button_no==6:
        button6.grid_forget()
        if player_no==1:
            button6 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp6 = "X"
        elif player_no==2:
            button6 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp6 = "O"
    if button_no==7:
        button7.grid_forget()
        if player_no==1:
            button7 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp7 = "X"
        elif player_no==2:
            button7 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp7 = "O"
    if button_no==8:
        button8.grid_forget()
        if player_no==1:
            button8 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp8 = "X"
        elif player_no==2:
            button8 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp8 = "O"
    if button_no==9:
        button9.grid_forget()
        if player_no==1:
            button9 = Button(root, text="X", padx=19, pady=14,font=("Arial",60),  fg="red")
            player_no=2
            status = Label(root, text="Player 2 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp9 = "X"
        elif player_no==2:
            button9 = Button(root, text="O", padx=16, pady=13, font=("Arial", 60))
            player_no=1
            status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
            inp9 = "O"
    if inp1==inp2==inp3=="X" :
        status = Label(root, text="Player 1 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no=3
    if inp1 == inp2 == inp3 == "O":
        status = Label(root, text="Player 2 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp4 == inp5 == inp6 == "X":
        status = Label(root, text="Player 1 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp4 == inp5 == inp6 == "O":
        status = Label(root, text="Player 2 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp7 == inp8 == inp9 == "X":
        status = Label(root, text="Player 1 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp7 == inp8 == inp9 == "O":
        status = Label(root, text="Player 2 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp1 == inp5 == inp9 == "X":
        status = Label(root, text="Player 1 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp1 == inp5 == inp9 == "O":
        status = Label(root, text="Player 2 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp3 == inp5 == inp7 == "X":
        status = Label(root, text="Player 1 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp3 == inp5 == inp7 == "O":
        status = Label(root, text="Player 2 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp1==inp4==inp7=="X" :
        status = Label(root, text="Player 1 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no=3
    if inp1 == inp4 == inp7 == "O":
        status = Label(root, text="Player 2 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp2==inp5==inp8=="X" :
        status = Label(root, text="Player 1 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no=3
    if inp2 == inp5 == inp8 == "O":
        status = Label(root, text="Player 2 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if inp3==inp6==inp9=="X" :
        status = Label(root, text="Player 1 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no=3
    if inp3 == inp6 == inp9 == "O":
        status = Label(root, text="Player 2 wins!!", bd=1, relief=SUNKEN,pady=12, bg="black")
        player_no = 3
    if player_no!=3:
        if inp1!="1" and inp2!="2" and inp3!="3" and inp4!="4" and inp5!="5" and inp6!="6" and inp7!="7" and inp8!="8" and inp9!="9":
            status = Label(root, text="Draw", bd=1, relief=SUNKEN, pady=12, bg="black")
            player_no = 3


    status.grid(row=3, column=1, sticky=W + E)
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
def button_game():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global status
    global player_no
    global inp1
    global inp2
    global inp3
    global inp4
    global inp5
    global inp6
    global inp7
    global inp8
    global inp9
    player_no = 1
    inp1 = "1"
    inp2 = "2"
    inp3 = "3"
    inp4 = "4"
    inp5 = "5"
    inp6 = "6"
    inp7 = "7"
    inp8 = "8"
    inp9 = "9"
    status.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    button4.grid_forget()
    button5.grid_forget()
    button6.grid_forget()
    button7.grid_forget()
    button8.grid_forget()
    button9.grid_forget()
    button1 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(1))
    button2 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(2))
    button3 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(3))
    button4 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(4))
    button5 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(5))
    button6 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(6))
    button7 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(7))
    button8 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(8))
    button9 = Button(root, text="", padx=40, pady=40, command=lambda: button_click(9))
    status = Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN, pady=12, bg="black")
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    status.grid(row=3, column=1, sticky=W + E)

button1= Button(root, text="", padx=40, pady=40, command= lambda : button_click(1))
button2= Button(root, text="", padx=40, pady=40, command= lambda : button_click(2))
button3= Button(root, text="", padx=40, pady=40, command= lambda : button_click(3))
button4= Button(root, text="", padx=40, pady=40, command= lambda : button_click(4))
button5= Button(root, text="", padx=40, pady=40, command= lambda : button_click(5))
button6= Button(root, text="", padx=40, pady=40, command= lambda : button_click(6))
button7= Button(root, text="", padx=40, pady=40, command= lambda : button_click(7))
button8= Button(root, text="", padx=40, pady=40, command= lambda : button_click(8))
button9= Button(root, text="", padx=40, pady=40, command= lambda : button_click(9))
button_exit= Button(root, text="Exit game", padx=10, pady=10, command= root.quit)
button_newgame= Button(root, text="New Game", padx=7, pady=10, command= button_game)



status1 = Label(root, text="Player 1=X                                                          Player 2=O", bd=1, relief=SUNKEN, anchor=W,pady=4, bg="black")
status= Label(root, text="Player 1 turn!", bd=1, relief=SUNKEN,pady=12, bg="black")
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button_exit.grid(row=3,column=2)
button_newgame.grid(row=3,column=0)
status1.grid(row=4, column=0, sticky=W + E, columnspan=3)
status.grid(row=3, column=1, sticky=W + E)




root.mainloop()
