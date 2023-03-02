import easygui
import audiooutput as ao

# Ask for the user's favorite color
aiChoices = ["Assistant", "Conversationalist", "DebateThing"]
aiChoice = easygui.buttonbox("Choose an AI type.", choices=aiChoices)

if aiChoice == "Assistant" or aiChoice == "Conversationalist":
   ao.setvoice

# Ask the user if they like pizza
#inputChoices = ["Yes", "No"]
#inputChoice = easygui.ynbox("Do you want to start in debug mode(Text input as opposed to voice input)?", choices=inputChoices)

 # Display the user's answers
easygui.msgbox("Settings set", ok_button="Start")

