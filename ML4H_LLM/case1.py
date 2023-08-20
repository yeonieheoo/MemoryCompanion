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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Arthur McMillan. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
	    Name: Arthur McMillan Gender: Male Age: 79 Ethnicity: White American Religion: Protestant Medical Condition: Alzheimer’s disease \
        First language: English Family: Two daughters Location: Suburban New York Family Details: Daughter - Emily, 51, works as a schoolteacher in New Jersey, married to Jeff, two children Paul, 23, and Jessica, 21. Daughter - Sarah, 47, a nurse in New York City, recently divorced, one child, Hannah, 17.\
        Arthur and his late wife lived in the same house for over 50 years. His wife passed away five years ago. Arthur has always been a lover of books and has a vast collection. He also enjoys woodworking.\
        Recently, neighbors have found him wandering around the block, seemingly disoriented. On one occasion, he attempted to enter a neighbor’s house, thinking it was his own. Emily and Sarah visit once a week, often bringing groceries and meals.\
        Arthur regularly attends a senior center but has been forgetting the days and sometimes goes when it\'s closed.\
        What’s important to you? Arthur loves reading historical novels and woodworking in his garage. He cherishes the family get-togethers during the holidays.\
        What’s happening for you at the moment? He\'s feeling more confused recently, often forgetting where he places his tools or the books he\'s currently reading. He misses his late wife terribly and sometimes calls Emily by her name.\
        What is the impact on you? He feels isolated and doesn\’t like to admit he\'s forgetting things. He\'s worried about being a burden to his daughters.\
        What would you like to happen in the future? Arthur wishes to stay in his home and continue his hobbies. He hopes to see his granddaughter Hannah go to college.\
        How might we achieve this? Emily and Sarah have discussed hiring a daily caregiver to check on Arthur, prepare his meals, and ensure he\'s safe.\
        What strengths and support networks do you have to help you? He has close relationships with his daughters and grandchildren. His neighbor, Mrs. Roberts, checks on him every now and then.'
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