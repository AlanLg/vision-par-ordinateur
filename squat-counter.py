import cv2
import mediapipe as mp
import numpy as np
from mediapipe.python.solutions.drawing_utils import BLACK_COLOR

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

def initialize_pose():
    return mp_pose.Pose()

def process_frame(frame, pose):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)
    return results

def draw_landmarks(frame, results):
    mp_drawing.draw_landmarks(
        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
    )

def detect_squat(results, counter, has_done_squat):
    landmarks = results.pose_landmarks.landmark

    if not results.pose_landmarks:
        return counter, has_done_squat

    left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]

    if left_knee.visibility > 0.9 and left_hip.visibility > 0.9:
        if left_knee.y > left_hip.y and not has_done_squat:
            counter += 1
            has_done_squat = True

        elif has_done_squat and left_knee.y < left_hip.y:
            has_done_squat = False
            print("Reset: has_done_squat")

    return counter, has_done_squat

def display_counter(frame, counter, gradient_step):
    text = f"Squat : {counter}"

    frame_height, frame_width, _ = frame.shape

    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.1, 2)[0]
    text_width = text_size[0]
    text_height = text_size[1]

    text_x = (frame_width - text_width) // 2
    text_y = frame_height - text_height - 20

    gradient_color = (
        int(128 + 127 * np.sin(gradient_step)),
        int(128 + 127 * np.sin(gradient_step + 2)),
        int(128 + 127 * np.sin(gradient_step + 4)),
    )

    cv2.putText(
        frame,
        text,
        (text_x, text_y),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.1,
        gradient_color,
        2,
        cv2.LINE_AA
    )

def main():
    pose = initialize_pose()
    cap = cv2.VideoCapture(0)
    counter = 0
    has_done_squat = False

    gradient_step = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        results = process_frame(frame, pose)

        if results.pose_landmarks:
            counter, has_done_squat = detect_squat(results, counter, has_done_squat)
            display_counter(frame, counter, gradient_step)
            draw_landmarks(frame, results)

        gradient_step += 0.1

        cv2.imshow("MediaPipe Pose", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
