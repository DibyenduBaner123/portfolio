import cv2
import numpy as np
import pyautogui

# Set up screen resolution and output file
screen_size = pyautogui.size()
output_file = 'screen_recording.avi'

# Define the codec and create a VideoWriter object to save the recording
codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0  # Frames per second
out = cv2.VideoWriter(output_file, codec, fps, screen_size)

try:
    print("Recording... Press Ctrl+C to stop.")
    while True:
        # Capture the screen
        img = pyautogui.screenshot()
        frame = np.array(img)  # Convert to numpy array
        
        # Convert colors from RGB to BGR (OpenCV uses BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Write the frame to the video file
        out.write(frame)

        # Display the recording live (optional)
        cv2.imshow("Recording", frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Recording stopped by user.")

finally:
    # Release resources
    out.release()
    cv2.destroyAllWindows()
