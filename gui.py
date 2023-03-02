import easygui
import audiooutput as ao


# Get AI type
aiChoices = ["Assistant", "Conversationalist", "DebateThing"]
aiChoice = easygui.buttonbox("Choose an AI type.", choices=aiChoices)

# Set the voice that each type is meant for
if aiChoice == "Assistant" or aiChoice == "Conversationalist":
   ao.voice_id = ao.set_voice("british")
elif aiChoice == "DebateThing":
   ao.voice_id = ao.set_voice("indian")

# Ask if the user wants to change the voice
inputChoices = ["Yes", "No"]
inputChoice = easygui.buttonbox("Do you want to override the default voice for your chosen AI?", choices=inputChoices)

# If yes, then get the wanted voice
if inputChoice == "Yes":
   voiceChoices = ["British", "Indian"]
   voiceChoice = easygui.buttonbox("Pick a voice.", choices=voiceChoices)
   if voiceChoice == "British":
      ao.voice_id = ao.set_voice("british")
   elif voiceChoice == "Indian":
      ao.voice_id = ao.set_voice("indian")
   

