#   In order to make this application work, you MUST NEED to do these REQUIREMENTS below:
#       - Go to your terminal (or in Windows Powershell Administrator) and type "pip install groq" and "pip install pillow". Reboot your device once
#           it has been installed.

#   For OPTIONAL below:
#       - In case if the API Key expires, login to your account at "https://console.groq.com" and go to the API Keys section,
#           which is at "https://console.groq.com/keys". This is where you will get the API Key from Groq.
#       - Once you have retrieve the API Key, replace the old API Key in "api_key" variable with your new key.


#IMPORT MODULES
import os
from tkinter import *
from API_Function import chat_execute
from PIL import ImageTk
from PIL import Image


#GUI INITIALIZATION
window = Tk()
window.geometry("620x620")
window.resizable(False, False)


icon = PhotoImage(file='benilde_icon_1.png')
window.iconphoto(True, icon)
window.title("BenildeGPT")

window.config(background="#202024")


#GUI INITIALIZATION: ROWS AND COLUMNS
window.grid_columnconfigure(0, weight=1) 
window.grid_columnconfigure(1, weight=0) 
window.grid_rowconfigure(0, weight=1) 


#DECLARATIONS
PLACEHOLDER_TEXT = "Enter your message here"

MIN_LINES = 1


#LABELS AND PANELS INITIALIZATION
chat_history = Text(
    window, 
    height=20, 
    state=DISABLED,
    font=("Arial", 12),
    wrap=WORD,
    bd=0,
    relief="flat",
)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
)

Input_Text_Box = Text(
    window, 
    width=50, 
    height=MIN_LINES, 
    font=("Arial", 12),
    foreground="#ffffff",
    background="#36363d",
    wrap=WORD,
    bd=0,
)
Input_Text_Box.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")

icon = Image.open("benilde_icon_2.png")
resized_icon = icon.resize((50, 50), Image.Resampling.LANCZOS)
new_icon = ImageTk.PhotoImage(resized_icon)

window.new_icon = new_icon
bottom_frame = Frame(window, bg="#202024")
bottom_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")

icon_label = Label(bottom_frame, image=new_icon, bg="#202024")
icon_label.grid(row=0, column=0, sticky="w") 

Labeling = Label(
    window,
    text="BenildeGPT",
    foreground="#ffffff",
    background="#202024",
    font=("Arial", 25, "bold")
)
Labeling.grid(row=2, column=0, columnspan=2, padx=67, pady=10, sticky="w")


#COLOR TEXT INITIALIZATION
Input_Text_Box.tag_config(
    "placeholder_tag",
    foreground="#999494"
)

chat_history.tag_configure(
    "ai_name_tag",
    foreground="#3ea83d",
    font=("Arial", 12, "bold")
)
chat_history.tag_configure(
    "user_name_tag",
    font=("Arial", 12, "bold")
)


#FUNCTIONS: GATHERING AI RESPONSES
def update_chat_history(chunk):
    chat_history.config(state=NORMAL)
    chat_history.insert(END, chunk) 
    chat_history.config(state=DISABLED)
    chat_history.see(END) 

    window.update()


#FUNCTIONS: REQUESTING API TO SEND BACK HERE WITH AI RESPONSES
def message_sent(event):
    message_given = Input_Text_Box.get("1.0", "end-1c").strip()
    chat_history_given = chat_history.get("1.0", "end-1c").strip()
    placeholder_text = Input_Text_Box.get("1.0", "end-1c").strip()

    if message_given and not chat_history_given:
        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"{os.environ.get('USERNAME')}: ", "user_name_tag")
        chat_history.insert(END, f"\n\n")
        chat_history.insert(END, f"Benilde Chatbot: ", "ai_name_tag")

        chat_execute(message_given, update_chat_history)

        chat_history.config(state=DISABLED)

        Input_Text_Box.delete("1.0", END)

        if placeholder_text == PLACEHOLDER_TEXT:
            Input_Text_Box.delete("1.0", END)


    elif message_given and chat_history_given:
        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"\n\n\n{os.environ.get('USERNAME')}: ", "user_name_tag")
        chat_history.insert(END, f"\n\n")
        chat_history.insert(END, "Benilde Chatbot: ", "ai_name_tag")

        chat_execute(message_given, update_chat_history)

        chat_history.config(state=DISABLED)

        Input_Text_Box.delete("1.0", END)

        if placeholder_text == PLACEHOLDER_TEXT:
            Input_Text_Box.delete("1.0", END)

    return "break"


#FUNCTIONS: REMOVING PLACEHOLDERTEXT
def remove_placeholdertext(event):
    placeholder_text = Input_Text_Box.get("1.0", "end-1c").strip()

    if placeholder_text == PLACEHOLDER_TEXT:
        Input_Text_Box.delete("1.0", END)
        Input_Text_Box.unbind('<FocusIn>', remove_placeholdertext)


#FUNCTIONS: ADDING PLACEHOLDERTEXT
def add_placeholdertext(event=None):

    if not Input_Text_Box.get("1.0", "end-1c").strip():
        Input_Text_Box.insert("1.0", PLACEHOLDER_TEXT, "placeholder_tag")


#SEND BUTTON INITIALIZATION
send_button = Button(
    window, 
    text="Send",
    font=("Arial", 23, "bold"),
    bd=0,
    foreground="#ffffff",
    background="#36363d",
    width=10, 
    command=lambda: message_sent(None)
)
send_button.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="e")


#BINDING
Input_Text_Box.bind('<Return>', message_sent)
Input_Text_Box.bind('<FocusIn>', remove_placeholdertext)
Input_Text_Box.bind('<FocusOut>', add_placeholdertext)


#PLACEHOLDERTEXT INITIALIZATION
add_placeholdertext()


#EXECUTING GUI
window.mainloop()
