import csv
import pyttsx3
import random


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3')

fields=[]
rows=[]

with open('dataset.csv','r') as csvfile:
    csvreader= csv.reader(csvfile)
    fileds=next(csvreader)

    for row in csvreader:
        rows.append(row)
    
    n=csvreader.line_num
    i=random.randint(0,n-1)

for row in rows[i:i+1]:
    for col in row:
        print("%10s"%col)
        engine.say(col)
        engine.runAndWait()
        break
