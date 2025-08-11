import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT_NAME = "Courier"
reps = 0
timer = None

# ---------------------------- TIMER RESET ----------------------------- #
def reset_timer():
    global reps, timer
    if timer:
        window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg="green")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg="red")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg="blue")
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg="green")

# ---------------------------- COUNTDOWN MECHANISM --------------------- #
def count_down(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔" * (reps // 2)
        check_marks.config(text=marks)

# ---------------------------- UI SETUP -------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")

title_label = tk.Label(text="Timer", fg="green", bg="#f7f5dd",
                       font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")  # You need a tomato.png file in the same folder
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg="green", bg="#f7f5dd")
check_marks.grid(column=1, row=3)

window.mainloop()
