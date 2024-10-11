import cv2

def setup_hsv_histogram(frame, region_of_interest):
    hsv_roi = cv2.cvtColor(region_of_interest, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, lower_bound, upper_bound)
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    return roi_hist
