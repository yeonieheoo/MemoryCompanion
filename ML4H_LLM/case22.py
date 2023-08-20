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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Omar Al-Saad. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Omar Al-Saad Gender: Male Age: 53 Ethnicity: Arabic Religion: Islam Medical Condition: Alzheimer’s First language: Arabic Family: Wife, one daughter, one son Location: Cairo, Egypt\
        Family Details: Wife - Laila, 50, school principal. Children - Yasmeen, 24, fashion designer; Sami, 21, college student.\
        Omar was a renowned architect, known for blending traditional designs with modern concepts.\
        What’s important to you? Omar takes pride in the skylines he\'s contributed to. Family gatherings during Ramadan and Eid, with all the laughter and shared meals, are something he cherishes.\
        What’s happening for you at the moment? Lately, Omar has found it challenging to remember certain architectural terms. He also forgets appointments and misplaces sketches frequently.\
        What is the impact on you? His inability to remember details affects ongoing projects. Omar finds it difficult to cope with the fact that he\'s not as efficient as he once was.\
        What would you like to happen in the future? He hopes to see his children settled and to complete one last architectural marvel, a tribute to his journey.\
        How might we achieve this? Yasmeen, with her design knowledge, is collaborating with him on this new project. Sami is digitizing his father\'s works to create a digital portfolio.\
        What strengths and support networks do you have to help you? Omar\'s decades of experience in architecture still guide many. His colleagues and former students are always around, providing both professional and emotional support.'
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