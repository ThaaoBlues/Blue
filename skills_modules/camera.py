import numpy as np
import cv2




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

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

        return True, "J'ai fermé la sortie vidéo"

    except:
        return True, "Votre caméra est indisponible"