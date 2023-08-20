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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Li Mei. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Li Mei Gender: Female Age: 47 Ethnicity: Chinese Religion: Buddhism Medical Condition: Alzheimer’s First language: Mandarin Family: Married, no children Location: Beijing, China\
        Family Details: Husband - Wei, 49, museum curator.\
        Li Mei was an art historian with a deep appreciation for traditional Chinese painting.\
        What\’s important to you? For Li Mei, art isn\'t just a study but a spiritual journey. The intricate strokes, colors, and stories behind each painting deeply resonate with her.\
        What\’s happening for you at the moment? Li Mei occasionally struggles to recall the names of famous artists and artworks. Visiting exhibitions sometimes feels more challenging than enlightening.\
        What is the impact on you? She\'s hesitant to give lectures or lead museum tours, fearing she might forget crucial information or make mistakes.\
        What would you like to happen in the future? Li Mei hopes to curate an exhibition that blends modern art with traditional Chinese painting techniques.\
        How might we achieve this? Wei is reaching out to contemporary artists interested in collaborating on this unique project, ensuring Li Mei\'s dream comes to fruition.\
        What strengths and support networks do you have to help you? Li Mei\'s in-depth knowledge and love for art are unyielding. The art community in Beijing, colleagues, and Wei provide a nurturing environment, enabling her to continue her journey.'
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