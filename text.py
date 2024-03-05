import time
import pyautogui

# Wait for a few seconds to give time to focus on the Telegram app
time.sleep(5)

# Message to be sent
message = "Enter your message"

# Number of times to send the message
num_messages = 100

for _ in range(num_messages):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(1)  # Adjust the delay as needed