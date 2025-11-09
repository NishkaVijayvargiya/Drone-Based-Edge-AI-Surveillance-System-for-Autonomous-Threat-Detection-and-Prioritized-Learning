import cv2
import numpy as np
import streamlit as st
from datetime import datetime

# ---- PAGE SETUP ----
st.set_page_config(page_title="Warzone Drone Dashboard", layout="wide")
st.title("🚁 Warzone Object Tracking and Priority Detection Dashboard")

# ---- VIDEO SETUP ----
video_path = "demo_video.mp4"
cap = cv2.VideoCapture(video_path)
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)

output_width, output_height = 640, 360

# ---- METRICS PLACEHOLDERS ----
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_placeholder = st.metric("Total Detections", 0)
with col2:
    low_placeholder = st.metric("Low Priority", 0)
with col3:
    med_placeholder = st.metric("Medium Priority", 0)
with col4:
    high_placeholder = st.metric("High Priority", 0)

chart_placeholder = st.empty()
video_placeholder = st.empty()
log_placeholder = st.empty()

# ---- COUNTERS ----
low, medium, high, total = 0, 0, 0, 0
frame_window = st.empty()

# ---- PROCESS VIDEO ----
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (output_width, output_height))
    fgmask = fgbg.apply(frame)
    fgmask = cv2.medianBlur(fgmask, 5)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        area = w * h

        if area > 10000:
            priority = "HIGH"
            color = (0, 0, 255)
            high += 1
        elif area > 3000:
            priority = "MEDIUM"
            color = (0, 255, 255)
            medium += 1
        else:
            priority = "LOW"
            color = (0, 255, 0)
            low += 1

        total += 1
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, priority, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Convert frame to RGB for Streamlit
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

    # Update metrics
    total_placeholder.metric("Total Detections", total)
    low_placeholder.metric("Low Priority", low)
    med_placeholder.metric("Medium Priority", medium)
    high_placeholder.metric("High Priority", high)

    # Live chart
    chart_placeholder.bar_chart(
        {"Low": [low], "Medium": [medium], "High": [high]}
    )

cap.release()
st.success("✅ Simulation Complete")
