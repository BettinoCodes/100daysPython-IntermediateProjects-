import math
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
REPS = 1
mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    global REPS
    window.after_cancel(timer)
    REPS = 1
    top_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    reps_25 = [1,3,5,7]
    reps_short = [2,4,6]

    if REPS in reps_25:
        count_down(work_sec)
        top_label.config(text="WORK!", fg=RED)
    elif REPS in reps_short:
        count_down(short_break)
        top_label.config(text="BREAK!", fg=PINK)
    else:
        count_down(long_break)
        top_label.config(text="BIG BREAK!!", fg= GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global mark
    global REPS
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_min < 1 and count_sec < 10:
        count_sec = f"0{int(count_sec)}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    if count_min == 0 and count_sec == "00":
        REPS += 1
        start_timer()
        if REPS > 1 and REPS%2 != 0:
            mark += "✔"
            check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

top_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
top_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="Start", width=7, font=(FONT_NAME, 18, "bold"), bg="red", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", width=7, font=(FONT_NAME, 18, "bold"), bg="white", highlightthickness=0, command=reset_time)
reset_button.grid(column=2,row=2)

check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)
window.mainloop()
