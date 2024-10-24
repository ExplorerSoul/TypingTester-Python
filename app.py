# Import necessary modules
import random
import nltk
from tkinter import *
import tkinter.font as font
from nltk.corpus import words

# Download the words corpus (run once if not already downloaded)
nltk.download('words')

# Fetch list of words from nltk corpus
words_list = words.words()

# Initialize score-related variables
score = 0
missed = 0
time_elapsed = 0
count = 0
total_words = 10  # Set a fixed count for the number of words

# Pick random words from nltk corpus
game_words = random.sample(words_list, total_words)

# Create the main window
wn = Tk()
wn.geometry('700x600')
wn.title("Typing Test By PythonGeeks")
wn.config(bg='LightBlue1')


# Time function to count seconds and end game after 10 words
def timeFunc():
    global time_elapsed, count
    if count < total_words:  # If count is less than total_words, continue updating time
        time_elapsed += 1
        timer.config(text=time_elapsed)
        timer.after(1000, timeFunc)
    else:  # When 10 words have been attempted, show the results
        show_results()


# Function to start the game when "Start" is clicked
def startGame():
    global score, missed, count, time_elapsed

    # Reset all values
    score = 0
    missed = 0
    time_elapsed = 0
    count = 0

    # Clear previous words and input
    userInput.delete(0, END)
    nextWord.config(text="")
    scoreboard.config(text=score)
    timer.config(text=time_elapsed)

    # Start the game and time counting
    nextWord.config(text=random_word())
    timeFunc()


# Function to display the final results
def show_results():
    result_label = Label(wn, text=f"Results:\nTime Taken: {time_elapsed} sec\nScore: {score}\nMissed: {missed}",
                         font=('arial', 20, 'italic bold'), fg='grey')
    result_label.place(x=180, y=350)

    # Disable the input box
    userInput.config(state=DISABLED)


# Function to shuffle and get the next word
def random_word():
    random.shuffle(game_words)
    return game_words[0]


# Main game function that runs each time Enter is pressed
def mainGame(event):
    global score, missed, count

    if count == 0 and time_elapsed == 0:  # Start game on first Enter press
        startGame()

    # Check if the user typed the correct word
    if userInput.get().lower() == nextWord['text'].lower():
        score += 1
        scoreboard.config(text=score)
    else:
        missed += 1

    count += 1

    # If we are still within the word limit, show the next word
    if count < total_words:
        nextWord.config(text=random_word())
        userInput.delete(0, END)
    else:
        show_results()


# Creating the layout and widgets

# Title label
heading_label = Label(wn, text="Welcome to \n PythonGeeks Typing Test", bg='azure2', fg='black',
                      font=('Courier', 20, 'bold'))
heading_label.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.15)

# "Your Score" label and scoreboard
score_label = Label(wn, text="Your Score:", font=('arial', 20, 'bold'), fg='red')
score_label.place(x=10, y=120)
scoreboard = Label(wn, text=score, font=('arial', 25, 'bold'), fg='blue')
scoreboard.place(x=150, y=160)

# "Time Elapsed" label and timer
timer_label = Label(wn, text="Time Elapsed:", font=('arial', 20, 'bold'), fg='red')
timer_label.place(x=500, y=120)
timer = Label(wn, text=time_elapsed, font=('arial', 25, 'bold'), fg='blue')
timer.place(x=550, y=160)

# Instructions and current word display
nextWord = Label(wn, text="Press Enter to start typing", font=('arial', 20, 'italic bold'), fg='black')
nextWord.place(x=100, y=240)

# User input field
userInput = Entry(wn, font=('arial', 25, 'bold'), bd=10, justify='center')
userInput.place(x=150, y=330)
userInput.focus_set()

# Start Button
start_btn = Button(wn, text="Start", bg='old lace', fg='black', width=20, height=2, command=startGame)
start_btn['font'] = font.Font(size=12)
start_btn.place(x=200, y=450)

# Bind the Enter key to the mainGame function
wn.bind('<Return>', mainGame)

# Start the main loop
wn.mainloop()
