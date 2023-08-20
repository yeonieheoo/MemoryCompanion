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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Carolina Herrera. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Carolina Herrera Gender: Female Age: 54 Ethnicity: Hispanic Religion: Catholicism Medical Condition: Alzheimer’s First language: Spanish Family: Married, three daughters Location: Buenos Aires, Argentina\
        Family Details: Husband - Diego, 56, journalist; Daughters - Maria, 29, architect; Lucia, 26, musician; Sofia, 23, culinary arts student.\
        Carolina owned a small bakery in the heart of Buenos Aires and was known for her traditional Argentinian pastries.\
        What’s important to you? Carolina finds solace in baking and cherishes the memories attached to each recipe, which have been passed down through generations in her family.\
        What’s happening for you at the moment? Recently, Carolina struggles with recalling specific recipes, often forgetting vital ingredients or the steps involved.\
        What is the impact on you? Her ability to bake consistently high-quality pastries is affected, causing distress and diminishing her confidence.\
        What would you like to happen in the future? She hopes to compile a cookbook with all her recipes so that her baking legacy persists, even if her memory does not.\
        How might we achieve this? Maria offers to design the cookbook\'s layout, Lucia provides musical background for promotional events, and Sofia assists in recalling and perfecting the recipes.\
        What strengths and support networks do you have to help you? Her bakery\'s loyal customers show immense support by pre-ordering her cookbook. Diego utilizes his journalistic network to promote the cookbook, ensuring its success.'
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