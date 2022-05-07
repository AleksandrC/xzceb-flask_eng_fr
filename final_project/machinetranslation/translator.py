'''translation module'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)



def english_to_french(english_text):
    '''translate English to French'''
    language_translator.set_service_url(url)

    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    json.dumps(translation, indent=2, ensure_ascii=False)
    french_text = translation['translations'][0]['translation']
    return french_text

#print(english_to_french('City'))
#print(english_to_french('Road'))
#print(english_to_french('Wolves are running to the dinner'))

def french_to_english(french_text):
    '''translate French to English'''
    language_translator.set_service_url(url)

    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    json.dumps(translation, indent=2, ensure_ascii=False)
    #print(translation['translations'][0]['translation'])
    english_text = translation['translations'][0]['translation']
    return english_text

#print(french_to_english('Ville'))
#print(french_to_english('Route'))
#print(french_to_english('Ça va pas changer le monde'))