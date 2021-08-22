import pyttsx3

high_score = 50.0
score=0

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3')
engine.setProperty('rate', 150)

def highscoreAchieved():
    high_score = score
    print ("Your score is:",score,"\nThe high score is: ",high_score)
    engine.say("Congragulations, It's a high score")
    engine.say("Your score is: ",score)
    engine.runAndWait()

def notHighscore():
    print ("Your score is:",score,"\nThe high score is: ",high_score)
    engine.say("Better luck next time..")
    engine.say("Your score is: ",score)
    engine.runAndWait()

arduino_input = int(input())
Distance = float(input())
score = round(Distance,2)

while arduino_input == 1:

    if score >= high_score:
	    highscoreAchieved()
    elif score < high_score:
	    notHighscore()

    arduino_input = int(input())
    Distance = float(input())
    score = round(Distance,2)

