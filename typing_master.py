from tkinter import *
import random
from tkinter import ttk
from time import sleep
import threading

root = Tk()
# root.get_themes()
# root.set_theme('radiance')
root.geometry("940x735+200+10")
root.resizable(False,False)
root.overrideredirect(True)
root.config(bg='Blue')

#! functionality part 
total_time =60
time = 0
wrongwords = 0
elapsedtimeinminute = 0

def start_timer():
    start_button.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()
    for time in range(1,61):
        elapsed_timer_label.config(text=time)
        remaining_time = total_time-time
        Remaining_timer_label.config(text=remaining_time)

        sleep(1)
        root.update()
    textarea.config(state=DISABLED)
    reset_button.config(state=NORMAL)

def count():
    global wrongwords
    while time!=total_time:
        entered_paragraph= textarea.get(1.0,END).split()
        total_words = len(entered_paragraph)
    
    total_words_count_label.config(text=total_words)

    para_word_list = pargarph_label['text'].split()

    for pair in zip(para_word_list,entered_paragraph):
        if pair[0]!=pair[1]:
            wrongwords+=1
    
    Wrong_word_count_label.config(text=wrongwords)

    elapsedtimeinminute = time/60
    wpm = (total_words - wrongwords)/elapsedtimeinminute
    wpm_count_label.config(text=wpm)
    gross_wpm = total_words/elapsedtimeinminute
    accuracy  = wpm/gross_wpm*100
    accuracy = round(accuracy)
    acurracy_count_label.config(text=str(accuracy)+"%")

def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()

def reset1():
    global time,elapsedtimeinminute
    time = 0
    elapsedtimeinminute = 0
    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    Remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    acurracy_count_label.config(text='0')
    total_words_count_label.config(text='0')
    Wrong_word_count_label.config(text='0')
    



# change the color of button when tpe on button from keyboard
def changeBg(widget):
    widget.config(bg="blue")
    widget.after(100,lambda :widget.config(bg="black"))




mainframe = Frame(root,bd=4)
mainframe.grid()

title_frame = Frame(mainframe,bg="orange")
title_frame.grid(row=0,column=0)

title_label = Label(title_frame,text="MASTER TYPING BY AJHAR",font=("algerian",28,"bold"),fg='white',bg="goldenrod3",width=38,bd=10)
title_label.grid(pady=5)

paragrapgh_frame = Frame(mainframe)
paragrapgh_frame.grid(row=1,column=0)

paragraph_list = [' I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” ',

                    ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

                    'I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyonce while I was in the background with a can of tuna.This is what happened in this short funny story if you like.',

                    'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

                    'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',
                    'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',
                    'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

                    'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.'
]
random.shuffle(paragraph_list)

pargarph_label = Label(paragrapgh_frame,text=paragraph_list[0],wraplength=912,justify=LEFT,font=('arial',14,'bold'))
pargarph_label.grid(row=0,column=0)

textarea_frame = Frame(mainframe)
textarea_frame.grid(row=2,column=0)

textarea = Text(textarea_frame,font=('arial',12,'bold'),width=100,height=7,bd=4,relief=GROOVE,wrap='word',state=DISABLED)
textarea.grid()

frame_output = Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time_label = Label(frame_output,text="Elapsed Time",font=('Tohoma',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label = Label(frame_output,text="0",font=('Tohoma',12,'bold'))
elapsed_timer_label.grid(row=0,column=1,padx=5)

Remaining_time_label = Label(frame_output,text="Remaining Time",font=('Tohoma',12,'bold'),fg='red')
Remaining_time_label.grid(row=0,column=2,padx=5)
Remaining_timer_label = Label(frame_output,text="60",font=('Tohoma',12,'bold'))
Remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_label = Label(frame_output,text="WPM",font=('Tohoma',12,'bold'),fg='red')
wpm_label.grid(row=0,column=4,padx=5)
wpm_count_label = Label(frame_output,text="0",font=('Tohoma',12,'bold'))
wpm_count_label.grid(row=0,column=5,padx=5)

acurracy_label = Label(frame_output,text="Accuracy",font=('Tohoma',12,'bold'),fg='red')
acurracy_label.grid(row=0,column=6,padx=5)
acurracy_count_label =Label(frame_output,text='0',font=('arial',12,'bold'))
acurracy_count_label.grid(row=0,column=7,padx=5)

total_words_label = Label(frame_output,text="Total Words",font=('Tohoma',12,'bold'),fg='red')
total_words_label.grid(row=0,column=8,padx=5)

total_words_count_label = Label(frame_output,text="0",font=('Tohoma',12,'bold'))
total_words_count_label.grid(row=0,column=9,padx=5)

Wrong_word_label = Label(frame_output,text="Wrong Words",font=('Tohoma',12,'bold'),fg='red')
Wrong_word_label.grid(row=0,column=10,padx=5)
Wrong_word_count_label =Label(frame_output,text="0",font=('Tohoma',12,'bold'))
Wrong_word_count_label.grid(row=0,column=11,padx=5)

button_frame = Frame(mainframe)
button_frame.grid(row = 4,column=0)

start_button =Button(button_frame,text="Start",font=('arial',10,'bold'),width=10,fg='black',bg='pink',bd=3,relief=GROOVE,command=start)
start_button.grid(row=0,column=0,padx=5)

reset_button = Button(button_frame,text="Reset",font=('arial',10,'bold'),width=10,fg='black',bg='pink',bd=3,relief=GROOVE,state=DISABLED,command=reset1)
reset_button.grid(row=0,column=1,padx=5)

exit_button = Button(button_frame,text="Exit",font=('arial',10,'bold'),width=10,fg='black',bg='pink',bd=3,relief=GROOVE,command=root.destroy)
exit_button.grid(row=0,column=2,padx=5)

keyboard_frame = Frame(mainframe)
keyboard_frame.grid(row=5,column=0)

from1to0 = Frame(keyboard_frame)
from1to0.grid(row=0,column=0,pady=3)

label1 = Label(from1to0,text='1',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label2 = Label(from1to0,text='2',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label3 = Label(from1to0,text='3',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label4 = Label(from1to0,text='4',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label5 = Label(from1to0,text='5',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label6 = Label(from1to0,text='6',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label7 = Label(from1to0,text='7',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label8 = Label(from1to0,text='8',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label9 = Label(from1to0,text='9',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label0 = Label(from1to0,text='0',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)

label1.grid(row=0,column=0,padx=5)
label2.grid(row=0,column=1,padx=5)
label3.grid(row=0,column=2,padx=5)
label4.grid(row=0,column=3,padx=5)
label5.grid(row=0,column=4,padx=5)
label6.grid(row=0,column=5,padx=5)
label7.grid(row=0,column=6,padx=5)
label8.grid(row=0,column=7,padx=5)
label9.grid(row=0,column=8,padx=5)
label0.grid(row=0,column=9,padx=5)

from_q_to_q = Frame(keyboard_frame)
from_q_to_q.grid(row=1,column=0,pady=3)

label_Q = Label(from_q_to_q,text='Q',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_W = Label(from_q_to_q,text='W',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_E = Label(from_q_to_q,text='E',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_R = Label(from_q_to_q,text='R',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_T = Label(from_q_to_q,text='T',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_Y = Label(from_q_to_q,text='Y',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_U = Label(from_q_to_q,text='U',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_I= Label(from_q_to_q,text='I',fg='white',bg='black',font=
('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_O = Label(from_q_to_q,text='O',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_P = Label(from_q_to_q,text='P',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)

label_Q.grid(row=0,column=0,padx=5)
label_W.grid(row=0,column=1,padx=5)
label_E.grid(row=0,column=2,padx=5)
label_R.grid(row=0,column=3,padx=5)
label_T.grid(row=0,column=4,padx=5)
label_Y.grid(row=0,column=5,padx=5)
label_U.grid(row=0,column=6,padx=5)
label_I.grid(row=0,column=7,padx=5)
label_O.grid(row=0,column=8,padx=5)
label_P.grid(row=0,column=9,padx=5)

from_a_to_l = Frame(keyboard_frame)
from_a_to_l.grid(row=2,column=0,pady=3)

label_A = Label(from_a_to_l,text='A',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_S = Label(from_a_to_l,text='S',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_D = Label(from_a_to_l,text='D',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_F = Label(from_a_to_l,text='F',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_G = Label(from_a_to_l,text='G',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_H = Label(from_a_to_l,text='H',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_J = Label(from_a_to_l,text='J',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_K = Label(from_a_to_l,text='K',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_L = Label(from_a_to_l,text='L',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)

label_A.grid(row=0,column=0,padx=5)
label_S.grid(row=0,column=1,padx=5)
label_D.grid(row=0,column=2,padx=5)
label_F.grid(row=0,column=3,padx=5)
label_G.grid(row=0,column=4,padx=5)
label_H.grid(row=0,column=5,padx=5)
label_J.grid(row=0,column=6,padx=5)
label_K.grid(row=0,column=7,padx=5)
label_L.grid(row=0,column=8,padx=5)

from_z_to_m = Frame(keyboard_frame)
from_z_to_m.grid(row=3,column=0,pady=3)

label_Z = Label(from_z_to_m,text='Z',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_X = Label(from_z_to_m,text='X',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_C = Label(from_z_to_m,text='C',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_V = Label(from_z_to_m,text='V',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_B = Label(from_z_to_m,text='B',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_N = Label(from_z_to_m,text='N',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)
label_M = Label(from_z_to_m,text='M',fg='white',bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=5,height=2)

label_Z.grid(row=0,column=0,padx=5)
label_X.grid(row=0,column=1,padx=5)
label_C.grid(row=0,column=2,padx=5)
label_V.grid(row=0,column=3,padx=5)
label_B.grid(row=0,column=4,padx=5)
label_N.grid(row=0,column=5,padx=5)
label_M.grid(row=0,column=6,padx=5)

space_frame = Frame(keyboard_frame)
space_frame.grid(row=4,column=0,pady=3)

space_label_1 = Label(space_frame,bg='black',font=('arial',10,'bold'),relief=GROOVE,bd=10,width=40,height=2)
space_label_1.grid(row=0,column=0)

label_numbers = [label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]

label_alphabets = [label_A,label_B,label_C,label_D,label_E,label_F,label_G,label_H,label_I,label_J,label_K,label_L,label_M,label_N,label_O,label_P,label_Q,label_R,label_S,label_T,label_U,label_V,label_W,label_X,label_Y,label_Z]

space_label = [space_label_1]

binding_numbers = ['1','2','3','4','5','6','7','8','9','0']

binding_capital_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

binding_small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for number in range(len(binding_numbers)):
    # print(binding_numbers[number])
    root.bind(binding_numbers[number],lambda event,label=label_numbers[number]:changeBg(label))


for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets],lambda event,label = label_alphabets[capital_alphabets]:changeBg(label))


for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets],lambda event, label=label_alphabets[small_alphabets]:changeBg(label))

root.bind('<space>',lambda event:changeBg(space_label[0]))

root.mainloop()