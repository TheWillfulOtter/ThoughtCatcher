from tkinter import *
import keyword

def main():

# Keystroke of ALT + X invokes
    shortcut ='alt+x'
    def on_triggered():
# GUI to enter text
        keyboard.add_hotkey(shortcut, on_triggered)
        root = Tk()
        w = Label(root, text="Capture what?")
        w.pack()



# GUI passes text to



# open file, append file, close file



# close GUI
        root.mainloop()


    on_triggered()


if __name__ == '__main__':
    main()