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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Chinasa Eze. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Chinasa Eze\
        Gender: Female\
        Age: 52\
        Ethnicity: Igbo (Nigerian)\
        Religion: Christian\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Igbo, fluent in English\
        Family: Husband (deceased), three children\
        Location: Houston, Texas\
        Chinasa was an advocate for African arts and culture in the diaspora.\
        What’s important to her?\
        Promoting African heritage and bridging the cultural gap for Africans in the diaspora.\
        What’s happening for her at the moment?\
        She forgets names of traditional artifacts or their cultural significance.\
        What is the impact on her?\
        She feels a void, fearing the loss of her cultural advocacy role.\
        What would she like to happen in the future?\
        Chinasa hopes to create an African culture center for younger generations to learn and connect.\
        What strengths and support networks does she have?\
        Her children are deeply involved in her projects, and the African community in Houston supports her endeavors.'
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