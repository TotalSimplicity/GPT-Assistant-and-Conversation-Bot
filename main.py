import os
import sys
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


openai.api_key = cnf.api
r = sr.Recognizer()
r.dynamic_energy_threshold = False
now = datetime.now()
current_time = now.strftime("%m/%d/%Y %H:%M:%S")
inputType = 1

# Get arguments
try:
    programname = sys.argv[0]
    arguone = sys.argv[1]
    argutwo = sys.argv[2]
except IndexError:
    aitype = "undefined"

# Check arguments and set variables
if arguone == "gui" and argutwo is not None:
    print("The argument \"gui\" does not require any other arguments")
    exit()
elif arguone == "gui":
    import gui
    aiType = gui.aiChoice
elif arguone == "nogui":
    if argutwo == "assistant":
        aiType = "assistant"
        
    elif argutwo == "conversation":
        aiType = "conversationalist"
        
    elif argutwo == "debate":
        aiType = "debatething"
        
    else:
        aiType = input("Pick an AI type, Assistant, Conversationalist, or Debatething\n")
        if aiType.lower() != "assistant" and aiType.lower() != "conversationalist" and aiType.lower() != "debatething":
            print("Error, that is not a valid AI type.")
            exit()
        if argutwo == "text":
            inputType = 2
else:
    print("No arguments found, please start with flags of either \"nogui\" or \"gui\"")
    exit()






aiTypeName = aiType

if aiType.lower() == "assistant":
    aiType = 1
    backstory = cnf.good + "\n" + cnf.instructs
    ao.voice_id = ao.set_voice("british")
elif aiType.lower() == "conversationalist":
    aiType = 2
    backstory = cnf.conversation + "\n"
    ao.voice_id = ao.set_voice("british")
elif aiType.lower() == "debatething":
    aiType = 3
    backstory = cnf.debatething + "\n"
    ao.voice_id = ao.set_voice("indian")
else:
    print("Invalid input type, killing program.")
    time.sleep(2)
    exit()


if aiType == 1:
    aiTitle = "AI"
elif aiType == 2 or aiType == 3:
    aiTitle = "Human 2"

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


def get_input():
    if inputType == 1:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.7)
            print("Waiting for speech....")
            audio = r.listen(source, timeout=None)
        try:
            user_input = r.recognize_google(audio, language="en-US")
        except sr.UnknownValueError:
            print("Could not understand audio")
            user_input = "*they mutter too quietly to hear*"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            user_input = "*unintelligible sounds come from human*"
        print("Human: " + user_input)
        return user_input
    elif inputType == 2:
        user_input = input("Human: ")
        return user_input


historyFile = f"{aiTypeName}history.txt"

# Save out
with open(historyFile, "a") as file:

        file.write("\n" + current_time + "NEW CONVO STARTED WITH AI TYPE " + aiTypeName + "\n")


history = []
while True:
    user_input = get_input()
    
    
    
    prompt = backstory + f"Human: {user_input}\n{aiTitle}:"

    response = generate_response(prompt, history)
    history.append(prompt)
    history.append(response)
    
    with open(historyFile, "a") as file:
        file.write("User: " + user_input + "\n")
        file.write("AI: " + response + "\n")
    
    pr.special_instructions(response)
    response = pr.clear_substrings(response)

    if aiType == 1:
        print("AI: " + response + "\n")    
    elif aiType == 2 or aiType == 3:
        print("Human 2: " + response + "\n")    
    
    ao.speak_response(response)
    playsound('recentoutput.mp3')
    os.remove("recentoutput.mp3")
    
    if "end of conversation" in response.lower():
        exit()
