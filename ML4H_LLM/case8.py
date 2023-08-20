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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Santiago Mendoza. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Santiago Mendoza Gender: Male Age: 84 Ethnicity: Mexican Religion: Catholic Medical Condition: Alzheimer’s First language: Spanish Family: Four daughters Location: Guadalajara, Mexico\
        Family Details: Daughters - Maria, 59; Carmen, 57; Luz, 55; Rosa, 53.\
        Santiago was a mariachi musician. He enjoys listening to mariachi music and is fond of spicy food.\
        What’s important to you? His musical days and spending time with family during traditional fiestas.\
        What’s happening for you at the moment? Santiago occasionally forgets lyrics but still recalls tunes on his violin.\
        What is the impact on you? He becomes emotional when reminiscing about performances.\
        What would you like to happen in the future? He dreams of playing with his old mariachi group one last time.\
        How might we achieve this? Maria is reaching out to old band members for a surprise reunion.\
        What strengths and support networks do you have to help you? Santiago is beloved in his community and has strong support from his daughters.'
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