import unittest
import os
from lucy import processar_comando
import speech_recognition as sr
import json  

class TestLucy(unittest.TestCase):
    def setUp(self):
        self.audio_files = [
            "Abrindo-Chrome.wav",
            "Chamando-Lucy.wav",
            "Chamando-outro-nome.wav",
            "Fechar-Discord.wav",
            "Pesquisar-no-Google.wav",
            "Pesquisar-no-sistema.wav",
        ]
        self.audio_path = "audio_files/" 

        
        with open("config.json", "r") as config_file:
            self.config = json.load(config_file)

    def test_processar_comando(self):
        for audio_file in self.audio_files:
            audio_path = os.path.join(self.audio_path, audio_file)
            with open(audio_path, "rb") as audio_file:
                audio_data = audio_file.read()

                try:
                    comando = processar_comando(audio_data, self.config)
                    self.assertTrue(comando, f"Comando não processado corretamente para {audio_file}")
                except sr.UnknownValueError:
                    self.fail(f"Nenhum comando detectado após processar áudio de {audio_file}")
                except sr.RequestError:
                    self.fail(f"Erro na solicitação ao processar áudio de {audio_file}")


if __name__ == "__main__":
    unittest.main(exit=False)
