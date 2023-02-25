from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    num = random.randint(0, 3)
    # 2. Print your variable to the console
    print(num)
    # 3. Get the user to enter something that they think is awesome
    awesome = simpledialog.askstring(title='Awesome?', prompt='What do you think is awesome?')
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if num == 0:
        messagebox.showinfo(message= awesome + ' is awesome!')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if num == 1:
        messagebox.showinfo(message= awesome + ' is ok.')
    if num == 2:
        messagebox.showwarning(message= awesome + ' is boring.')
    if num == 3:
        messagebox.showerror(message= awesome + '... is bad.')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
