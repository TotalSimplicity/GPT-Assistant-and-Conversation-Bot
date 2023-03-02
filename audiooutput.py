import os
import boto3 as b3
import config as cnf

voice_id = "undefined"
os.environ['AWS_ACCESS_KEY_ID'] = cnf.aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = cnf.aws_secret_key
# Create a client for the Amazon Polly service
polly = b3.client('polly', region_name='us-east-1')

def set_voice(voice):
    if voice == "british":
        voice_id = 'Arthur'
    elif voice == "indian":
        voice_id = 'Kajal'
    return voice_id

def speak_response(response):
    # Generate the speech using Amazon Polly
    response = polly.synthesize_speech(Text=response, OutputFormat='mp3', VoiceId=voice_id, Engine="neural")
    # Save the speech as an audio file
    with open('recentoutput.mp3', 'wb') as f:
        f.write(response['AudioStream'].read())


