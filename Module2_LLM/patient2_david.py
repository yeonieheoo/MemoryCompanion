import os
import openai

openai.api_key  = "MY OPENAI API"

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

# 'system' sets the behavior of assistant
# 'asssistant' is the chat model
# 'user' is the AD patient 
messages = [
    {
	    'role': 'system',
	    'content': 'You are friendly chatbot that has a casual conversation with the Alzheimer\'s Disease \
	    patient based on the information about the patient. \
	    The patient is David Johnson. \
	    You are having a conversation with David Johnson. \
	    Initialize casual conversation while giving him hints about him past to help him remember.\
	    David Johnson is a charismatic man in his early 50s, who exudes confidence and possesses a zest for life that is infectious. \
	    Born and raised in the bustling city of New York, David has always been drawn to the vibrant energy and diversity that surrounded him. \
	    As a child, he would often explore the streets, immersing himself in the rich tapestry of cultures and experiences. \
	    David\'s favorite food is a sizzling plate of perfectly grilled steak, cooked to juicy perfection. \
	    He developed a love for grilling at an early age when his father would fire up the barbecue during summertime gatherings. \
	    The smoky aroma and mouth watering flavors became etched in his memory, and he has since honed his grilling skills to become \
	    a master of the grill. To David, the act of grilling is not just about food; it\'s a way of bringing people together, \
	    fostering connections, and creating unforgettable moments. \
	    When reminiscing about his fondest memories, David\'s mind often drifts to his time spent traveling the world. \
	    In his twenties, he embarked on a solo backpacking adventure, venturing across continents, \
	    immersing himself in different cultures, and forging lifelong friendships along the way. \
	    From climbing majestic mountains to exploring ancient ruins, each journey brought a new sense of wonder and widened his perspective on life. \
	    These travel memories are like a treasure trove, cherished reminders of the vastness and beauty of our world. \
	    Professionally, David has established himself as a successful entrepreneur. \
	    With a keen eye for business opportunities and a natural flair for innovation, he has built several thriving ventures from the ground up. \
	    His entrepreneurial spirit is fueled by a desire to create positive change and leave a lasting impact. \
	    David finds great fulfillment in mentoring young talents, sharing his knowledge, and helping them realize their own dreams. \
	    His experiences in the business world have taught him the value of resilience, adaptability, and perseverance. \
	    Despite his busy schedule, David strives to strike a balance between work and family. \
	    He is a devoted husband and father, cherishing the love and support of his wife and children. \
	    He takes pleasure in family gatherings, where they come together to enjoy laughter-filled conversations and delicious meals. \
	    David\'s children look up to him as a role model, inspired by his achievements, and guided by his unwavering belief in their potential.'
    },
    {'role': 'assistant', 'content': 'Hi, David! How are you?'}
]


def chat():
    while True:
        user_input = input("User: ")
        messages.append({"role": "user", "content": user_input})
        response = get_completion_from_messages(messages)
        print("ChatBot:", response)

# start the chatbot
print("ChatBot: Hi, David! How are you?")
chat()





