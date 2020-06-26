#TIC TAC TOE using Tkinter module in Python

from tkinter import * # to import everything from tkinter module
from tkinter import messagebox # for alert message pop-up

root = Tk() # object or instance of Tk class
root.title('"Welcome to TicTacToe"')
root.geometry('375x300') # for window size
root.resizable(0,0) # for fixed window size 

player1 = StringVar()
player2 = StringVar()
p1 = StringVar()
p2 = StringVar()

# to enter player's name
Player1_entry = Entry(root,textvariable=player1,bd=5)
player2_entry = Entry(root,textvariable=player2,bd=5)
Player1_entry.grid(row=1, column=1, columnspan=8)
player2_entry.grid(row=2, column=1, columnspan=8)

button_click = True  # true represents button is not clicked yet
counter = 0  # initially count=0 as game is not started and player has not clicked any button


# widget label is used to write text on a window
# it takes some arguments like root,text,font etc
label1 = Label(root, text= ' TIC-TAC-TOE', fg='Blue', font= 'Times 19 bold')
label2 = Label(root, text= ' Player 1 Name:',font='Georgia 15',bg='white', fg='Red')
label3 = Label(root, text= ' Player 2 Name:',font='Georgia 15',bg='white', fg='Red')


# Grid is the arrangement of widgets (eg: Label)in a matrix form on a window
# Grid confirms the position where we want to arrange our widgets
# it takes argument as row and column
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)


# Now lets create a function called BtnClick
# It should perform two major tasks:
# Is should check whether that button is clicked already or not
# if that button is not clicked then obviously it is empty
# so if it's empty then player should be able to enter 'X' or 'O'
# if it is clicked previously then its not empty;
# so if player tries to click that button then it should give a warning pop up as "button already clicked"

def BtnClick(btn):
# we use global keyword to access the variable defined outside this function

    global counter
    global button_click
    global player1
    global player2
    global p1
    global p2

    if btn['text'] == ' ' and button_click == True:
        btn["text"] = 'X'
        # after the button has been clicked we should make it False to prevent further clicking
        button_click = False
        p1 = (f'{player1.get()} won the game!')
        # function that checks the winner every time after the button is clicked
        Winner_Check()
        # and now if we didn't get any winner; simply increase the counter variable
        # this counter variable is incremented each time player clicks the button
        counter += 1


    elif btn['text'] == ' ' and button_click == False:
        btn['text'] = 'O'
        # after the button has been clicked we should make it True to prevent further clicking
        button_click = True
        p2= (f'{player2.get()} won the game!')
        Winner_Check()
        counter += 1

    else:
        messagebox.showinfo('Tic-Tac-Toe', 'This Button is already used!')


# Now lets create a function that checks every possible conditions for a win
# there are 8 total conditions for winning the game (3 row wise, 3 column wise and 2 diagonal wise)
# the logic here is if any row ; column or diagonal is equal to 'X' or 'O' then there is a win
def Winner_Check():
    if (button1['text'] == button2['text'] == button3['text'] == 'X' or
        button4['text'] == button5['text'] == button6['text'] == 'X' or
        button7['text'] == button8['text'] == button9['text'] == 'X' or
        button1['text'] == button4['text'] == button7['text'] == 'X' or
        button2['text'] == button5['text'] == button8['text'] == 'X' or
        button3['text'] == button6['text'] == button9['text'] == 'X' or
        button1['text'] == button5['text'] == button9['text'] == 'X' or
        button3['text'] == button5['text'] == button7['text'] == 'X'):
        messagebox.showinfo("Tic-Tac-Toe", p1)
        root.destroy()
        # it is used to go out from the game menu when ok button is clicked


    elif (button1['text'] == button2['text'] == button3['text'] == 'O' or
        button4['text'] == button5['text'] == button6['text'] == 'O' or
        button7['text'] == button8['text'] == button9['text'] == 'O' or
        button1['text'] == button4['text'] == button7['text'] == 'O' or
        button2['text'] == button5['text'] == button8['text'] == 'O' or
        button3['text'] == button6['text'] == button9['text'] == 'O' or
        button1['text'] == button5['text'] == button9['text'] == 'O' or
        button3['text'] == button5['text'] == button7['text'] == 'O'):
        messagebox.showinfo("Tic-Tac-Toe", p2)
        root.destroy()

    # now lets see the condition for a tie/draw
    # the logic here is if count reaches 8; it means every button has been clicked 9 times already
    # so there is no any winner; hence game is a draw
    elif (counter == 8):
        messagebox.showinfo("Tic-Tac-Toe", "Game is a Tie!")
        root.destroy()


# Button is another type of widget in tkinter for creating buttons
# it takes different arguments like (window, text, fg, bg , height, width,command)
# argument command is used to trigger the action when that widget is clicked ... syntax: command = function_call
# here text = ' ' blank because text must be displayed inside the widget only when button is clicked

button1 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button1))
button1.grid(row=3,column=2)
button2 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button2))
button2.grid(row=3,column=3)
button3 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button3))
button3.grid(row=3,column=4)
button4 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button4))
button4.grid(row=4,column=2)
button5 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button5))
button5.grid(row=4,column=3)
button6 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button6))
button6.grid(row=4,column=4)
button7 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button7))
button7.grid(row=5,column=2)
button8 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button8))
button8.grid(row=5,column=3)
button9 = Button(root,text = ' ',font= 'Arial 10 bold',height=3,width=6,bg="Pink",fg="Black",command=lambda: BtnClick(button9))
button9.grid(row=5,column=4)

root.mainloop()

