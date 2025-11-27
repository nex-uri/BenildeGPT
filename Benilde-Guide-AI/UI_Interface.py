import os
from tkinter import *
from API_Function import chat_execute

window = Tk()
window.geometry("420x420")
window.resizable(False, False)
window.title("Benilde AI")
window.config(background="#202024")

PLACEHOLDER_TEXT = "Enter your message here"

MIN_LINES = 1

window.grid_columnconfigure(0, weight=1) 
window.grid_columnconfigure(1, weight=0) 
window.grid_rowconfigure(0, weight=1) 

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
Input_Text_Box.grid(row=1, column=0, padx=(10, 10), pady=5, sticky="ew")

Labeling = Label(
    window,
    text="Benilde AI",
    foreground="#ffffff",
    background="#202024",
    font=("Arial", 25, "bold")
)
Labeling.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")


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

def update_chat_history(chunk):
    chat_history.config(state=NORMAL)
    chat_history.insert(END, chunk) 
    chat_history.config(state=DISABLED)
    chat_history.see(END) 

    window.update()

def message_sent(event):
    message_given = Input_Text_Box.get("1.0", "end-1c").strip()
    chat_history_given = chat_history.get("1.0", "end-1c").strip()
    placeholder_text = Input_Text_Box.get("1.0", "end-1c").strip()

    if message_given and not chat_history_given:
        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"{os.environ.get('USERNAME')}: ", "user_name_tag")
        chat_history.insert(END, f"{message_given}\n\n")
        chat_history.insert(END, f"Benilde Chatbot: ", "ai_name_tag")

        chat_execute(message_given, update_chat_history)

        chat_history.config(state=DISABLED)

        Input_Text_Box.delete("1.0", END)

        if placeholder_text == PLACEHOLDER_TEXT:
            Input_Text_Box.delete("1.0", END)


    elif message_given and chat_history_given:
        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"\n\n\n{os.environ.get('USERNAME')}: ", "user_name_tag")
        chat_history.insert(END, f"{message_given}\n\n")
        chat_history.insert(END, "Benilde Chatbot: ", "ai_name_tag")

        chat_execute(message_given, update_chat_history)

        chat_history.config(state=DISABLED)

        Input_Text_Box.delete("1.0", END)

        if placeholder_text == PLACEHOLDER_TEXT:
            Input_Text_Box.delete("1.0", END)

    return "break"

def remove_placeholdertext(event):
    placeholder_text = Input_Text_Box.get("1.0", "end-1c").strip()

    if placeholder_text == PLACEHOLDER_TEXT:
        Input_Text_Box.delete("1.0", END)
        Input_Text_Box.unbind('<FocusIn>', remove_placeholdertext)

def add_placeholdertext(event=None):

    if not Input_Text_Box.get("1.0", "end-1c").strip():
        Input_Text_Box.insert("1.0", PLACEHOLDER_TEXT, "placeholder_tag")


send_button = Button(
    window, 
    text="Send",
    font=("Arial", 9, "bold"),
    bd=0,
    foreground="#ffffff",
    background="#36363d",
    width=10, 
    command=lambda: message_sent(None)
)
send_button.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="e")


Input_Text_Box.bind('<Return>', message_sent)
Input_Text_Box.bind('<FocusIn>', remove_placeholdertext)
Input_Text_Box.bind('<FocusOut>', add_placeholdertext)

add_placeholdertext()
window.mainloop()
