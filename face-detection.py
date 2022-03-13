from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)  # Create Video Capture Object
detector = FaceDetector()  # Create detector instance

while True:
    success, img = cap.read()    # Get Image
    img, bboxs = detector.findFaces(img)   # Detect Face

    if bboxs:   # If boxes found, 
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
