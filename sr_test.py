import module_speechrecognition as sr
from naoqi import ALProxy
 
sr.main()

SpeechRecognition = ALProxy("SpeechRecognition")
SpeechRecognition.start()
SpeechRecognition.setLanguage("de-de")
SpeechRecognition.calibrate()
SpeechRecognition.enableAutoDetection()

memory = naoqi.ALProxy("ALMemory")
memory.subscribeToEvent("SpeechRecognition", self.getName(), "processRemote")

def processRemote(self, signalName, message):
    # Do something with the received speech recognition result
    print(message)

print("hello")
