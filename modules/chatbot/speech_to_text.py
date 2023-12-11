import whisper
from openai import OpenAI

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

from configurations.config import OPENAI_API_KEY

class S2T_with_whisper():
    def __init__(self,):
        self.model = whisper.load_model("base")
        
    def transcribe(self, audio_file,):
        result = self.model.transcribe(audio_file)
        return result["text"]
    
class S2T_with_openai():
    def __init__(self,):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.translate_model = self.client.audio.translations
        self.model = "whisper-1"
    
    def transcribe(self, audio_file,):
        if type(audio_file) == str:
            audio_file = open(audio_file, "rb")
            
        transcript = self.translate_model.create(
          model=self.model, 
          file=audio_file
        )   
        return transcript.text
        