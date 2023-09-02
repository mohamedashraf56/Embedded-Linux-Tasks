import tkinter as tk

def turn_on():
    # Update the LED state to "On" and change the LED color to green
    led_state.set("On")
    led_label.config(fg="green")

def turn_off():
    # Update the LED state to "Off" and change the LED color to red
    led_state.set("Off")
    led_label.config(fg="red")

# Create the main window
window = tk.Tk()
window.title("LED Control")

# Variable to track the LED state
led_state = tk.StringVar()
led_state.set("Off")

# Create a label to display the LED state
led_label = tk.Label(window, textvariable=led_state, font=("Arial", 50))
led_label.pack(pady=20)

# Create the "On" button
on_button = tk.Button(window, text="On", width=10, height=2, command=turn_on)
on_button.pack(pady=10)

# Create the "Off" button
off_button = tk.Button(window, text="Off", width=10, height=2, command=turn_off)
off_button.pack(pady=10)

# Start the main event loop
window.mainloop()
