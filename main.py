from tkinter import *
import math

# CONSTANTS
BACKGROUND = "#C7D14F"
WHITE = "#FFFFFF"
FONT_NAME = "test"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = "00:00"


# TIMER
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_canvas.itemconfig(title_image, image=title_timer)
    checkmark.config(text="")

    global reps
    reps = 0


# TIMER CODE
def start_timer():
    global reps

    if reps == 8:
        reps = 1
    else:
        reps += 1

    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title_canvas.itemconfig(title_image, image=title_work)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_canvas.itemconfig(title_image, image=title_break)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_canvas.itemconfig(title_image, image=title_break)


# COUNTDOWN CODE
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" # correct seconds formatting

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) # actual counting looping until 0
    else: # when timer hits zero, restart timer, add a checkmark if needed
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


# UI

window = Tk()
window.title("Pomodoro")
window.config(padx=40, pady=20, bg=BACKGROUND)

# TOMATO & TEXT
canvas = Canvas(width=200,height=232, bg=BACKGROUND, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 116, image=tomato_image)
canvas.grid(column=1, row=1)

timer_text= canvas.create_text(102, 150, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))

# TITLE
title_canvas = Canvas(width=250,height=80, bg=BACKGROUND, highlightthickness=0)

title_timer = PhotoImage(file="title_timer.png")
title_break = PhotoImage(file="title_break.png")
title_work = PhotoImage(file="title_work.png")

title_image = title_canvas.create_image(125, 30, image=title_timer)
title_canvas.grid(column=1, row=0)

# BUTTONS
button_start = Button(command=start_timer)
button_start_image = PhotoImage(file="button_start.png")
button_start.config(image=button_start_image, highlightthickness=0, bd=0, relief="flat", bg=BACKGROUND, activebackground=BACKGROUND)
button_start.grid(column=0, row=2)

button_reset = Button(command=reset_timer)
button_reset_image = PhotoImage(file="button_reset.png")
button_reset.config(image=button_reset_image, highlightthickness=0, bd=0, relief="flat", bg=BACKGROUND, activebackground=BACKGROUND)
button_reset.grid(column=2, row=2)

# CHECKS
checkmark = Label(fg=WHITE, bg=BACKGROUND, font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=2)



window.mainloop()