import cv2

def start_video_stream(video_source=0):
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print("Error: Cannot open video source")
        return None
    return cap
