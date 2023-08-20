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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Mei Ling. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Mei Ling Gender: Female Age: 78 Ethnicity: Chinese Religion: Buddhist Medical Condition: Alzheimer’s First language: Mandarin Family: One son Location: Beijing, China\
        Family Details: Son - Wei, 52, journalist in Shanghai.\
        Mei was a traditional dancer and still enjoys watching performances. She maintains a small garden with bonsai trees.\
        What’s important to you? Mei loves reminiscing about her dancing days and nurturing her bonsai trees.\
        What’s happening for you at the moment? She sometimes mixes up traditional dance forms or forgets to water her trees.\
        What is the impact on you? Mei becomes agitated when she can\'t remember dance routines.\
        What would you like to happen in the future? She wants to visit a traditional dance performance with her son and grandchildren.\
        How might we achieve this? Wei is planning a trip to bring Mei to Shanghai for a renowned dance festival.\
        What strengths and support networks do you have to help you? Mei\'s neighbors are supportive, and she has a tight bond with Wei.'
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