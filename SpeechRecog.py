import time
from naoqi import ALProxy

class ASRModule:
    # Variables
    def __init__(self, robotIP):
        self.ROBOT_IP = robotIP

        asr = ALProxy("ALSpeechRecognition", self.ROBOT_IP, 9559)

        asr.setLanguage("English")

        vocabulary = []  
        with open('english3.txt', 'r') as file:
            for line in file:
                word = line.strip() 
                vocabulary.append(word) 
        
        asr.setVocabulary(vocabulary, True)

        self.asr = asr

    # Methods
    def listen(self, asr, duration):
        # Start the speech recognition engine with user Test_ASR
        asr.subscribe("Test_ASR")
        print('Speech recognition engine started')
        time.sleep(duration)
        asr.unsubscribe("Test_ASR")

        return asr.WordRecognized