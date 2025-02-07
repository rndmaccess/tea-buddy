import tkinter as tk
import tkinter.ttk as ttk
object_list = list()

def write_text(frame, line, anchor_nw=True):
    neon_green = "#228B22"
    label = tk.Label(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15))

    if anchor_nw:
        label.pack(side="top", anchor="nw")
    else:
        label.pack(side="top")

    for char in line:
        label.config(text=label.cget("text") + char)
        frame.update_idletasks()
        frame.after(100)

    # Keep all the labels we add to the screen so we can clear them later!
    object_list.append(label)
    return label

def write_button(frame, button, line):
    for char in line:
        button.config(text=button.cget("text") + char)
        frame.update_idletasks()
        frame.after(100)

    # Keep all the buttons we add to the screen so we can clear them later!
    object_list.append(button)
    return button

def clear_screen():
    for obj in object_list:
        obj.destroy()

def start_timer(frame, total_secs):
    seconds = total_secs
    remaining_mins, remaining_secs = divmod(seconds, 60)
    timer_label = init_timer(frame, remaining_mins, remaining_secs)
    bar = init_bar(frame)

    while seconds:
        remaining_mins, remaining_secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(remaining_mins, remaining_secs)
        timer_label.config(text=timer + " on the clock -_-")
        frame.after(1000, update_progress(frame, bar, seconds, total_secs))
        seconds -= 1

def update_progress(frame, bar, remaining_secs, total_secs):
    percentage = 100 - ((remaining_secs / total_secs) * 100)
    bar["value"] = percentage
    frame.update_idletasks()

def init_timer(frame, remaining_mins, remaining_secs):
    timer = '{:02d}:{:02d}'.format(remaining_mins, remaining_secs)
    timer_text = timer + " on the clock -_-"
    return write_text(frame, timer_text)

def init_bar(frame):
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("custom.Horizontal.TProgressbar", background="green", troughcolor="gray", thickness=10)
    progress = ttk.Progressbar(frame, orient="horizontal", mode="determinate", style="custom.Horizontal.TProgressbar")
    progress["value"] = 0
    progress.pack(side="top", anchor="nw")
    object_list.append(progress)
    return progress

def display_welcome_text(frame):
    bullet_pt = "\u2022"
    line_one = "Tea Time :D"
    line_two = "What kind of tea are you having?"
    black_tea = bullet_pt + " Black Tea 5:00"
    green_tea = bullet_pt + " Green Tea 3:00"
    white_tea = bullet_pt + " White Tea 3:00"
    fruit_tea = bullet_pt + " Fruit Tea 5:00"
    herbal_tea = bullet_pt + " Herbal Tea 5:00"
    custom_tea = bullet_pt + " Custom Tea"

    write_text(frame, line_one)
    write_text(frame, line_two)

    neon_green = "#228B22"
    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="Black Tea", total_secs=300),
                       highlightbackground="#767674")
    button.pack(side="top", anchor="nw")
    write_button(frame, button, black_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="Green Tea", total_secs=180),
                       highlightbackground="#767674")
    button.pack(side="top", anchor="nw")
    write_button(frame, button, green_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="White Tea", total_secs=180),
                       highlightbackground="#767674")
    button.pack(side="top", anchor="nw")
    write_button(frame, button, white_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="Fruit Tea", total_secs=300),
                       highlightbackground="#767674")
    button.pack(side="top", anchor="nw")
    write_button(frame, button, fruit_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="Herbal Tea", total_secs=300),
                       highlightbackground="#767674")
    button.pack(side="top", anchor="nw")
    write_button(frame, button, herbal_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: make_custom_tea(frame=frame),
                       highlightbackground="#767674")
    button.pack(side="top", anchor="nw")
    write_button(frame, button, custom_tea)

def make_custom_tea(frame):
    black_bg = '#111111'

    new_window = tk.Toplevel(frame)
    new_window.configure(background=black_bg)
    new_window.title("Enter Tea Time")
    new_window.resizable(False, False)
    new_window.geometry("400x200")

    write_text(new_window, "Number of seconds: ", False)
    entry = tk.Entry(new_window, font=("Arial", 15))
    entry.pack(side="top", anchor="center", expand=True)

    button = tk.Button(new_window, text="Submit", command=lambda: submit_input(frame=frame, new_window=new_window, entry=entry))
    button.pack()

    new_window.mainloop()

def submit_input(frame, new_window, entry):
    secs = int(entry.get())
    new_window.destroy()
    display_timing_text(frame=frame, tea_type="Custom Tea", total_secs=secs)

def display_timing_text(frame, tea_type, total_secs):
    clear_screen()
    line_one = "> " + tea_type
    line_two = "Timing your " + tea_type + "!"

    write_text(frame, line_one)
    write_text(frame, line_two)
    start_timer(frame, total_secs)
    clear_screen()
    display_finish_text(frame)

def display_finish_text(frame):
    line_one = "Times up!"
    line_two = "Your tea is ready"
    line_three = "Enjoy ^_^"

    write_text(frame, line_one)
    write_text(frame, line_two)
    write_text(frame, line_three)

def main():
    root = tk.Tk()
    black_bg = '#111111'
    frame = tk.Frame(root, bg=black_bg)
    frame.pack(padx=20, pady=20, anchor="nw")
    root.configure(background=black_bg)
    root.title("Title")
    root.geometry("1024x768")

    display_welcome_text(frame)

    root.mainloop()

if __name__ == "__main__":
    main()