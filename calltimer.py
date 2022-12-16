import datetime
import pytz
import pyperclip
import pyautogui
import time

# Get the AEST time zone
aest = pytz.timezone("Australia/Sydney")

while True:
  # Calculate the number of hours since May 28, 2022, 5:52:10 PM AEST in the AEST time zone
  current_time = datetime.datetime.now(aest)
  target_time = datetime.datetime(2022, 5, 28, 17, 52, 10, tzinfo=aest)
  time_difference = current_time - target_time
  hours = time_difference.total_seconds() / 3600

  # Copy the number of hours to the clipboard
  pyperclip.copy(hours)

  # Switch to Discord and press Ctrl+V and Enter
  pyautogui.hotkey("ctrl", "v")
  pyautogui.press("enter")

  # Print a message indicating that the value has been pasted
  print(f"Number of hours since May 28, 2022, 5:52:10 PM AEST in the AEST time zone pasted to Discord: {hours}")

  # Pause the script for 1 hour
  time.sleep(3600)
