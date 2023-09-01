import pyautogui
import time
import webbrowser


webbrowser.open('https://mail.google.com/mail/u/0/?pli=1#inbox')

email_location = (100, 200)  # Adjust the coordinates based on your email 
pyautogui.moveTo(*email_location)

# Click to open the email
pyautogui.click()

time.sleep(2)  # Wait for the email to load


# Mark the email as read
read_button_location = (500, 300)  # Adjust the coordinates based on your email 
pyautogui.moveTo(*read_button_location)
pyautogui.click()

time.sleep(1)  

# Repeat the process for other emails as needed
# You can use loops to automate the process for multiple emails
