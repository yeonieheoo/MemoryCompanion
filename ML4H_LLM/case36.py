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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Ananya Patil. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Ananya Patil Gender: Female Age: 53 Ethnicity: Indian Religion: Hindu Medical Condition: Alzheimer’s First language: Hindi Family: Married, one son, and one daughter Location: Mumbai, India\
        Family Details: Husband - Rajan, 55, architect. Children - Aditya, 29, photographer; Priya, 25, yoga instructor.\
        Ananya was a botanical scientist, working with medicinal plants, and has authored several research papers.\
        What’s important to you? Ananya believes in the union of science and tradition. For her, plants aren’t just species but carriers of ancient wisdom and healing powers.\
        What’s happening for you at the moment? Of late, she\'s been forgetting plant names and their properties, making it hard for her to continue her research.\
        What is the impact on you? The plants and her lab were her refuge. The increasing lapses in memory make her feel estranged from her life’s work, leading to moments of profound sadness.\
        What would you like to happen in the future? She dreams of starting a botanical garden that showcases medicinal plants, providing both education and serenity to visitors.\
        How might we achieve this? Aditya plans to document the journey through his photographs, while Priya contemplates integrating yoga sessions amidst the serene setting. Rajan, with his architectural skills, is designing the garden layout.\
        What strengths and support networks do you have to help you? Her family is a perfect blend of diverse talents, all committed to realizing Ananya’s dream. The scientific community, recognizing her contributions, has been providing research assistance and resources.'
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