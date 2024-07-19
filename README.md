Trained Python ChatBot using Tkinter and Rasa

## Libraries
* pip install tkinter
* pip install rasa

## Rasa Install Instructions
* switch to python 3.8
* pip install spacy[universal] (optional?)
* pip install rasa
* rasa init (creates and trains default chatbot)
* rasa run (runs server on localhost)
* run python/tkinter file

## Training
domain.yml: 
* define intents (what is the user's goal?) 
* define entities (keywords in the user's message)
* create responses (based on specific intents)
data/nlu.yml:
* add training examples of potential responses
data/stories.yml:
* add sequences (using intents and actions)
terminal:
* rasa train (implement changes)