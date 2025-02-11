import tkinter as tk
import tkinter.ttk as ttk
object_list = list()

# Write an immutable label to the screen!
def write_text(frame, line, anchor_nw=True):
    neon_green = "#228B22"
    label = tk.Label(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15))

    # Whether to anchor the text to the north-west side of the screen (top-left)
    if anchor_nw:
        label.pack(side="top", anchor="nw")
    else:
        label.pack(side="top")

    # Display each letter one at a time!
    for char in line:
        label.config(text=label.cget("text") + char)
        frame.update_idletasks() # Refresh the screen after we update the text
        frame.after(100) # Wait 100 milliseconds before displaying the next letter!

    # Keep all the labels we add to the screen so we can clear them later!
    object_list.append(label)
    return label

# Write a button to the screen (This is used to display each tea option)
def write_button(frame, button, line):
    # Display each letter one at a time!
    for char in line:
        button.config(text=button.cget("text") + char)
        frame.update_idletasks() # Refresh the screen after we update the text
        frame.after(100) # Wait 100 milliseconds before displaying the next letter!

    # Keep all the buttons we add to the screen so we can clear them later!
    object_list.append(button)
    return button

def clear_screen():
    for obj in object_list:
        obj.destroy()

# This method is used to both increase the progress bar and count down the timer
def start_timer(frame, total_secs):
    seconds = total_secs
    remaining_mins, remaining_secs = divmod(seconds, 60)
    timer_label = init_timer(frame, remaining_mins, remaining_secs)
    bar = init_bar(frame)

    # While there are seconds remaining update the progress bar and the timer!
    while seconds:
        remaining_mins, remaining_secs = divmod(seconds, 60)
        # Format the remaining minutes and seconds in a digital clock format!
        timer = '{:02d}:{:02d}'.format(remaining_mins, remaining_secs)
        timer_label.config(text=timer + " on the clock -_-")
        frame.after(1000, update_progress_bar(frame, bar, seconds, total_secs)) # Update the progress bar after 1 second
        seconds -= 1

def update_progress_bar(frame, bar, remaining_secs, total_secs):
    percentage = 100 - ((remaining_secs / total_secs) * 100) # Calculate the remaining time left!
    bar["value"] = percentage
    frame.update_idletasks() # Refresh the screen after we update the text

def init_timer(frame, remaining_mins, remaining_secs):
    # Format the remaining minutes and seconds in a digital clock format!
    timer = '{:02d}:{:02d}'.format(remaining_mins, remaining_secs)
    timer_text = timer + " on the clock -_-"
    return write_text(frame, timer_text)

def init_bar(frame):
    # Style the progress bar!
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("custom.Horizontal.TProgressbar", background="green", troughcolor="gray", thickness=10)
    progress = ttk.Progressbar(frame, orient="horizontal", mode="determinate", style="custom.Horizontal.TProgressbar")
    progress["value"] = 0
    progress.pack(side="top", anchor="nw")

    # Keep all the progress bars we add to the screen so we can clear them later!
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

    # Write each tea option to the screen!
    neon_green = "#228B22"
    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="Black Tea", total_secs=300),
                       highlightbackground="#767674", width=20)
    button.pack(side="top", anchor="nw")
    write_button(frame, button, black_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="Green Tea", total_secs=180),
                       highlightbackground="#767674", width=20)
    button.pack(side="top", anchor="nw")
    write_button(frame, button, green_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="White Tea", total_secs=180),
                       highlightbackground="#767674", width=20)
    button.pack(side="top", anchor="nw")
    write_button(frame, button, white_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="Fruit Tea", total_secs=300),
                       highlightbackground="#767674", width=20)
    button.pack(side="top", anchor="nw")
    write_button(frame, button, fruit_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: display_timing_text(frame=frame, tea_type="Herbal Tea", total_secs=300),
                       highlightbackground="#767674", width=20)
    button.pack(side="top", anchor="nw")
    write_button(frame, button, herbal_tea)

    button = tk.Button(frame, text="", fg=neon_green, bg='#111111', font=("Arial", 15),
                       command=lambda: make_custom_tea(frame=frame),
                       highlightbackground="#767674", width=20)
    button.pack(side="top", anchor="nw")
    write_button(frame, button, custom_tea)

def make_custom_tea(frame):
    black_bg = '#111111'

    # Make a new window for inputting the minutes and seconds for the custom tea!
    new_window = tk.Toplevel(frame)
    new_window.configure(background=black_bg)
    new_window.title("Enter Tea Time")
    new_window.resizable(False, False) # Make the popup window not resizable!
    new_window.geometry("400x200")

    # Add the minutes box and seconds box to the middle of the screen along with text for each box in the new window!
    write_text(new_window, "Minutes: ", False)
    min_entry = tk.Entry(new_window, font=("Arial", 15))
    min_entry.pack(side="top", anchor="center", expand=True)
    write_text(new_window, "Seconds: ", False)
    sec_entry = tk.Entry(new_window, font=("Arial", 15))
    sec_entry.pack(side="top", anchor="center", expand=True)

    # Add a submission button for submitting the custom time!
    button = tk.Button(new_window, text="Submit", command=lambda: submit_input(frame=frame, new_window=new_window,
                                                                               entry_min=min_entry, entry_sec=sec_entry))
    button.pack()

    new_window.mainloop()

def submit_input(frame, new_window, entry_min, entry_sec):
    mins = 0
    secs = 0

    # If either input box is left blank the program will assume 0 seconds for that entry!
    if entry_min.get():
        mins = int(entry_min.get())
    if entry_sec.get():
        secs = int(entry_sec.get())

    total_secs = (mins * 60) + int(secs) # Convert the number of mins and secs inputted to seconds
    new_window.destroy()
    display_timing_text(frame=frame, tea_type="Custom Tea", total_secs=total_secs)

# Display the timing text and start the timer!
def display_timing_text(frame, tea_type, total_secs):
    clear_screen()
    line_one = "> " + tea_type
    line_two = "Timing your " + tea_type + "!"

    write_text(frame, line_one)
    write_text(frame, line_two)
    start_timer(frame, total_secs)
    clear_screen()
    display_finish_text(frame)

# Once our tea is done this will display the finishing text!
def display_finish_text(frame):
    line_one = "Times up!"
    line_two = "Your tea is ready"
    line_three = "Enjoy ^_^"

    write_text(frame, line_one)
    write_text(frame, line_two)
    write_text(frame, line_three)

def main():
    # Create the main window and style it accordingly!
    root = tk.Tk()
    black_bg = '#111111'
    frame = tk.Frame(root, bg=black_bg)
    frame.pack(padx=20, pady=20, anchor="nw")
    root.configure(background=black_bg)
    root.title("Title")
    root.geometry("1024x768")

    # Display the first page for our program
    display_welcome_text(frame)

    root.mainloop()

if __name__ == "__main__":
    main()