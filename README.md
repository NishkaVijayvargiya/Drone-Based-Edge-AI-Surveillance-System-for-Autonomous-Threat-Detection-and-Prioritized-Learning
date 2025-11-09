# 🚁 Drone-Based Edge AI Surveillance System for Autonomous Threat Detection and Prioritized Learning

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.10-success.svg)](https://opencv.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live%20Dashboard-red.svg)](https://streamlit.io/)
[![AirSim](https://img.shields.io/badge/AirSim-Drone%20Simulation-lightgrey.svg)](https://microsoft.github.io/AirSim/)
[![Dependencies](https://img.shields.io/badge/Dependencies-requirements.txt-blue)](./requirements.txt)

---

## 📖 Project Overview

This project presents an **AI-powered warzone surveillance system** that uses **drone-based simulation** to automatically **detect, classify, and prioritize movement** in real time.  
It combines **Microsoft AirSim** and **Unreal Engine 5** for environment simulation, and **Python (OpenCV + Streamlit)** for computer vision and monitoring.

Developed as a **capstone project**, it demonstrates how **Edge AI** can support **autonomous threat detection** and **situational awareness** in critical environments.

---

## 🧠 Key Features

✅ Realistic **drone simulation** using AirSim and Unreal Engine  
✅ Real-time **motion detection and object tracking** with OpenCV  
✅ **Priority classification** of movements (Low / Medium / High)  
✅ Automatic **alert logging** with timestamps  
✅ **Streamlit dashboard** for live web-based visualization  
✅ Modular and extensible architecture for real or simulated drone feeds

---

## 🏗️ System Architecture

Unreal Engine Environment
│
▼
AirSim Drone Feed
│
▼
OpenCV Processing
(Motion Detection + Classification)
│
├── warzone_output.mp4 → Processed Output Video
├── alerts_log.txt → Alert Log File
└── Streamlit Dashboard → Real-Time Visualization


---

## 🔬 Classification Logic

| Motion Area (pixels) | Classification | Description |
|----------------------|----------------|--------------|
| `< 3000` | 🟢 **Low** | Small movements (wind, leaves, shadows) |
| `3000–10000` | 🟡 **Medium** | Noticeable motion (human or vehicle) |
| `> 10000` | 🔴 **High** | Large or fast-moving entities |

---

## 📦 Project Structure



object_tracking_via_simulation/
│
├── capstone_extensions/
│ ├── demo_runner.py # Main detection pipeline
│ ├── live_dashboard.py # Terminal-based live dashboard
│ └── warzone_dashboard.py # Streamlit-based web dashboard
│
├── helper_functions.py # Plotting and calculation utilities
├── tracker_w_vector.py # Base image tracking module
├── location_tracker.py # AirSim location tracker
│
├── demo_video.mp4 # Input drone feed (replaceable)
├── warzone_output.mp4 # Processed video output
├── alerts_log.txt # Log of detections and priorities
│
├── settings/settings.json # AirSim configuration file
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/NishkaVijayvargiya/Drone-Based-Edge-AI-Surveillance-System-for-Autonomous-Threat-Detection-and-Prioritized-Learning.git
cd Drone-Based-Edge-AI-Surveillance-System-for-Autonomous-Threat-Detection-and-Prioritized-Learning

2️⃣ Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Project
Demo Mode (video input)

Run object detection and motion tracking on a demo video:

python capstone_extensions/demo_runner.py

Streamlit Web Dashboard

Launch an interactive web interface:

streamlit run capstone_extensions/warzone_dashboard.py

Console Dashboard

Terminal-based live updates (for quick tests):

python capstone_extensions/live_dashboard.py

```

📊 Outputs

Processed Video: warzone_output.mp4 (shows bounding boxes + labels)

Log File: alerts_log.txt (timestamped movement records)

Dashboard: Live stats + real-time visualization of detection results

Example log output:

[14:23:12] Movement detected - Priority: HIGH
[14:23:19] Movement detected - Priority: LOW

📈 Results

✅ Motion detection accuracy demonstrated on simulated drone footage
✅ Priority-based movement classification functioning in real-time
✅ Streamlit dashboard for operational visualization
✅ Scalable design for real drone feeds or defense simulations

🧩 Future Enhancements

🔹 Integrate YOLOv8 or Detectron2 for object-specific recognition

🔹 Enable multi-drone coordination using AirSim APIs

🔹 Extend to edge deployment for live field inference

🔹 Integrate audio and GPS-based tracking for advanced surveillance

📚 References

Microsoft AirSim Documentation

Unreal Engine Marketplace Assets

OpenCV Official Docs

Streamlit Documentation

👩‍💻 Author

Nishka Vijayvargiya
🎓 Capstone Project — Edge AI & Vision Systems
