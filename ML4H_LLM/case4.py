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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Alan Smith. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Alan Smith Gender: Male Age: 85 Ethnicity: White Australian Religion: Anglican Medical Condition: Alzheimer’s disease First language: English Family: Deceased wife, two sons Location: Perth, Western Australia\
		Family Details: Sons - David, 55, marine biologist, lives in Brisbane. Son - Steven, 53, owns a bookstore in Sydney.\
		Alan was a geologist and has an extensive collection of rocks and minerals. He enjoys beach walks and has a passion for marine life, often visiting aquariums.\
		Alan\'s neighbors have noticed him wandering around the beach looking lost. He sometimes forgets the names of his sons and calls them by his late wife\'s name.\
		What’s important to you? Alan loves his rock collection and the memories associated with each specimen. He has fond memories of diving with his sons.\
		What’s happening for you at the moment? Alan often forgets recent events, like the last meal he had, but vividly remembers his diving trips from decades ago.\
		What is the impact on you? He becomes frustrated when he can\'t remember recent events and is fearful of losing his memories of his wife.\
		What would you like to happen in the future? Alan wishes to document his rock collection and share his diving stories with his grandchildren.\
		How might we achieve this? David and Steven are planning a family reunion and are considering hiring a professional to document Alan\'s stories.\
		What strengths and support networks do you have to help you? Alan\'s neighbors keep an eye on him and he has a close bond with both his sons.'
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