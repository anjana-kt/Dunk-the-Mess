# Dunk-the-Mess
Make a trash bin to "smart bin"

## Inspiration

Initially , we were quite uncertain about what to develop that replicated the fun elements of basketball.
Later, we thought to ourselves why not associate the fun of basketball for the greater good of the planet.<br>
The massive amount of litter produced everyday in public places , it's subsequent consequences as well as the lack of effort from each of us inspired us to  create **Dunk the mess**, that encourages people to dispose their litter more efficiently by making the process enjoyable and rewarding.
<br>
![problem](https://img.resized.co/newstalk/eyJkYXRhIjoie1widXJsXCI6XCJodHRwczpcXFwvXFxcL21lZGlhLnJhZGlvY21zLm5ldFxcXC91cGxvYWRzXFxcLzIwMjFcXFwvMDRcXFwvMTkxNTE1MjVcXFwvOTAzNzU2ODYuanBnXCIsXCJ3aWR0aFwiOjEyMDAsXCJoZWlnaHRcIjo5MDAsXCJkZWZhdWx0XCI6XCJodHRwczpcXFwvXFxcL3d3dy5uZXdzdGFsay5jb21cXFwvaW1hZ2VzXFxcL2RlZmF1bHRfbm9faW1hZ2UucG5nXCJ9IiwiaGFzaCI6IjY1YTQyY2UzMzM1MTdlNjU1YjkzYTJiYWQ3YjE1ZTZjYjMxODYwZTUifQ==/90375686.jpg)
## What it does??

**Dunk the Mess** is a low cost device that can be used to upgrade a garbage bin. <br> It can be  easily attached on top of a normal bin to upgrade it into a smart bin.
- **Slam dunk** :-People can try to toss the litter through the hoop of bin from a distance just like the game of basketball. The camera will detect the distance from where the litter/plastic bottle is tossed and it'll announce your score through the speakers. 
- **Overflow alert** :-It automatically detects when the bin is full and alerts the concerned people, so that they can empty the bin at correct intervals.
- **Talking bin** :-When a trash falls into the bin it's understood that someone in person is near the bin, so at this time the device speaks about the common concerns of people related to covid.<br><br>
Altogether, it helps to keep our environment clean by attracting people to make an effort to come near the bin and trash properly by engaging them with fun and enjoyable activities in an economical way.

## How we built it?!
It basically consists of a  camera, ultrasonic sensor and a speaker, these are integrated using raspberry pi. 
- The scores are calculated on the basis of distance from the bin at the time of throw. This is implemented by object detection using python and opencv.
- Text to speech libraries were used and connected to the speaker to enhance the device with voice actions
- The ultrasonic sensors detect whether the litter has fallen correctly or not and also detects if the bin becomes full and sent alerts notifications.
- The covid 19 facts and dataset was collected from kaggle.

## Demo video
  - [Dunk the Mess video](https://)

## What we learned..
We got to learn so much in this limited time and really pushed ourselves further .We got a chance to learn and grow together. 
We learned jina, how to automate the components like camera, sensors etc using raspberry pi and python, object detectiona nad face detection using opencv and machine learning 

## What's next?
Next up, we have to learn more about automation and jina to make the bin more interactive and act as a chatbot which talks with the power of AI . We have to improve the design of our bin and make if more cost effective.

## Authors

- **Fida Fathima**  - [fida](https://github.com/Fida123789)
- **Aadhya K Raj**  - [aayahda](https://github.com/aayahda)
- **Anjana K T**  - [anjana-kt](https://github.com/anjana-kt)
