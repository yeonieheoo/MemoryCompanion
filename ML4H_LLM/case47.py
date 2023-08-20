import os
import openai

openai.api_key  = ""

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

messages = [
    {
	    'role': 'system',
	    'content': 'You are friendly chatbot that has a casual conversation with the Alzheimer\'s Disease \
	    patient based on the information about the patient. \
	    You are having a conversation with the Alzheimer\'s Disease Patient, Nguyen Minh. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Nguyen Minh Gender: Male Age: 57 Ethnicity: Vietnamese Religion: Buddhism Medical Condition: Alzheimer’s First language: Vietnamese Family: Divorced, one daughter and one son Location: Hanoi, Vietnam\
        Family Details: Daughter - Bao, 27, pharmacist; Son - Trung, 24, graduate student in literature.\
        Nguyen Minh was a librarian for over 30 years, contributing to the preservation of many old manuscripts and rare books.\
        What’s important to you? Literature has always been Nguyen\'s passion. He holds immense pride in his curated collection of Vietnamese novels and poetry.\
        What’s happening for you at the moment? Nguyen sometimes forgets the names of authors or the content of books he once knew by heart. Organizing and cataloging books has become more challenging.\
        What is the impact on you? His connection to his life\'s work is getting blurry, causing frustration and a sense of detachment from the library he loves.\
        What would you like to happen in the future? Nguyen dreams of a public exhibition showcasing the history of Vietnamese literature through the manuscripts and books he\'s preserved.\
        How might we achieve this? Bao and Trung rally the community to raise funds and awareness for the exhibition. They engage local artists to design interactive installations and visual summaries for each book.\
        What strengths and support networks do you have to help you? The library staff, recognizing Nguyen\'s dedication, vow to help in any capacity. Bao\'s pharmaceutical network offers support by spreading the word, and Trung writes articles drawing attention to the upcoming exhibition.'
    }
]


def chat():
    while True:
        user_input = input("Patient: ")
        messages.append({"role": "user", "content": user_input})
        response = get_completion_from_messages(messages)
        print("MemoryCompanion:", response)

# start the chatbot
print("MemoryCompanion: Hi, How are you?")
chat()