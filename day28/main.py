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

# ---------------------------- VARIABLES ------------------------------- #
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count = LONG_BREAK_MIN * 60
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        title_label.config(text="Break", fg=PINK)
    else:
        count = WORK_MIN * 60
        title_label.config(text="Work", fg=GREEN)

    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    mins = math.floor(count / 60)
    secs = math.floor(count % 60)
    canvas.itemconfig(timer_text, text=f"{mins:02d}:{secs:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 24), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(text="", fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
