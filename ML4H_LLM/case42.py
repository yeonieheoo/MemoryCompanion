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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Carmen Rodriguez. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Carmen Rodriguez Gender: Female Age: 56 Ethnicity: Colombian Religion: Roman Catholic Medical Condition: Alzheimer’s First language: Spanish Family: Widowed, three daughters Location: Bogotá, Colombia\
        Family Details: Daughters - Sofia, 29, environmental scientist; Lucia, 27, musician; Maria, 25, social worker.\
        Carmen dedicated her life to botany, especially studying Colombia\'s rich orchid diversity, and running a local botanical garden.\
        What\’s important to you? She values nature\'s wonders, especially the unique flora of Colombia. Her garden is both her workplace and sanctuary.\
        What\’s happening for you at the moment? While Carmen can describe the characteristics of orchids she studied decades ago, she sometimes forgets their names or their care routines.\
        What is the impact on you? Seeing her beloved plants wilt due to her forgetfulness deeply saddens her. She fears her life\'s work could fade away.\
        What would you like to happen in the future? Carmen wishes to host educational workshops in her garden, sharing her knowledge while also creating lasting documentation of her findings.\
        How might we achieve this? Sofia proposes to intertwine her environmental studies with her mother\'s work, while Lucia considers a series of musical pieces inspired by different orchids. Maria, using her social work background, seeks grants to fund the workshops.\
        What strengths and support networks do you have to help you? Her daughters, with their varied skills, are united in preserving Carmen’s legacy. The botanical community, understanding the depth of Carmen\'s knowledge, stands ready to assist in various capacities.'
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