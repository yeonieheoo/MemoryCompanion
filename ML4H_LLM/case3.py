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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Rosa Martinez. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Rosa Martinez Gender: Female Age: 68 Ethnicity: Hispanic Religion: Catholic Medical Condition: Early-onset Alzheimer’s First language: Spanish Family: Husband, three grandchildren Location: San Antonio, Texas\
        Family Details: Husband - Miguel, 70, retired construction worker. Grandchildren - Maria, 14, Carlos, 12, Sofia, 10.\
        Rosa was diagnosed with early-onset Alzheimer\'s a few years ago. She and Miguel live in a small house near the city center. They both love dancing and used to teach salsa to young couples.\
        Rosa occasionally forgets the steps and gets frustrated. She has a close bond with her grandchildren, especially Sofia, who reminds her of herself at that age.\
        What’s important to you? Her family, dancing, and preparing family meals on Sundays.\
        What’s happening for you at the moment? Rosa struggles with daily tasks like managing finances and sometimes doesn’t recognize her own grandchildren.\
		What is the impact on you? She feels lost and distressed when she forgets family members.\
		What would you like to happen in the future? Rosa wants to pass down her family recipes to Sofia and see her grandchildren graduate.\
		How might we achieve this? Miguel is gathering the family more often to create memories. They\'re also recording Rosa sharing her recipes.\
		What strengths and support networks do you have to help you? A loving husband, supportive grandchildren, and a \
		tight-knit community in their dance circle.'
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