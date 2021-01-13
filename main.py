from tkinter import *
import math
reps = 0
timer = None
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

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg = GREEN)
window.geometry('200x224')



timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=GREEN, fg= YELLOW)
timer_label.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg = GREEN, highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=1, column=1)

def set_counter():
    global reps
    if reps in [0, 2, 4, 6]:
        timer_label['text'] ='Work'
        count_down(count=WORK_MIN*60)
    elif reps in [1, 3, 5]:
        timer_label.config(text='Break', fg=PINK)
        count_down(count=SHORT_BREAK_MIN*60)
    elif reps == 7:
        count_down(count=LONG_BREAK_MIN*60)
        timer_label.config(text='Break', fg= RED)


def count_down(count=1500):
    time_min = math.floor(count/60)
    if time_min <= 9:
        time_min = '0' + str(time_min)
    time_sec = count % 60
    if time_sec <= 9:
        time_sec = '0' + str(time_sec)
    canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        if reps % 2 == 0:
            check_mark['text'] = '🗸'
        reps = reps + 1
        set_counter()

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=GREEN, fg=YELLOW)
    check_mark.config(bg=GREEN, fg='green', font=(FONT_NAME, 35, 'bold'))



start_button = Button(text='Start', bg=YELLOW, highlightthickness=0, command=set_counter)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(bg= GREEN, fg='green', font=(FONT_NAME, 35, 'bold'))
check_mark.grid(column=1, row=3)



window.mainloop()