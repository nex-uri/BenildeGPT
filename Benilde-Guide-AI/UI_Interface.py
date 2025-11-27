import os
from tkinter import *
from API_Function import chat_execute

window = Tk()
window.geometry("420x420")
window.resizable(False, False)
window.title("Benilde AI")

MIN_LINES = 1

window.grid_columnconfigure(0, weight=1) 
window.grid_columnconfigure(1, weight=0) 
window.grid_rowconfigure(0, weight=1) 

chat_history = Text(
    window, 
    height=20, 
    state=DISABLED,
    font=("Arial", 12),
    wrap=WORD
)
chat_history.grid(
    row=0, 
    column=0, 
    columnspan=2, 
    padx=10, 
    pady=5, 
    sticky="nsew"
)

Input_Text_Box = Text(
    window, 
    width=50, 
    height=MIN_LINES, 
    font=("Arial", 12),
    wrap=WORD
)
Input_Text_Box.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="ew")

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

    if message_given and not chat_history_given:
        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"{os.environ.get('USERNAME')}: ", "user_name_tag")
        chat_history.insert(END, f"{message_given}\n\n")
        chat_history.insert(END, f"Benilde Chatbot: ", "ai_name_tag")

        chat_execute(message_given, update_chat_history)

        chat_history.config(state=DISABLED)

        Input_Text_Box.delete("1.0", END)

    elif message_given and chat_history_given:
        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"\n\n\n{os.environ.get('USERNAME')}: ", "user_name_tag")
        chat_history.insert(END, f"{message_given}\n\n")
        chat_history.insert(END, "Benilde Chatbot: ", "ai_name_tag")

        chat_execute(message_given, update_chat_history)

        chat_history.config(state=DISABLED)

        Input_Text_Box.delete("1.0", END)

send_button = Button(window, text="Send", width=10, command=lambda: message_sent(None))
send_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

Input_Text_Box.bind('<Return>', message_sent)

window.mainloop()