import cv2

def main():
    # Title of the project
    print("Project: Edge Detection using DIP Concepts")

    # Open the default webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    print("Press 's' to save the current edge-detected frame.")
    print("Press 'q' to quit.")

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Canny Edge Detection
        edges = cv2.Canny(blurred, 100, 200)

        # Display the edge-detected frame
        cv2.imshow('Edge Detection - Live Feed', edges)

        # Handle key events
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            cv2.imwrite('edge_output.png', edges)
            print("Saved edge-detected image as 'edge_output.png'")
        elif key == ord('q'):
            print("Exiting...")
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
