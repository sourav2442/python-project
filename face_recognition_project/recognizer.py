import os
import cv2
import face_recognition
import numpy as np
from datetime import datetime

IMAGE_DIR = 'images'
CSV_FILE = 'attendance.csv'
os.makedirs(IMAGE_DIR, exist_ok=True)

def capture_face(name):
    cam = cv2.VideoCapture(0)
    print("📸 Press SPACE to capture face or ESC to cancel.")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Capture Face", frame)
        key = cv2.waitKey(1)
        if key % 256 == 27:  # ESC
            break
        elif key % 256 == 32:  # SPACE
            path = os.path.join(IMAGE_DIR, f"{name}.jpg")
            cv2.imwrite(path, frame)
            print(f"✅ Saved: {path}")
            break

    cam.release()
    cv2.destroyAllWindows()

def load_faces():
    known_encodings = []
    known_names = []
    faces_dir = "faces"
    
    # Create folder if it doesn't exist
    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)
        print(f"📂 Created missing folder: {faces_dir}")
        return [], []

    for filename in os.listdir(faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(faces_dir, filename)
            image = cv2.imread(image_path)
            
            if image is None:
                print(f"⚠️ Skipping {filename}: Image not found or unreadable.")
                continue

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            face_encs = face_recognition.face_encodings(image)

            if face_encs:
                known_encodings.append(face_encs[0])
                known_names.append(os.path.splitext(filename)[0])
            else:
                print(f"⚠️ No face found in {filename}. Skipping.")
    
    return known_encodings, known_names


def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w') as f:
            f.write("Name,Date,Time\n")

    with open(CSV_FILE, 'r+') as f:
        lines = f.readlines()
        already_marked = any(line.startswith(name) and date in line for line in lines)
        if not already_marked:
            f.write(f"{name},{date},{time}\n")
            print(f"📌 Attendance marked for {name} at {time}")
        else:
            print(f"ℹ️ {name} already marked today.")

def recognize_faces():
    images, known_encodings, known_names = load_faces()
    if not known_encodings:
        print("⚠️ No registered faces found.")
        return

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("❌ Error: Could not access the camera.")
        return

    print("🔍 Press ESC to stop recognition.")
    
    while True:
        ret, frame = cam.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find faces and their encodings
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            if len(face_distances) > 0:
                best_match_index = face_distances.argmin()
                if matches[best_match_index]:
                    name = known_names[best_match_index]
                    mark_attendance(name)  # Mark attendance when a known face is recognized

            # Scale back up face locations
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw box and label
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        cv2.imshow("Face Recognition", frame)
        # The following block is misplaced and redundant, as attendance marking and drawing are already handled above.
        # If you want to mark attendance when a known face is recognized, do it inside the face loop:
        # (Move this logic inside the for loop above, after name is determined)
        
        # ESC to quit
        if cv2.waitKey(1) & 0xFF == 27:
            break
            break
    cam.release()
    cv2.destroyAllWindows()

def delete_user(name):
    path = os.path.join(IMAGE_DIR, f"{name}.jpg")
    if os.path.exists(path):
        os.remove(path)
        print(f"🗑️ Deleted user: {name}")
    else:
        print("❌ User not found.")

def main():
    while True:
        print("\n===== Face Recognition Attendance System =====")
        print("1. Register New Face")
        print("2. Start Recognition")
        print("3. Delete User")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            capture_face(name)
        elif choice == '2':
            recognize_faces()
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_user(name)
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()