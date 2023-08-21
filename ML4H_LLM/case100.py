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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Nathaniel Abebe. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Nathaniel Abebe\
        Gender: Male\
        Age: 50\
        Ethnicity: Ethiopian\
        Religion: Ethiopian Orthodox\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Amharic, speaks English\
        Family: Wife, three children\
        Location: Seattle, Washington\
        Nathaniel was a coffee trader, selling Ethiopian Arabica beans.\
        What’s important to him?\
        Introducing the world to the rich flavors of Ethiopian coffee.\
        What’s happening for him at the moment?\
        He sometimes forgets the nuances of different coffee bean types.\
        What is the impact on him?\
        He\'s concerned about maintaining his business reputation.\
        What would he like to happen in the future?\
        Nathaniel wants to open a café, showcasing Ethiopian coffee rituals.\
        What strengths and support networks does he have?\
        His family helps in the business, and coffee connoisseurs respect his expertise.'
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