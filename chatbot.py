import tkinter as tk
from tkinter import scrolledtext

# Define the chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I don't understand that."

# Function to handle sending and receiving messages
def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() != "":
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot_response(user_input)
        chat_log.insert(tk.END, "Chatbot: " + response + "\n\n")
        chat_log.config(state=tk.DISABLED)
        chat_log.yview(tk.END)
        user_entry.delete(0, tk.END)

# Function to handle exit
def on_closing():
    root.destroy()

# Create GUI window
root = tk.Tk()
root.title("Simple Chatbot")

# Create a frame for the chat log
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a scrolled text widget for the chat log
chat_log = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state=tk.DISABLED, height=20, width=60)
chat_log.pack(padx=10, pady=10)

# Create an entry widget for user input
user_entry = tk.Entry(root, width=50)
user_entry.pack(padx=10, pady=10, side=tk.LEFT)

# Bind the return key to send message
user_entry.bind("<Return>", send_message)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Handle window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the application
root.mainloop()
