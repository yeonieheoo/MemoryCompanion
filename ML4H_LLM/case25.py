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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Alejandro Fernandez. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Alejandro Fernandez Gender: Male Age: 49 Ethnicity: Hispanic Religion: Catholic Medical Condition: Alzheimer’s First language: Spanish Family: Single, one sister Location: Buenos Aires, Argentina\
        Family Details: Sister - Clara, 52, pediatrician.\
        Alejandro used to be a tango instructor, a dance deeply rooted in Argentine culture.\
        What’s important to you? For Alejandro, the thrill of tango isn\'t just in the dance but in its ability to tell passionate stories. He cherishes the memories of evenings spent dancing at milongas.\
        What’s happening for you at the moment? Recently, Alejandro sometimes forgets his dance steps. The once vibrant milonga settings now seem overwhelming and confusing.\
        What is the impact on you? He\'s had to reduce the number of classes he teaches, which diminishes his connection to the dance community. Alejandro fears losing the essence of tango from his life.\
        What would you like to happen in the future? He wishes to open a tango school, ensuring that the dance\'s legacy continues even if he can no longer teach.\
        How might we achieve this? Clara is exploring locations and funding opportunities for the school. Several of Alejandro\'s former students have volunteered to teach at the new institution.\
        What strengths and support networks do you have to help you? Alejandro’s passion for tango still burns brightly. His students and the Buenos Aires dance community continually rally around him, offering support and love.'
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