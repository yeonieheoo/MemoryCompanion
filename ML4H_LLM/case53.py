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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Sophie Chen. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Sophie Chen\
        Gender: Female\
        Age: 56\
        Ethnicity: Chinese\
        Religion: Buddhist\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Mandarin, speaks English\
        Family: Daughter, son-in-law, two grandchildren\
        Location: San Francisco\
        Sophie owned a small bookstore, which her daughter now runs. She\'s an avid reader, enjoys Tai Chi, and is deeply involved in the local Chinese community.\
        What’s important to her?\
        Sophie takes pride in her bookstore\'s legacy and is passionate about literature. She finds peace in practicing Tai Chi and values her involvement in community events.\
        What’s happening for her at the moment?\
        She\'s been having difficulty recalling book titles and authors, and sometimes she gets lost in familiar places, like her neighborhood park.\
        What is the impact on her?\
        These lapses in memory are causing Sophie anxiety, particularly the thought of forgetting her favorite books. She\'s also hesitant to practice Tai Chi in groups now, fearing she\'ll forget movements.\
        What would she like to happen in the future?\
        Sophie wants to find ways to manage her condition, possibly through memory-enhancing exercises. She also wishes to spend more quality time with her grandchildren, sharing stories of her life.\
        What strengths and support networks does she have?\
        Her daughter and son-in-law are supportive, helping her manage her daily routines. The local Chinese community has been understanding, and her Tai Chi instructor offers private sessions.'
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