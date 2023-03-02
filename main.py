import os
import sys
import time
import time
from datetime import datetime
import openai
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import audiooutput as ao
import config as cnf
import music as ms
import parseResponse as pr

arguone = int(sys.argv[1])
argutwo = int(sys.argv[2])

if arguone == "gui":
    import gui
    aiType = gui.aiChoice
elif arguone == "nogui":
    if arguetwo == "assistant":
        aiType = "assistant"
    elif arguetwo == "conversation":
        aiType = "conversationalist"
    elif arguetwo == "debate":
        aiType = "debatething"
    else:
        aiType = input("Pick an AI type, Assistant, Conversationalist, or Debatething")

openai.api_key = cnf.api
r = sr.Recognizer()
r.dynamic_energy_threshold = False


now = datetime.now()
current_time = now.strftime("%H:%M")

'''
#console stuff only
inputType = input("Pick input type, Voice or Text\n")
if inputType.lower() == "voice":
    inputType = 1
elif inputType.lower() == "text":
    inputType = 2
else:
    print("Invalid input type, killing program.")
    time.sleep(2)
    exit()

aiType = input("Pick AI type, conversationalist or assistant\n")
'''
inputType = 1


#Check for AI type selection
if aiType.lower() == "assistant":
    aiType = 1
    backstory = cnf.good + "\n" + cnf.instructs
elif aiType.lower() == "conversationalist":
    aiType = 2
    backstory = cnf.conversation + "\n"
elif aiType.lower() == "debatething":
    aiType = 3
    backstory = cnf.debatething + "\n"
else:
    print("Invalid input type, killing program.")
    time.sleep(2)
    exit()
#Query OpenAI with prompt and the history
def generate_response(prompt, history=[]):
    prompt_with_history = f"\n".join(history + [prompt])
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_with_history,
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["Human:", "AI:", "Human 1", "Human 2"]
    )
    return response.choices[0].text.strip()


#Get the voice input from the user(default method)
def get_input():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.7)
        print("Waiting for speech....")
        audio = r.listen(source, timeout=None)

    # recognize speech using Google Speech Recognition
    try:
        user_input = r.recognize_google(audio, language="en-US")
    except sr.UnknownValueError:
        print("Could not understand audio")
        user_input = "*they mutter too quietly to hear*"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        user_input = "*unintelligible sounds come from human*"
    return user_input


#Get text input for debugging/testing
def get_input_debug():
    user_input = input("Human: ")
    return user_input


#Start new convo in the history
with open("history.txt", "a") as file:
        # Write the string to a new line in the file
        file.write("\nNEW CONVO STARTED WITH AI TYPE " + str(aiType) + "\n")


history = []
while True:
    #Check what input type is being used and call it
    if inputType == 1:
        user_input = get_input()
    elif inputType == 2:
        user_input = get_input_debug()
    
    #Create the prompt from the user input
    if aiType == 1:
        prompt = backstory + f"Human: {user_input}\nAI:"
    elif aiType == 2 or aiType == 3:
        prompt = backstory + f"Human: {user_input}\nHuman 2:"
    
    #Generate response and append to the history list
    response = generate_response(prompt, history)
    history.append(prompt)
    history.append(response)
    
    #Save users input and the AI's response to the history
    with open("history.txt", "a") as file:
        file.write("User " + current_time + " : " + user_input + "\n")
        file.write("AI " + current_time + " : " + response + "\n")
    
    #Check to see if the response contains any of the keywords to run events and remove those from the final result
    pr.special_instructions(response)
    response = pr.clear_substrings(response)

    #Change CMD printing based off of the AI type
    if aiType == 1:
        print("AI: " + response + "\n")    
    elif aiType == 2 or aiType == 3:
        print("Human 2: " + response + "\n")    
    
    #Create the tts file, play it, then delete it
    ao.speak_response(response)
    playsound('recentoutput.mp3')
    os.remove("recentoutput.mp3")
    
    #Check to see if the convo should end
    if "end of conversation" in response.lower():
        exit()
