import nltk
import random
import string

#download data
nltk.download('punkt')

#knowledge
knowledge={
"hello":"hii! how can i help you?",
"hii":"hello! what can i do for you?",
"what is ai?":"AI stand for ARTIFICIAL INTELLIGENCE.Ai is the simulation of human intelligence by machine.",
"what is machine learning":"machine learning is a subset of AI that allows system tp learn from data. ",
"what is nlp":"NATURAL LANGUAGE PROCESSING helps computer understand human language.",
"what is python":"python is a popular programming language used in Ai and Web development.",
"bye":"Goodbye! Have a nice day"
}

def preprocess(text):
    return text.lower().strip()
print("AI chatbot:hello ask me something type 'bye' to exit")

while True:
  user_input=input("you:")
  cleaned_input=preprocess(user_input)

  if cleaned_input in knowledge:
   print("AI chatbot",knowledge[cleaned_input])

   if cleaned_input=="bye":
      break
   else:
      print("AI chatot:sorry! i don't understand that yet")