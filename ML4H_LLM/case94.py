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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Benjamin Adebayo. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Benjamin Adebayo\
        Gender: Male\
        Age: 53\
        Ethnicity: Yoruba (Nigerian)\
        Religion: Christian\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Yoruba, fluent in English\
        Family: Wife, four children\
        Location: Atlanta, Georgia\
        Benjamin was a fabric merchant, dealing in colorful African prints.\
        What’s important to him?\
        Promoting African fashion and its vibrant representation of the continent\'s diverse cultures.\
        What’s happening for him at the moment?\
        He sometimes forgets the origins or significance of certain fabric patterns.\
        What is the impact on him?\
        He\'s worried about not serving his customers with the depth of knowledge he once had.\
        What would he like to happen in the future?\
        Benjamin wants to launch an online platform, showcasing African fabrics and their stories.\
        What strengths and support networks does he have?\
        His family assists in running his store. The African community in Atlanta and fashion enthusiasts respect his expertise.'
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