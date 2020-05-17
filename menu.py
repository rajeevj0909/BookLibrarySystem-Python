'''RUN ON Windows with 100% on Scale and Layout settings
Welcome to my coursework
The beginning of the program is towards the
bottom where the main menu is created.'''

from booksearch import *
from bookcheckout import *
from bookreturn import *
from booklist import *
from tkinter import *
import tkinter
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Runs when exit button clicked at any instance
def exit_window():
    window.destroy()

#Creates the homepage again
def go_home():
    welcome.pack()
    button1.pack(fill = "x")
    button2.pack(fill = "x")
    button3.pack(fill = "x")
    button4.pack(fill = "x")
    
#Removes home widgets
def leave_home():
    welcome.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()

#Book search window appears
def button1_booksearch():
    #Gets answer and displays it
    def get_answer(x):
        user_choice=choice.get()
        search_item=textBox.get("1.0","end-1c")
        #Function found in booksearch file
        answer_list=submit_button(search_item,user_choice)
        if len(answer_list)==1:
            return_message.configure(text=answer_list[0])
            return_message.pack()
        #If there is more than one answer, it displays a next button
        else:
            x=x+1
            if x==len(answer_list):
                x=0
            next_button=tkinter.Button(window, height=3, width=7,bg="blue4",
            fg = "white",font="Verdana 16 bold",text="Next",
            command=lambda: get_answer(x))
            next_button.place(x=1670, y=480)
            return_message.configure(text=answer_list[x])
            return_message.pack()
        #This line is ran when the back button is clicked.
        if x==(-2):
            #The below line does not work for some reason!
            next_button.place_forget()

    #Deletes all the current widgets and loads the home menu
    def back(back_button,search_title,textBox,submit,return_message,option_menu,
         welcome,button1,button2,button3,button4):
        get_answer(-3)
        back_button.place_forget()
        search_title.pack_forget()
        textBox.pack_forget()
        submit.pack_forget()
        return_message.pack_forget()
        option_menu.place_forget()
        #Creates the homepage
        go_home()

    #Deletes the home page
    leave_home()
    
    #Loads the search page (creates and makes widgets appear)
    back_button=tkinter.Button(window, height=3, width=7,bg="blue4",
            fg = "white",font="Verdana 16 bold",text="Back",
            command=lambda: back(back_button, search_title,textBox,submit,
            return_message,option_menu,welcome,button1,button2,button3,button4))
    search_title=tkinter.Label(window,fg = "blue4",bg="white",
            font="Verdana 33 bold", text="  What do you want to search by \n and enter the search term you are looking for: \n ")
    textBox=tkinter.Text(window,bg="lightblue",font="Verdana 22 bold",
            height=3, width=50)
    submit=tkinter.Button(window, height=4, width=20,bg="blue4",fg = "white",
            font="Verdana 22 bold", text="Search",  command=lambda:get_answer(-1))
    return_message=tkinter.Label(window,text="",width=80,bg="white",fg = "blue4",
            font="Verdana 30 bold")
    choice=StringVar(window)
    choice.set("Title")
    option_menu=OptionMenu(window, choice,"Book ID","Title","Author","Purchase Date","Member ID")
    option_menu.config(width=20,bg="blue4",fg = "white", font="Verdana 20 bold")

    back_button.place(x=1810, y=0)
    search_title.pack()
    textBox.pack()
    submit.pack()
    option_menu.place(x=0, y=400)

#Book checkout window appears   
def button2_bookcheckout():
    #Gets answer and displays it
    def get_answer():
        search_book_id=textBox1.get("1.0","end-1c")
        search_member_id=textBox2.get("1.0","end-1c")
        #Function found in bookcheckout file
        answer=availability(search_book_id,search_member_id)
        return_message.configure(text=answer)
        return_message.pack()

    #Deletes all the current widgets and loads the home menu
    def back(back_button, search_title_book,search_title_member,textBox1,textBox2,submit,
            return_message,welcome,button1,button2,button3,button4):
        back_button.place_forget()
        search_title_book.pack_forget()
        search_title_member.pack_forget()
        textBox1.pack_forget()
        textBox2.pack_forget()
        submit.pack_forget()
        return_message.pack_forget()
        #Creates the homepage
        go_home()

    #Deletes the home page
    leave_home()
    
    #Loads the checkout page (creates and makes widgets appear)
    back_button=tkinter.Button(window, height=3, width=7,bg="blue4",
            fg = "white",font="Verdana 16 bold",text="Back",
            command=lambda: back(back_button, search_title_book,search_title_member,textBox1,textBox2,submit,
            return_message,welcome,button1,button2,button3,button4))
    search_title_book=tkinter.Label(window,fg = "blue4",bg="white",
            font="Verdana 33 bold", text="  What is the ID of the book that you want to check out?\n ")
    search_title_member=tkinter.Label(window,fg = "blue4",bg="white",
            font="Verdana 33 bold", text="  What is the ID of the member that you want to check out?\n ")
    textBox1=tkinter.Text(window,bg="lightblue",font="Verdana 22 bold",
            height=3, width=50)
    textBox2=tkinter.Text(window,bg="lightblue",font="Verdana 22 bold",
            height=3, width=50)
    submit=tkinter.Button(window, height=4, width=20,bg="blue4",fg = "white",
            font="Verdana 22 bold", text="Search",  command=lambda:get_answer())
    return_message=tkinter.Label(window,text="",width=80,bg="white",fg = "blue4",
            font="Verdana 70 bold")

    back_button.place(x=1810, y=0)
    search_title_book.pack()
    textBox1.pack()
    search_title_member.pack()
    textBox2.pack()
    submit.pack()

#Book return window appears
def button3_bookreturn():
    #Gets answer and displays it
    def get_answer():
        book_id=textBox.get("1.0","end-1c")
        #Function found in bookreturn file
        answer=return_book(book_id)
        return_message.configure(text=answer)
        return_message.pack()

    #Deletes all the current widgets and loads the home menu
    def back(back_button,search_title,textBox,submit,return_message,
         welcome,button1,button2,button3,button4):
        back_button.place_forget()
        search_title.pack_forget()
        textBox.pack_forget()
        submit.pack_forget()
        return_message.pack_forget()
        #Creates the homepage
        go_home()

    #Deletes the home page
    leave_home()

    #Loads the return page (creates and makes widgets appear)
    back_button=tkinter.Button(window, height=3, width=7,bg="blue4",
            fg = "white",font="Verdana 16 bold",text="Back",
            command=lambda: back(back_button, search_title,textBox,submit,
            return_message,welcome,button1,button2,button3,button4))
    search_title=tkinter.Label(window,fg = "blue4",bg="white",
            font="Verdana 33 bold", text=("What is the ID of the book that you want to return?\n \n "))
    textBox=tkinter.Text(window,bg="lightblue",font="Verdana 22 bold",
            height=3, width=50)
    submit=tkinter.Button(window, height=4, width=20,bg="blue4",fg = "white",
            font="Verdana 22 bold", text="Search",  command=lambda:get_answer())
    return_message=tkinter.Label(window,text="",width=80,bg="white",fg = "blue4",
            font="Verdana 80 bold")

    back_button.place(x=1810, y=0)
    search_title.pack()
    textBox.pack()
    submit.pack()

#Book return window appears
def button4_booklist():
    #Function found in booklist file
    results=list_books()
    titles_list=results[0]
    popularity_list=results[1]

    #Deletes all the current widgets and loads the home menu
    def back(back_button,bar1,welcome,button1,button2,button3,button4):
        back_button.place_forget()
        bar1.get_tk_widget().pack_forget()
        #Creates the homepage
        go_home()

    #Deletes the home page
    leave_home()

    #Loads the back button
    back_button=tkinter.Button(window, height=3, width=7,bg="blue4",
            fg = "white",font="Verdana 16 bold",text="Back",
            command=lambda: back(back_button,bar1,welcome,button1,button2,button3,button4))

    back_button.place(x=1810, y=0)

    #This is ran when there is mouse movement
    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            for bar in bars:
                cont, ind = bar.contains(event)
                if cont:
                    x = bar.get_x()+bar.get_width()
                    y = bar.get_y()+bar.get_height()
                    annot.xy = (x,y)
                    text=""
                    '''I have calculated the width of each bar and
                    managed to match that with the book title
                    allowing me to match each bar with the book
                    information'''
                    for i in range (len(titles_list)+1):
                        if y<i and i<(y+1):
                            title = titles_list[i-1]
                    '''This takes all the summary information
                    shown in the bubbles. The function for this is in
                    book_list'''
                    text=title_search(title)
                    annot.set_text(text)
                    annot.get_bbox_patch().set_alpha(0.4)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    #This is used to embed the graph into tkinter
    fig=plt.figure()
    ax=plt.subplot()
    bars = plt.barh(titles_list,popularity_list,color='#00008B')
    plt.title("Popularity")
    plt.xlabel("Times taken out")
    plt.ylabel("Books")
    annot = ax.annotate("", xy=(0,0), xytext=(20,30),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="#00008B", ec="b", lw=2),
                        arrowprops=dict(arrowstyle="->"))
    #These draw the graph onto the window like a normal widget
    bar1 = FigureCanvasTkAgg(fig, window)
    bar1.get_tk_widget().pack(expand=True,fill=tkinter.BOTH)
    annot.set_visible(False)
    #Runs when there is mouse movement
    hovering= fig.canvas.mpl_connect("motion_notify_event", hover)
    

#Start of program!
    
#Creates the window
window=tkinter.Tk()
window.title("Library System")
window.configure(background="white")
#Makes it always fullscreen
window.attributes('-fullscreen', True)

top_frame = tkinter.Frame(window).pack()
title=tkinter.Label(window, text="  --- R A J E E V' S   L I B R A R Y  --- \n",
                    fg = "blue4",bg="white",font="Verdana 60 bold")
welcome=tkinter.Label(window, text="  WELCOME \n ",fg = "blue4",bg="white",
                    font="Verdana 45 bold")
height_y=1
font_type="Verdana 55 bold"
#Creates all the home widgets
button1=tkinter.Button(top_frame, text = "SEARCH for books",command=lambda:button1_booksearch(),
               fg = "blue4",height=height_y,font=font_type)
button2=tkinter.Button(top_frame, text = "CHECK out books",command=lambda:button2_bookcheckout(),
               fg = "blue4",height=height_y,font=font_type)
button3=tkinter.Button(top_frame, text = "RETURN books",command=lambda:button3_bookreturn(),
               fg = "blue4",height=height_y,font=font_type)
button4=tkinter.Button(top_frame, text = "Look at book POPULARITY",command=lambda:button4_booklist(),
               fg = "blue4",height=height_y,font=font_type)
exit1=tkinter.Button(window, height=3, width=7,bg="blue4",fg = "white",font="Verdana 16 bold",
                                text="Exit",  command=lambda: exit_window())
#Draws on all the widgets to the window
title.pack()
exit1.place(x=0, y=0)
welcome.pack()
button1.pack(fill = "x")
button2.pack(fill = "x")
button3.pack(fill = "x")
button4.pack(fill = "x")

#Runs the window!
window.mainloop()
