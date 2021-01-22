# install chatterbot lib.
# then we import chatbot class from chatterbot module
# and now we will create a new chatbot
# so take a var(bot) and put class(chatbot)in it and make class object and pass constructor here(constructor)
# ----- we must create a set(no duplicacy) of conversation / and put this set of conversation in a DATABASE / and give refrence of this set to listtrainer() to fetch data from database
# for this we can use SQLITE DATABASE for conversation
# we can ADAPTOR to TRAIN
# install lib. pyttsx3 for audio msgs

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *
import pyttsx3 as pp

import speech_recognition as s  # for spech recognise #taking query
# threading(a module)for calling takequery func we created a thread
import threading

engine = pp.init()  # initializing pp and it returne a module named engine
voices = engine.getProperty('voices')  # it will take all male / female voices
engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)  # using say func
    engine.runAndWait()  # runandwait method using


# now create object of chatbot class: -
robot = ChatBot("write anything here like-my Bot")

list = [
    'hello',
    'hi',
    'how are you',
    'fine',
    'what is your name',
    'my name is bot',
    'where you live',
    'i live in india',
    'which language you speak',
    'mostly i speak english'

]

# now create an object of listtrainer
trainer = ListTrainer(robot)

# now train the bot with help of trainer # trainer help our robot to learn all conversation
trainer.train(list)

#answer = robot.get_response("hello")
# print(answer)


# print('talk: ')
# while True:
#     query = input()
#     if query == "exit":
#         break
#     ans = robot.get_response(query)
#     print('bot:', ans)


window = Tk()
window.geometry('500x450')  # width x height x=x not *
window.title('my chatbot')


# now taking audio as input and convert it into string and give that string to our robot to print
# so now create a fun.
def takequery():
    sr = s.Recognizer()
    # this line is not imp. # read documentation and understand threshold
    sr.pause_threshold = 1
    print('bot is listening so speak .........')
    with s.Microphone() as m:
        audio = sr.listen(m)
        text = sr.recognize_google(audio, language='eng-in')
        print(text)
        textF.delete(0, END)
        textF.insert(0, text)
        ask()


def ask():
    question = textF.get()
    answer = robot.get_response(question)
    msg.insert(END, 'you: ' + question)
    msg.insert(END, 'robot: ' + str(answer))
    speak(answer)  # here our speaker becomes active//calling speak func
    textF.delete(0, END)  # deleting text field automatically
    msg.yview(END)  # automatically shows us end msg

    #img = PhotoImage(file=r'C:\Users\RIG1\Desktop\robot.png')
    #photoL = Label(window, Image=img)
    # photoL.pack(pady=5)


frame = Frame(window)

sc = Scrollbar(frame)


# create object of  a list box
# (yscrollcommand=scrol.set= just to active our scroll bar)
# yscrollcommand is an attribute
msg = Listbox(frame, width=60, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=20)
frame.pack()
# now creating text field
textF = Entry(window)
textF.pack(fill=X, pady=10)
# creating button
btn = Button(window, text='ask', command=ask)
btn.pack()

# creating a function for enter:-


def enter(event):  # write event(an object) is important
    btn.invoke()


# now bind(joint) main window with enter key
# (here binding RETURN means ENTER with our window) AND (giving refrence of ENTER function not calling enter)
window.bind('<Return>', enter)


def repeatListen():  # for taking audio againand agin from user
    while True:
        takequery()  # our function name


# takequery()  # for calling takequery function here we create a THREAD
# not using() to call func.just giving name/reference of func with its name
t = threading.Thread(target=repeatListen)  # repeat - our function
t.start()  # so now our thread is staring with calling takequery func.


window.mainloop()
