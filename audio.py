# import speech_recognition as sr

# from os import path
# # def printWAV(FILE_NAME, pos, clip):
# FILE_NAME = "static/Break Bad Habits.wav"
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), FILE_NAME)

# r = sr.Recognizer()

# time = 0 # position in track
# dur = 10 # clip length to process each iteration

# with sr.AudioFile(AUDIO_FILE) as source:
#     while time < source.DURATION:
#         audio = r.record(source, duration=dur, offset=time)  # read the audio file 1 clip at a time
#         # recognize speech using Google Speech Recognition
        
#         try:
#             # for testing purposes, we're just using the default API key
#             # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#             # instead of `r.recognize_google(audio)`
#             print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print("Could not request results from Google Speech Recognition service; {0}".format(e))

import speech_recognition as sr
from os import path
                
def printWAV(FILE_NAME, pos, clip):
    # use the audio file as the audio source
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), 'static/'+FILE_NAME)
    r = sr.Recognizer()
    text = ""
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source, duration=clip, offset=pos)
        # recognize speech using Google Speech Recognition
        try:
            text += r.recognize_google(audio) + "\n"
        except sr.UnknownValueError:
            text += "Could not understand audio\n"
        except sr.RequestError as e:
            text += "Could not request results; {0}".format(e)+ "\n"
    return text