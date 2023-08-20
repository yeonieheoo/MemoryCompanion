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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Farah Al-Qasimi. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Farah Al-Qasimi Gender: Female Age: 49 Ethnicity: Emirati Religion: Islam Medical Condition: Alzheimer’s First language: Arabic Family: Married, two sons, one daughter Location: Dubai, United Arab Emirates\
        Family Details: Husband - Omar, 52, businessman; Sons - Ahmed, 28, engineer; Rashid, 24, professional soccer player; Daughter - Aisha, 22, poet.\
        Farah was a teacher, spending over two decades teaching history to high school students in Dubai.\
        What\’s important to you? Farah values education and believes in imparting the rich history of the Middle East to younger generations. She\'s amassed a collection of historical artifacts and documents.\
        What\’s happening for you at the moment? Farah sometimes struggles to recall specific historical events, often confusing timelines, which she once recited effortlessly.\
        What is the impact on you? Her inability to remember historical details disturbs her deeply, as she fears losing touch with her past and cultural identity.\
        What would you like to happen in the future? She wants to establish a small museum in her community to both share her collection and engage the youth with their rich history.\
        How might we achieve this? With Ahmed\'s engineering skills, a plan for the museum\'s structure is conceived, while Aisha offers to write informational content, and Rashid uses his influence to gather community support.\
        What strengths and support networks do you have to help you? Omar provides financial backing for the museum. Farah\'s former students, inspired by her dedication, volunteer to help in various roles. The local community acknowledges her contributions and rallies around her vision.'
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