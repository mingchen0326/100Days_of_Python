import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-01-13', authenticator=authenticator)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    frenchText = language_translator.translate(englishText, source="en", target="fr")
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(frenchText, source="fr", target="en")
    return englishText

eng_text = "Hello"
print(englishToFrench(eng_text))