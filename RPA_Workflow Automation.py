import pyautogui

# Example of opening a browser and typing into a search box
pyautogui.hotkey('ctrl', 't')  # Open new tab
pyautogui.write('www.example.com')  # Type the URL
pyautogui.press('enter')  # Press enter to go to the website
