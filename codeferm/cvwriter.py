import cv2
import numpy as np

def track_object(video_path):
    cap = cv2.VideoCapture(video_path)
    # Initialization of tracking parameters
    # Camshift algorithm setup and tracking loop

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Perform tracking and display result
        cv2.imshow('Object Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    track_object('data/sample_video.mp4')
