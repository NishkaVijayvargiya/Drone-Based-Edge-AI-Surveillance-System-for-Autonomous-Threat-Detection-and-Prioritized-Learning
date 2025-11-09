import cv2
import numpy as np
import os
import platform
from datetime import datetime

# --------- Helper: play beep sound ----------
def play_alert_sound():
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.Beep(1000, 300)  # frequency=1000Hz, duration=300ms
    else:
        # Works on Ubuntu / WSL (requires 'sox' package)
        os.system('play -nq -t alsa synth 0.3 sine 1000 2>/dev/null || echo -e "\a"')

# --------- Setup log file ----------
log_file = "alerts_log.txt"
with open(log_file, "w") as f:
    f.write("=== Warzone Object Tracking Log ===\n")
    f.write(f"Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("--------------------------------------------------\n")
    f.write("Time\t\t\tFrame\tPriority\tDetails\n")
    f.write("--------------------------------------------------\n")

# --------- Video Setup ----------
video_path = "demo_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Could not open video. Make sure demo_video.mp4 is in the project root.")
    exit()

output_width, output_height = 960, 540
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0 or np.isnan(fps):
    fps = 30.0

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("warzone_output.mp4", fourcc, fps, (output_width, output_height))

print("🎬 Recording started: warzone_output.mp4")

# Motion detector
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    frame = cv2.resize(frame, (output_width, output_height))
    fgmask = fgbg.apply(frame)
    fgmask = cv2.medianBlur(fgmask, 5)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        area = w * h

        # Priority logic
        if area > 10000:
            priority = "HIGH"
            color = (0, 0, 255)
            play_alert_sound()
        elif area > 3000:
            priority = "MEDIUM"
            color = (0, 255, 255)
        else:
            priority = "LOW"
            color = (0, 255, 0)

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, f"Priority: {priority}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Log entry
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_line = f"{timestamp}\t{frame_count}\t{priority}\tObject area={area}\n"
        with open(log_file, "a") as f:
            f.write(log_line)

        print(f"🚨 Movement detected at frame {frame_count} (Priority: {priority})")

    out.write(frame)
    cv2.imshow("Warzone Demo", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("\n✅ Demo complete. Saved processed video as warzone_output.mp4")
print(f"🗒️ All detections logged in: {log_file}")

