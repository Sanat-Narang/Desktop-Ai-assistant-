from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action
root = Tk()
root.title("Ai Assistant")
root.geometry("550x670")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # background color
 # ask fun
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, "Me --> "+user_val+"\n")
    if bot_val != None:
            text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()


# send fun
def send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  
#delete fun
def del_text():
   text.delete("1.0", "end")

#frame
frame = LabelFrame(root, padx = 100 , pady = 7, borderwidth = 3, relief = "raised")
frame.configure(bg = "#1e1e1e")  # background color
frame.grid(row = 0, column = 1, padx = 55, pady = 10)

# text lable

text_label = Label(frame, text = "AI assistant", font = ("Arial", 20, "bold"), bg = "#e7d9d9")
text_label.grid(row = 0, column = 0, padx = 20, pady = 10)

#image
image = ImageTk.PhotoImage(Image.open("image/assistant.png.jpeg"))
image_label = Label(frame, image = image)
image_label.grid(row = 1, column = 0, pady = 20)

#adding text widget 1 box

text=Text(root , font= ('Courier 10 bold') , bg = "#E3E4E6")
text.grid(row = 2,  column= 0)
text.place(x= 70, y= 375, width= 375, height= 100) 

# entry widget
entry1 = Entry(root, justify = CENTER)
entry1.place(x=70, y= 500, width= 375, height= 30)

#button 1 
button1 = Button(root, text = "Ask", bg = "#24C0CB", pady = 16,padx = 40, borderwidth = 3, relief = SOLID, command = ask)
button1.place(x = 70, y = 575)
#button 2
button2 = Button(root, text = "Send", bg = "#24C0CB", pady = 16,padx = 40, borderwidth = 3, relief = SOLID, command = send)
button2.place(x = 400, y = 575)
#button 3
button3 = Button(root, text = "Delete", bg = "#24C0CB", pady = 16,padx = 40, borderwidth = 3, relief = SOLID,command = del_text)
button3.place(x = 225, y = 575)
root.mainloop()