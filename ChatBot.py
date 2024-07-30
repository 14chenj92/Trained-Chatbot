import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk
import requests

# Function to handle sending messages
def send_message():
    user_message = entry.get()
    if user_message.strip():
        chat_area.configure(state=tk.NORMAL)
        chat_area.insert(tk.END, "You: " + user_message + "\n")
        chat_area.yview(tk.END)
        entry.delete(0, tk.END)
        respond(user_message)
        chat_area.configure(state=tk.DISABLED)

# Function to handle responses from Rasa
def respond(user_message):
    RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'
    try:
        response = requests.post(RASA_SERVER_URL, json={"message": user_message})
        response.raise_for_status()
        responses = response.json()
        bot_message = '\n'.join([msg['text'] for msg in responses])
    except Exception as e:
        bot_message = f"Bot: Sorry, I encountered an error: {e}"
    
    chat_area.configure(state=tk.NORMAL)
    chat_area.insert(tk.END, "Bot: " + bot_message + "\n")
    chat_area.yview(tk.END)
    chat_area.configure(state=tk.DISABLED)

# Create the main window
root = ctk.CTk()
root.title("Chatbot")
root.geometry("300x400")

text_font="Perpetua"
text_size=14

# Set dark mode
ctk.set_appearance_mode("dark")

# Create the chat area
chat_area = ctk.CTkTextbox(root, wrap=tk.WORD, state='disabled', bg_color="#2e2e2e", text_color="#ffffff", font=(text_font, text_size))
chat_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
chat_area.configure(state=tk.NORMAL)
chat_area.insert(tk.END, "Bot: Hi! I'm your Rasa chatbot. Say something to start the conversation.\n")
chat_area.configure(state=tk.DISABLED)

# Create the entry box
entry = ctk.CTkEntry(root, font=(text_font, text_size), bg_color="#3e3e3e", text_color="#ffffff")
entry.pack(padx=10, pady=5, fill=tk.X, expand=True)

# Create the send button
send_button = ctk.CTkButton(root, text="Send", command=send_message, fg_color="#007bff", hover_color="#0056b3", font=(text_font, text_size))
send_button.pack(pady=5)

# Run the application
root.mainloop()
