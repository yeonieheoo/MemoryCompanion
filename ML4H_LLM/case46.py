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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Tendai Moyo. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Tendai Moyo Gender: Male Age: 59 Ethnicity: Zimbabwean Religion: Christianity Medical Condition: Alzheimer’s First language: Shona Family: Widowed, two sons Location: Harare, Zimbabwe\
        Family Details: Sons - Takudzwa, 32, wildlife conservationist; Kuda, 28, teacher.\
        Tendai was an avid gardener, transforming his backyard into a haven of native plants and a sanctuary for local birds.\
        What’s important to you? Tendai values the harmony of nature and believes in the importance of preserving local flora and fauna.\
        What’s happening for you at the moment? Tendai often forgets to water the plants or where he\'s planted certain species, leading to a decline in the garden\'s health.\
        What is the impact on you? His once-thriving garden is now showing signs of neglect, causing him emotional distress and a feeling of loss.\
        What would you like to happen in the future? He desires to transform his garden into a community space where local children can learn about native plants and their importance.\
        How might we achieve this? Takudzwa introduces native animals into the garden, turning it into an ecological educational center. Kuda incorporates garden lessons into his school curriculum, ensuring a steady stream of young learners.\
        What strengths and support networks do you have to help you? Tendai\'s neighbors volunteer to help maintain the garden and set up educational stations. The local community donates resources to ensure the garden remains a vibrant educational hub.'
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