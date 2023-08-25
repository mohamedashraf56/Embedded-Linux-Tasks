#!/usr/bin/python3
import webbrowser
#my favorite websites (my Social media)
print ("My Social media\n1-GITHUB \n2-Linkedin \n3-Instagram \n4-Facebook")
URL= int (input ("Choose 1 ,2 , 3 or 4 : "))

#my Social Media links 'URL'
websites= {1:"https://github.com/mohamedashraf56",
           2:"https://www.linkedin.com/in/mohamed-ashraf-7a6593246/?fbclid=IwAR0BKLYXOxh4FPv3IkIOa7qSSxjL4vFs-p7QJ7Qpta5od7bRTTz7zImQTqw",
           3:"https://l.facebook.com/l.php?u=https%3A%2F%2Finstagram.com%2Fmohamed_ashraf_ezzeldin%3Futm_source%3Dqr%26igshid%3DMzNlNGNkZWQ4Mg%253D%253D%26fbclid%3DIwAR1q1GGFKqEH2HIq1DRCPq_doZHifLHttZtjbRr6H5lex_fb8feioJ2vaXE&h=AT2ORb1cl3iOkS5TsxkcyttBzZHqxePnI93gre72cTBoEHVgWc4nRqA37syshkmsSOZqDQX9YUvVO7qoCpbqbop3UkTkoOkLo7xSK0Qq-wA8woXcu8HcuCT3j_7CTQ",
           4:"https://www.facebook.com/profile.php?id=100018990008224&mibextid=ZbWKwL"}
if  URL in websites :
    webbrowser.open_new_tab(websites[URL])
print (websites[URL])
