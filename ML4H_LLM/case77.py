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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Elena Ivanova. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Elena Ivanova\
        Gender: Female\
        Age: 53\
        Ethnicity: Russian\
        Religion: Orthodox Christian\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Russian, speaks English\
        Family: Divorced, one son\
        Location: Boston, Massachusetts\
        Elena was a mathematics professor, often presenting at international conferences.\
        What’s important to her?\
        She\'s devoted to mathematics, always encouraging her students to challenge conventional thought.\
        What’s happening for her at the moment?\
        She struggles to solve complex mathematical problems and sometimes loses her train of thought during lectures.\
        What is the impact on her?\
        She\'s distraught at the thought of not being able to guide her students effectively.\
        What would she like to happen in the future?\
        Elena hopes to author a series of math textbooks, simplifying complex topics.\
        What strengths and support networks does she have?\
        Her son, a mathematician as well, constantly discusses new theories with her. The academic community values her expertise and contributions.'
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