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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Esther Abioye. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Esther Abioye Gender: Female Age: 58 Ethnicity: Nigerian Religion: Christian Medical Condition: Alzheimer’s First language: Yoruba Family: Widowed, three grandchildren Location: Lagos, Nigeria\
        Family Details: Grandchildren - Tolu, 12; Bisi, 10; and Femi, 8.\
        Esther was a dance instructor, teaching traditional African dances to youngsters in her community.\
        What\’s important to you? Esther finds solace and joy in dance. For her, dance isn\'t just movement; it\'s a form of storytelling, an embodiment of culture and history.\
        What\’s happening for you at the moment? She occasionally loses her rhythm, forgetting dance steps that once came to her naturally. She\'s started mixing up instructions during her classes, causing confusion among her students.\
        What is the impact on you? Her confidence has been shaken, and she feels a deep sense of loss, not just for herself but for the cultural legacy she\'s been upholding.\
        What would you like to happen in the future? Esther dreams of seeing a dance school in her name, ensuring the preservation and propagation of traditional dances.\
        How might we achieve this? Local dance enthusiasts and former students are rallying together, pooling resources to set up a community dance school under Esther\'s guidance and mentorship.\
        What strengths and support networks do you have to help you? Esther\'s lifetime of experience, coupled with her inherent love for dance, ensures she remains an icon in the community. Her grandchildren and countless students are her pillars, constantly uplifting her and cherishing her invaluable contribution.'
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