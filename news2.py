#Import all libraries
import requests
from customtkinter import *
import time 

#Initialize Custom tkinter window and set properties
app = CTk()
app.title('CSCZ')
app.geometry('1400x700')
app._set_appearance_mode('light')

index1 = 0
index2 =  1

#Function to display next story
def nextbutton_pressed():
 global index1
 index1 += 1
 update()
#Function to display previous story
def prevbutton_pressed():
 global index1
 index1 -= 1
 update()

#Initialize all labels, buttons and text boxes and set characteristics
title = CTkLabel(app, text = 'CRAZYNEWZ', font = ('papyrus', 25), text_color='black', bg_color='#EBEBEA')

topstory1 = CTkLabel(app, text = '',  font = ('papyrus', 15), text_color='blue', bg_color='#EBEBEA')
topstory2 = CTkLabel(app, text = '', font = ('papyrus', 15), text_color='blue', bg_color='#EBEBEA')
allstory = CTkLabel(app, text = '', font = ('papyrus', 15), text_color='black', bg_color='#EBEBEA')

nextbutton = CTkButton(app, text = 'next story',font = ('papyrus', 15), text_color='black', bg_color='#EBEBEA', command = nextbutton_pressed )
prevbutton = CTkButton(app, text = 'previous stories',font = ('papyrus', 15), text_color='black', bg_color='#EBEBEA', command = prevbutton_pressed )

sports = CTkLabel(app, text = '',  font = ('papyrus', 15), text_color='black', bg_color='#EBEBEA')
label = CTkLabel(app, text = 'Search by keword here ↓↓↓↓',  font = ('papyrus', 15), text_color='black', bg_color='#EBEBEA')
entry = CTkEntry(app, font = ('papyrus', 20), text_color='magenta', corner_radius=32, bg_color='#EBEBEA')
label2 = CTkLabel(app, text = 'Change language here ↓↓↓↓',  font = ('papyrus', 15), text_color='black', bg_color='#EBEBEA')
entry2 = CTkEntry(app, font = ('papyrus', 20), text_color='magenta', corner_radius=32, bg_color='#EBEBEA')

#Function to get input from entry box, and update the screen based on the given input
def get_input():
 global keyword
 global lang
 
 keyword = entry.get()
 keyword = str(keyword)
 
 lang = entry2.get()
 lang = str(lang)
 print(keyword)
 update()




keyword='apple'
lang = 'en'

#Won't give my API key away, not that it matters that much anyway. 
api = 'API_KEY'


#Main function
def update():
 global index1
 global index2

 #URL's for getting news data from GNnews 
 topurl = f'https://gnews.io/api/v4/top-headlines?category=politics&lang=en&max=30&apikey={api}'
 allurl = f'https://gnews.io/api/v4/top-headlines?category=general&lang={lang}&max=30&q={keyword}&apikey={api}'
 sportsurl = f''

 #Get top news headlines in a JSON file 
 topdata = requests.get(topurl)
 topdata = topdata.json()

 #Get news in a JSON file to be filtered through later 
 alldata = requests.get(allurl)
 alldata = alldata.json()


 
 #Find import information for two top stories from the JSON file and display them
 story1title = topdata['articles'][0]['title']
 story1desc = topdata['articles'][0]['description']
 story1source = topdata['articles'][0]['source']
 topstory1.configure(text = f'''
 {story1title}
    {story1desc}
                    Source: {story1source}''')
 #Second top story
 story2title = topdata['articles'][1]['title']
 story2desc = topdata['articles'][1]['description']
 story2source = topdata['articles'][1]['source']
 topstory2.configure(text = f'''
 {story2title}
    {story2desc}
                    Source: {story2source}''')
 

 
 #Finds and gets news headlines to be filtered through later
 alltitle = alldata['articles'][index1]['title']
 alldesc = alldata['articles'][index1]['description']
 allsource = alldata['articles'][index1]['source']
 allstory.configure(text = f'''
 {alltitle}
    {alldesc}
                    Source: {allsource}
                    ''')
#Checks if index is out of range
 if index1 < 0:
  index1 = 1
 if index2 < 0:
  index2 = 0

 print(topdata)
 
#Auto update stories after given amount of time
app.after(1000000, update)


#Bind both entry boxes to retrieve input 
entry.bind("<Return>", lambda event: get_input())
entry2.bind("<Return>", lambda event: get_input())


#Call functions and pack all widgets
update()

title.pack()
topstory1.pack()
topstory2.pack()

allstory.pack()
nextbutton.pack()
prevbutton.pack()

label.pack()
entry.pack()
label2.pack()
entry2.pack()





#CTk mainloop
app.mainloop()
