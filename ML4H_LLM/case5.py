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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Priti Desai. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Priti Desai Gender: Female Age: 78 Ethnicity: Indian Religion: Hindu Medical Condition: Alzheimer’s First language: Gujarati Family: Three daughters, one son Location: Mumbai, India\
		Family Details: Daughter - Neha, 50, textile designer, lives in Delhi. Daughter - Rina, 47, doctor in Mumbai. Daughter - Aisha, 44, entrepreneur, lives in Bangalore. Son - Rahul, 40, musician, travels frequently.\
		Priti was a schoolteacher and is respected in her community. She loves gardening and has a balcony full of plants. She also enjoys traditional Indian music.\
		Priti often forgets to water her plants and has difficulty recognizing some of her long-time neighbors.\
		What\’s important to you? Priti cherishes her teaching days and the respect she receives from former students. She loves her garden and the peace it brings her.\
		What\’s happening for you at the moment? She sometimes forgets the names of plants she\'s been growing for years and gets upset about it.\
		What is the impact on you? Priti becomes very emotional when she can\'t remember things, especially related to her garden and teaching.\
		What would you like to happen in the future? She wants to see all her children settled and wishes to spend more time with her grandkids.\
		How might we achieve this? Rina, being in Mumbai, is considering moving Priti in with her to offer better care. They are also considering hiring a gardener to maintain her plants.\
		What strengths and support networks do you have to help you? Priti is active in her community group and has a close bond with her children, especially Rina.'
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