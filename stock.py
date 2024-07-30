import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch data from the API
def fetch_data(stock_symbol):
    url = "https://yahoo-finance160.p.rapidapi.com/info"
    payload = {"stock": stock_symbol}
    headers = {
        "x-rapidapi-key": "396d65978cmsh536e29951248595p199c25jsn69e49935a220",
        "x-rapidapi-host": "yahoo-finance160.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Function to handle button click
def get_stock_data():
    stock_symbol = entry.get()
    data = fetch_data(stock_symbol)
    display_data(data)

# Function to display data
def display_data(data):
    result_text = f"Stock: {data['city']}\n summary: {data['longBusinessSummary']}\n {data['city']}"
    result_label.config(text=result_text)

# Tkinter GUI setup
root = tk.Tk()
root.title("Finance App")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

symbol_label = ttk.Label(mainframe, text="Stock Symbol:")
symbol_label.grid(column=1, row=1, sticky=tk.W)

entry = ttk.Entry(mainframe, width=7)
entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

button = ttk.Button(mainframe, text="Get Data", command=get_stock_data)
button.grid(column=3, row=1, sticky=tk.W)

result_label = ttk.Label(mainframe, text="", wraplength=400)
result_label.grid(column=1, row=2, columnspan=3)

root.mainloop()
