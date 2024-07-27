import detect_voice
import threading

prediction = [None]
mic = detect_voice.init(prediction)

def thread():
    oldPrediction = None
    with mic:
        while True:
            detect_voice.mic_record(mic)
            if(prediction[0] != oldPrediction):
                print(prediction[0])
                oldPrediction = prediction[0]

voice_thread = threading.Thread(target=thread, args=() ,daemon=True)
voice_thread.start()
  