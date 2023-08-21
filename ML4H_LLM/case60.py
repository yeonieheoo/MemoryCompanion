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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Luis Rodriguez. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Luis Rodriguez\
        Gender: Male\
        Age: 60\
        Ethnicity: Hispanic\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Spanish\
        Family: Wife, two daughters\
        Location: San Diego, California\
        Luis was a marine biologist, having spent years studying marine ecosystems.\
        What’s important to him?\
        Luis treasures the memories of his sea expeditions and the joy of discovery. He also values the time spent teaching his daughters to swim and snorkel.\
        What’s happening for him at the moment?\
        He\'s started forgetting names of common marine species and recently got disoriented during a beach visit.\
        What is the impact on him?\
        Luis feels disconnected from the marine world he once loved, causing bouts of depression. He fears he might become a burden to his family.\
        What would he like to happen in the future?\
        He hopes to pen down his adventures in a book and perhaps set up a small marine exhibit with his collected specimens.\
        What strengths and support networks does he have?\
        His wife is his primary caregiver, and his daughters frequently engage him in marine-related activities to keep his spirit up. The local marine research community offers support and resources.'
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