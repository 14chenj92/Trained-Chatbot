import tkinter as tk
from tkinter import scrolledtext
import requests

# URL of the Rasa server
RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'

# Function to handle sending messages
def send_message():
    user_message = entry.get()
    if user_message.strip():
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "You: " + user_message + "\n")
        chat_area.yview(tk.END)
        entry.delete(0, tk.END)
        respond(user_message)
        chat_area.config(state=tk.DISABLED)

# Function to handle responses from Rasa
def respond(user_message):
    try:
        response = requests.post(RASA_SERVER_URL, json={"message": user_message})
        response.raise_for_status()
        responses = response.json()
        bot_message = '\n'.join([msg['text'] for msg in responses])
    except Exception as e:
        bot_message = f"Bot: Sorry, I encountered an error: {e}"
    
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "Bot: " + bot_message + "\n")
    chat_area.yview(tk.END)
    chat_area.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Rasa Chatbot")

# Create the chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "Bot: Hi! I'm your Rasa chatbot. Say something to start the conversation.\n")
chat_area.config(state=tk.DISABLED)

# Create the entry box
entry = tk.Entry(root)
entry.pack(padx=10, pady=10, fill=tk.X, expand=True)

# Bind the enter key to send message
entry.bind("<Return>", lambda event: send_message())

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Run the application
root.mainloop()
