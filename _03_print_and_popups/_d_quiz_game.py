from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    correct = simpledialog.askstring(title='Question', prompt='Is this a test?')
    #      // 2.  Ask the user a question 
    if correct == 'yes':
        messagebox.showinfo(message='Correct!')
        score = score+1
    else:
        messagebox.showerror(message='Incorrect.')
        score = score-1
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
    correct = simpledialog.askstring(title='Question', prompt='Is this another question?')
    if correct == 'yes':
        messagebox.showinfo(message='Correct!')
        score += 1
    else:
        messagebox.showerror(message='Incorrect.')
        score -= 1
    messagebox.showinfo(message='The quiz is over! Your score was ' +str(score) + '.')

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
