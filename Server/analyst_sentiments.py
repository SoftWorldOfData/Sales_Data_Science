from pysentimiento import create_analyzer
from main import Dataset_Copy
from deep_translator import GoogleTranslator

def Translator():
        
        translator = GoogleTranslator(source='auto', target='es')
        
        Translate = []

        # Divide el texto largo en fragmentos de 5000 caracteres o menos
        fragmentos = [Dataset_Copy["review_content"][i:i+5000] for i in range(0, len(Dataset_Copy["review_content"]), 4900)]

        for text in fragmentos:

            translated_text = translator.translate(fragmentos)
            
            Translate.append(translated_text)

            print(Translate)

        Dataset_Translator = GoogleTranslator(source="auto", target="es").translate(Dataset_Copy["review_content"])

        print(Dataset_Translator)

def main():

    analyzer = create_analyzer(task="sentiment", lang="es")

Translator()