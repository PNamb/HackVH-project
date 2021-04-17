import tkinter as tk
import tkinter.font as tkFont
import time

win = tk.Tk()
font_1 = tkFont.Font(family = "Helvitaca", size = "9")
##############################################################################################################################################
#mental health button
mental = tk.Button(win, text = "Mental Health Tips", font = font_1, fg = "white", bg = "purple", height = 2, width = 16, cursor = "hand2")
mental.pack()
def mental_entered(event):
    mental.config(font = "TkDefaultFont 9 underline")
mental.bind("<Enter>", mental_entered)
def mental_left(event):
    mental.config(font = "TkDefaultFont 9")
mental.bind("<Leave>", mental_left)
##############################################################################################################################################
#physical health button
physical = tk.Button(win, text = "Physical Health Tips", font = font_1, fg = "black", bg = "green", height = 2, width = 16, cursor = "hand2")
physical.pack()
def physical_entered(event):
    physical.config(font = "TkDefaultFont 9 underline")
physical.bind("<Enter>", physical_entered)
def physical_left(event):
    physical.config(font = "TkDefaultFont 9")
physical.bind("<Leave>", physical_left)
##############################################################################################################################################
##############################################################################################################################################
social_text, emotional_text, s_c, e_c = None, None, None, None

def social_m_clicked(event):
    global social_text, emotional_text, s_c, e_c
    social_text.place(x = 90, y = -56)
    emotional_text.place_forget()
    s_c = True
    e_c = False
    if s_c == False:
        social_text.place_forget()

def emotional_m_clicked(event):
    global social_text, emotional_text, s_c, e_c
    emotional_text.place(x = 90, y = -56)
    social_text.place_forget()
    e_c = True
    s_c = False
    if e_c == False:
        emotional_text.place_forget()

def mental_clicked(event):
    global social_text, emotional_text, s_c, e_c
    mental.pack_forget()
    physical.pack_forget()

    s_c = False
    e_c = False
    
    frame1 = tk.Frame(win, width = 460, height = 400)
    frame1.pack()

    e_m = tk.Label(frame1, text = "During this \n pandemic, \n mental health \n is more \n important than \n ever, and \n these tips can \n help with \n elevating it.", font = font_1, bg = "purple", fg = "gray", width = 12, height = 20)
    e_m.place(x = 0, y = 106)
    
    social_m = tk.Button(frame1, text = "Social Tips", font = font_1, bg = "blue", fg = "white", height = 2, width = 11, cursor = "hand2")
    social_m.place(x = 0, y = 25)

    social_text = tk.Label(frame1, cursor = "ibeam", text = "- Connect with others \n Personal connections can contribute to an overall \n happier life, in both the short and long term. \n \n - Join a community group \n If you prefer to keep things low key, but still want to \n engage with others, a group might be right for you, however due \n to covid-19 many community groups are meeting virtually. \n \n - Hone your communication skills \n You may not be able to talk to your freinds all the time, but that \n doesn't mean you should let your communication skills sink down. \n Good communication skills is the backbone of a good relationship. \n Here are some ways you can work on them: \n • Mantain eye contact when you're talking with \n someone, even if it's on a video call. \n • Give the other person plenty of time to talk, \n and listen well when they do. \n • Pay attention to your body language. For example, \n don't rest your head on your hand, which can look like you're \n not paying attention to what the other person is saying.", bg = "blue", fg = "white", height = 30, width = 52, font = font_1, relief = "ridge")
    
    emotional_m = tk.Button(frame1, text = "Emotional Tips", font = font_1, bg = "red", height = 2, width = 11, cursor = "hand2")
    emotional_m.place(x = 0, y = 65)

    emotional_text = tk.Label(frame1, cursor = "ibeam", text = "- Meditate \n Meditation calms the mind and soul, making you more content \n with your surrondings. Meditation also reduces: \n • Stress \n • Pain \n • Anxiety \n •Depression \n \n - Practice Graititude \n Self esteem and optimism are powerful healers. Expressing love \n and other emotions can help bring balance in the face of \n challenges. \n \n - Expand your circle of friends \n Friends are a great support system and can serve as a shoulder \n to lean on in trying times. Expanding your circle of friends can \n increase the number of people you have that can cheer you up \n when you're down. \n \n - Develop a passion \n You should do something that makes you happy. Doesn't matter \n what it is, as long as that hobby makes you happy.", bg = "red", fg = "black", height = 30, width = 52, font = font_1, relief = "ridge")

    social_m.bind("<Button-1>", social_m_clicked)
    emotional_m.bind("<Button-1>", emotional_m_clicked)
    
    #back_1 clicked
    back_1 = tk.Button(frame1, text = "←", fg = "black", bg = "light blue", width = 5, height = 1, cursor = "hand2")
    back_1.place(x = 0, y = 0)

    def back_1_clicked(event): #EXP clicked
        frame1.pack_forget()
        mental.pack()
        physical.pack()
        
    back_1.bind("<Button-1>", back_1_clicked)
mental.bind("<Button-1>", mental_clicked)
##############################################################################################################################################
##############################################################################################################################################
pe_text, right, left, stop_text, start_b, stop_b, timer_t, stop_1 = None, None, None, None, None, None, None, None

def right_clicked(event):
    global pe_text, right, left, stop_text, start_b, stop_b, timer_t, stop_1
    pe_text.place_forget()
    right.place_forget()
    left.place(x = 19, y = 30)
    stop_text.place(x = 19, y = 30)
    start_b.place(x = 19, y = 313)
    #stop_b.place(x = 335, y = 313)

def left_clicked(event):
    global pe_text, right, left, stop_text, start_b, stop_b, timer_t, stop_1
    right.place(x = 394, y = 30)
    pe_text.place(x = 20, y = 30)
    left.place_forget()
    stop_text.place_forget()
    start_b.place_forget()
    stop_b.place_forget()
    stop_1 = True

def start_clicked(event):
    global pe_text, right, left, stop_text, start_b, stop_b, timer_t, stop_1
    start_b.place_forget()
    stop_b.place(x = 335, y = 313)
    stop_1 = False
    while True:
        time.sleep(0.1)
        timer_t += 0.1
        timer_t_a = round(timer_t, 2)
        #print(timer_t_a)
        a_ti = timer_t_a
        h_ti = int(a_ti/3600)
        a_ti = a_ti % 3600
        m_ti = int(a_ti/60)
        a_ti = a_ti % 60
        s_ti = a_ti
        stop_text.config(text = ("%02d:%02d:%02d" % (h_ti ,m_ti ,s_ti)))
        win.update()
        if stop_1:
            break
        else:
            continue

def stop_clicked(event):
    global pe_text, right, left, stop_text, start_b, stop_b, timer_t, stop_1
    stop_b.place_forget()
    start_b.place(x = 19, y = 313)
    stop_1 = True
        

def physical_clicked(event):
    global pe_text, right, left, stop_text, start_b, stop_b, timer_t, stop_1
    mental.pack_forget()
    physical.pack_forget()
    
    stop_1 = False

    timer_t = 0.0
    
    frame2 = tk.Frame(win, width = 460, height = 400)
    frame2.pack()
    ##############################################################################################################################################
    pe_text = tk.Label(frame2, text = "- Mantain a healthy diet \n A healthy diet helps reduce the risk of physical \n probelms such as heart diseases and diabetes. \n \n - Drink lots of water \n Your body requires water to function, and drinking \n water can help soothe aches/pains plus improve your \n energy levels. \n \n - Wear comfortable shoes \n Wearing shoes that don't fit you properly can result \n in cramps, damage to your feet, and an overall more \n difficult time when exercising. \n \n - Take time to relax \n Pushing yourself too hard can compromise your body's \n ability to bounce back and can make you constantly feel \n achy and sore. \n \n - Do timed workouts \n When doing a tough workout, especially when working on \n building strength, your body needs down time to rest and rebuild. \n On the next page is a stopwatch to use for workouts.", font = font_1, bg = "orange", height = 24, width = 59, relief = "ridge", cursor = "ibeam")
    pe_text.place(x = 20, y = 30)

    stop_text = tk.Label(frame2, text = "00:00:00", font = ("Courier", 20), bg = "blue", fg = "white", height = 12, width = 26)
    ##############################################################################################################################################
    right = tk.Button(frame2, text = "❯", fg = "white", bg = "blue", width = 5, height = 1, cursor = "hand2")
    right.place(x = 394, y = 30)
    
    left = tk.Button(frame2, text = "❮", fg = "white", bg = "blue", width = 5, height = 1, cursor = "hand2")
    ##############################################################################################################################################
    start_b = tk.Button(frame2, text = "START", font = ("Courier", 20), fg = "white", bg = "blue", cursor = "hand2", width = 6, height = 2)

    stop_b = tk.Button(frame2, text = "STOP", font = ("Courier", 20), fg = "white", bg = "blue", cursor = "hand2", width = 6, height = 2)

    
    right.bind("<Button-1>", right_clicked)
    left.bind("<Button-1>", left_clicked)
    start_b.bind("<Button-1>", start_clicked)
    stop_b.bind("<Button-1>", stop_clicked)
    #back_2 clicked
    back_2 = tk.Button(frame2, text = "←", fg = "black", bg = "light blue", width = 5, height = 1, cursor = "hand2")
    back_2.place(x = 0, y = 0)

    def back_2_clicked(event): #EXP clicked
        frame2.pack_forget()
        mental.pack()
        physical.pack()
        
    back_2.bind("<Button-1>", back_2_clicked)

physical.bind("<Button-1>", physical_clicked)














    
