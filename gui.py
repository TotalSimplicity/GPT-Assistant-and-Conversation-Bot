import easygui
import audiooutput as ao


# Get AI type
aiChoices = ["Assistant", "Conversationalist", "DebateThing"]
aiChoice = easygui.buttonbox("Choose an AI type.", choices=aiChoices)

# Set the voice that each type is meant for
if aiChoice == "Assistant" or aiChoice == "Conversationalist":
   ao.set_voice("british")
elif aiChoice == "DebateThing":
   ao.set_voice("indian")

# Ask if the user wants to change the voice
inputChoices = ["Yes", "No"]
inputChoice = easygui.ynbox("Do you want to override the default voice for your chosen AI?", choices=inputChoices)

# If yes, then get the wanted voice
if inputChoice == "Yes":
   voiceChoices = ["British", "Indian"]
   voiceChoice = easygui.buttonbox("Do you want to override the default voice for your chosen AI?", choices=inputChoices)
   if voiceChoice == "British":
      ao.set_voice("british")
   elif voiceChoice == "Indian":
      ao.set_voice("indian")
      
 finalMessage = r"Starting {aiChoice}......"

# Display the user's answers
easygui.msgbox(finalMessage, ok_button="Start")

