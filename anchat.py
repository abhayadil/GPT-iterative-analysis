#You will need to install the openai module
import openai

#You will need an api key from openai to run this code
openai.api_key = "<insert your openai api key here>"
#Note: api keys are chargable and you need to get it from openai

print("\nStarting GPT 3.5!\n\n")

messages = []
#This will the first input in the conversation after initial response
convo = 'Act as a personel analyst'

def get_completion(prompt, model = "gpt-3.5-turbo"):
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0,
    )
    return response.choices[0].message["content"]

#If you want to give a diiferent name to the file that is being read, change it here
inputer = open("inputdata.txt", encoding="utf8", mode="r")

text = inputer.read()

#Edit this prompt as per your requirements
prompt = f"""I want you to act as a book critic and expert in the subject of literature, \
You are working with one of the top book reviewing magazine. \
Criticize and review the content of the book, the content of the book is delimited by triple backticks. \
Your review should be at max 3 paragraphs long explaining in your thoughts about the book. \
``` {text}``` """

response = get_completion(prompt)

#Initial response is printed within lines to distinguish it from rest of the conversation
print("_______________________________________________________________________")
print("Inital prompt response:")
print("-----------------------------")
print(response)
print("_______________________________________________________________________")

print("\n\n Welcome to Analysis CHAT")
print(" Interact with ChatGPT 3.5\n")
print(" Instructions:\n - Type your question and click enter\n - ChatGPT will give its answer\n - To end chat type '...end' in lowercase\n")
print(" Ask your question:")

while convo != '...end':
    convo = input(" >>>  ")
    prompt = convo
    response = get_completion(prompt)
    messages.append({"role": "assistant", "content": response})
    print("\n ",response,"\n")

prompt = f"""Summarize the our entire conservation in at max 6 paragraphs, after your summary please highlight key takeways \
from our entire conversation in bullet points.
"""

response = get_completion(prompt)

outputer = open("gpt-response.txt", "w")

outputer.write(response)

outputer.close()

inputer.close()

print("\nResult is processed and saved in an txt file\n")
