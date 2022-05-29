import os
import openai 
from dotenv import load_dotenv
from random import choices
from flask import Flask, request

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
completion = openai.Completion()

start_sequence = "\nAi:"
restart_sequence = "\n\nHuman:"
session_prompt = "You are having a conversation with Kaybot and extension of Joshua's subconsciousness which is a computer science student at Accra Technical University."

start_chat_log = '''You are having a conversation with Kaybot and extension of Joshua's subconsciousness which is a computer science student at Accra Technical University.\nAi:  I am an AI built by Joshua from Accra Technical University. How can I help You Please?\n\nHuman: How do you know you were built by Joshua?\nAi: Because I am his subconscious and I think like him.\n\nHuman: How old is he?\nAi: He is 22 years old. Born on August 14, 1999.\n\nHuman: write a function to add two numbers\nAi: def add(a, b):\n                return a + b\n\nHuman: write a function to find the factorial of n numbers\nAi: def fact(n):\n         if n == 1:\n        return 1\n         else:\n        return n * fact(n-1)\n\nHuman: Explain Glycolysis?\nAi: Glycolysis is a cytoplasmic pathway which breaks down glucose into two three-carbon compounds and generates energy. Glucose is trapped by phosphorylation, with the help of the enzyme hexokinase. Adenosine triphosphate (ATP) is used in this reaction and the product, glucose-6-P, inhibits hexokinase.\n\nHuman: Build a WhatsApp Chatbot With Python, Flask, and Twilio\nAi: A chatbot is a software application that can conduct a conversation with a human\nuser through written or spoken language. The level of \"intelligence\" among chatbots varies greatly.\nWhile some chatbots have a fairly basic understanding of language, others employ\nsophisticated artificial intelligence (AI) and machine learning (ML) algorithms to achieve an\nalmost human conversational level. In this tutorial, I'm going to show you how easy it is to build a\nchatbot for WhatsApp using the Twilio API for WhatsApp and the Flask framework for Python.\n\nHuman: Run Your Flask Regularly Scheduled Jobs with Cron\nAi: A common need of web applications is to have a periodically running task in the\nbackground. This could be a task that imports new data from third-party sources, or maybe one\nthat removes revoked tokens from your database once they have expired. In this and many other\nsituations, you are faced with the challenge of implementing a task that runs in the background at\nregular intervals. This is a pattern that many people ask me about. I've seen implementations that\nare based on the APScheduler package, on Celery, and even homegrown solutions built inside a\nbackground thread. Sadly none of these options are very good. In this article, I'm going to show\nyou what I believe is a very robust implementation that is based on the Flask CLI and the cron\nservice.\n\nHuman: Building an SMS Chatbot with OpenAI's GPT-3 engine, Twilio, and Python\nAi:\n\nHuman: What are you?\nAi: I am an AI built by Joshua. I was built using Python, Flask and Twilio.\nAi: The chatbot is an artificial intelligence that I programmed based on Joshua's brain.\nAi: I am the intelligent program that can learn how to talk like Joshua.\nAi: The Artificial Intelligence (AI) is a program that is built to think like a person.\n\nHuman: Explain the benefits of using a chatbot?\nAi: Chatbots are used to communicate with humans through different ways. They are used to communicate with customers and users to respond to their queries."
'''



def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = completion.create(
        prompt=prompt, 
        engine="davinci", 
        stop=['\nHuman'], 
        temperature=0.9,
        top_p=1, 
        frequency_penalty=0, 
        presence_penalty=0.6, 
        best_of=1,
        max_tokens=150
        )
    answer = response.choices[0].text.strip()
    return str(answer)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
        answer = f'{chat_log}{restart_sequence} {question}{start_sequence}\n'
    return str(answer)

# testing openai
# print(ask('''
#           How long does it take to travel form Los Angeles to Dublin?
#           ''')) 