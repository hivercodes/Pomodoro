from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

checkbox = "✓"



window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=100, bg=YELLOW)
tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold" ))
timer_text.config(bg=YELLOW)
timer_text.pack()
canvas.create_image(100,112, image=tomato)
canvas.create_text(101,130, text="00:00", font=(FONT_NAME, 35, "bold" ))
canvas.pack()
start_button = Button(text="Start")
start_button.place(x=-30, y=290)
reset_button = Button(text="Reset")
reset_button.place(x=150, y=290)
check_box = Label(text=checkbox, fg=GREEN)
check_box.config(bg=YELLOW)
check_box.place(x=90, y=290)







window.mainloop()