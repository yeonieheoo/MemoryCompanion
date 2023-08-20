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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Leilani Kekoa. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Leilani Kekoa Gender: Female Age: 77 Ethnicity: Native Hawaiian Religion: Spiritual (Ancient Hawaiian beliefs) Medical Condition: Alzheimer’s First language: Hawaiian Family: Two sons, one daughter Location: Oahu, Hawaii\
        Family Details: Sons - Keanu, 49, surfer and entrepreneur; Makoa, 46, marine biologist. Daughter - Malia, 44, cultural guide.\
        Leilani was a hula teacher. She\'s deeply connected to the land and ocean and enjoys storytelling.\
        What’s important to you? Preserving Hawaiian culture and passing it onto the next generation.\
        What’s happening for you at the moment? Leilani sometimes forgets newer dance steps but recalls ancient tales.\
        What is the impact on you? She feels a deep sadness when she can\'t remember cultural details.\
        What would you like to happen in the future? To see her grandchildren embrace Hawaiian traditions.\
        How might we achieve this? Malia is documenting Leilani\'s stories for future generations.\
        What strengths and support networks do you have to help you? Leilani\'s community values her wisdom, and she has immense support from her family.'
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