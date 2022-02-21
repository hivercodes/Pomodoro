from tkinter import *
import math

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

def start_timer():
    count_down(2 * 10)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

checkbox = "✓"




window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=50, bg=YELLOW)


tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold" ))
timer_text.config(bg=YELLOW)
timer_text.grid(column=1, row=0)
canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(101,130, text="00:00", font=(FONT_NAME, 35, "bold" ))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=3)
check_box = Label(text=checkbox, fg=GREEN, font=(FONT_NAME, 30, "bold" ))
check_box.config(bg=YELLOW)
check_box.grid(column=1, row=4)







window.mainloop()