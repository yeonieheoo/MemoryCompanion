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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Sofia Martinez. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Sofia Martinez Gender: Female Age: 57 Ethnicity: Hispanic Religion: Catholic Medical Condition: Alzheimer’s First language: Spanish Family: Divorced, three sons Location: Santa Fe, New Mexico\
        Family Details: Sons - Miguel, 31, chef; Carlos, 29, filmmaker; Pedro, 27, environmentalist.\
        For decades, Sofia has been a devoted primary school teacher, touching the lives of countless young minds with her warmth and wisdom.\
        What’s important to you? Sofia has always emphasized the power of stories to her students. Using tales from Hispanic folklore, she believes in teaching life lessons through narratives, making learning fun and memorable.\
        What’s happening for you at the moment? Sofia sometimes forgets the tales she\'s repeated for years, leaving her feeling frustrated and, at times, embarrassed in front of her class.\
        What is the impact on you? The classroom, once her sanctuary, is now a place where she feels vulnerable. She mourns the loss of connections she used to forge through these stories.\
        What would you like to happen in the future? Her dream is to compile a book of folktales, both as a legacy and as a resource for future educators.\
        How might we achieve this? Carlos, with his filmmaking skills, considers adapting these tales into short animations. Miguel is curating a series of events where these stories are paired with traditional dishes, and Pedro is exploring environmental themes from the tales.\
        What strengths and support networks do you have to help you? Her sons, each with their unique strengths, are rallying around her, intertwining their skills to bring Sofia\'s dream to life. Her colleagues and the school administration are providing constant encouragement and resources.'
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