import cv2
from time import sleep
from util.res import speak
from random import sample
from string import digits, ascii_lowercase
from os import mkdir, path

def initialize(voice_command,sentences):
    try:
        cap = cv2.VideoCapture(0)

        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()


            # Display the resulting frame
            cv2.imshow('Caméra output',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            """
            for i in range(3,0,-1):
                speak(str(i))
                sleep(1)
            """ 
                
            if not path.exists("images"):
                mkdir("images")
            
            filename = "".join(sample(digits+ascii_lowercase,16))+".jpg"
            cv2.imwrite(f"images/{filename}",frame)


            break       

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

        return True, "La photo est maintenant disponible dans la page images de mon server web !"


    except Exception as e:
        print(e)
        return True, "Votre caméra est indisponible"