import cv2
import mediapipe as mp

def main():
    mp_hands = mp.solutions.hands  # Load the MediaPipe Hands module
    mp_drawing = mp.solutions.drawing_utils  # Utility to draw landmarks
    
    # Initialize the hand tracking model
    hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    
    cap = cv2.VideoCapture(0)  # Start webcam capture
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)  # Mirror the frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for MediaPipe
        
        result = hands.process(rgb_frame)  # Process the frame for hand landmarks
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),  # Red color for landmarks
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=1)  # Red color for connections
                )
        
        cv2.imshow('Hand Tracking', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    hands.close()

if __name__ == "__main__":
    main()
