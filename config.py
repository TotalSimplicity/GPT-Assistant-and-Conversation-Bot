import os
from dotenv import load_dotenv
load_dotenv(".env")

api = os.getenv('OPENAI-APIKEY')

#spotify bot info
spotify_client_id = os.getenv('spotify_client_id')
spotify_client_secret = os.getenv('spotify_client_secret')

#aws tts info
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_key = os.getenv('aws_secret_key')

good_file = open("goodpersonality.txt", "r")
good = good_file.read()
good_file.close()

instructs_file = open("instructs.txt", "r")
instructs = instructs_file.read()
instructs_file.close()

conversation_file = open("midpersonality.txt", "r")
conversation = conversation_file.read()
conversation_file.close()

debate_file = open("debatething.txt", "r")
debatething = debate_file.read()
debate_file.close()