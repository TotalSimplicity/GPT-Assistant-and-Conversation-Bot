import easygui
import audiooutput as ao


# Ask for the user's favorite color
aiChoices = ["Assistant", "Conversationalist", "DebateThing"]
aiChoice = easygui.buttonbox("Choose an AI type.", choices=aiChoices)


if aiChoice == "Assistant" or aiChoice == "Conversationalist":
   ao.set_voice("british")
elif aiChoice == "DebateThing":
   ao.set_voice("indian")

inputChoices = ["Yes", "No"]
inputChoice = easygui.ynbox("Do you want to override the default voice for your chosen AI?", choices=inputChoices)

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

