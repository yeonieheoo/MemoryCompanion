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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Helena "Lena" Olsson. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Helena "Lena" Olsson\
        Gender: Female\
        Age: 57\
        Ethnicity: Swedish\
        Religion: Lutheran\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Swedish, fluent in English\
        Family: Divorced, one daughter, one grandson\
        Location: Minneapolis, Minnesota\
        Lena was an architect, known for her sustainable designs.\
        What’s important to her?\
        Lena believes in eco-friendly architecture, creating spaces that resonate with nature.\
        What’s happening for her at the moment?\
        She\'s having difficulty visualizing design concepts and sometimes forgets clients\' requirements.\
        What is the impact on her?\
        Her ability to design and deliver projects is compromised, affecting her professional reputation.\
        What would she like to happen in the future?\
        Lena wants to collaborate with younger architects and pass on her knowledge of sustainable design.\
        What strengths and support networks does she have?\
        Her daughter, also an architect, collaborates with her on projects. The architectural community acknowledges her work, providing platforms for her to share her insights.'
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