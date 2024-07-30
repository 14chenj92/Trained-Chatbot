# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionGetStock(Action):

    def name(self) -> Text:
        return "action_get_stock"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        stock_symbol = tracker.get_slot('stock_symbol')
        stock_info = self.fetch_stock_data(stock_symbol)

        if stock_info:
            response = f"Stock: {stock_symbol}\nSummary: {stock_info}"
        else:
            response = "Sorry, I couldn't fetch the stock information."

        dispatcher.utter_message(text=response)
        return []

    def fetch_stock_data(self, stock_symbol: Text) -> Text:
        url = "https://yahoo-finance160.p.rapidapi.com/info"
        payload = {"stock": stock_symbol}
        headers = {
            "x-rapidapi-key": "396d65978cmsh536e29951248595p199c25jsn69e49935a220",
            "x-rapidapi-host": "yahoo-finance160.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if 'longBusinessSummary'or 'business summary' in data:
                return data['longBusinessSummary']
            elif 'city' in data:
                return data['city']
        return None

