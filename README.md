# Face Recognition System (Python + OpenCV + Tkinter)

This project is a simple **Face Capture and Viewer Application** built using **Python**, **OpenCV**, and **Tkinter**.
It allows the user to **capture their face using a webcam**, save the image under their name, and **view previously stored faces** from within the application.

---

## Features

- GUI interface built with **Tkinter**
- Automatically **detects face** using Haar Cascade
- Saves captured face images with **user-entered names**
- **10-second capture timer** for convenience
- View all previously saved images directly in the app
- All images stored inside `faces/` folder

---

## Requirements

Install the required libraries before running:

```bash
pip install opencv-python pillow
sudo apt-get install python3-tk
```
## How to run 
1. Download or Clone the Repository
git clone https://github.com/YourUserName/YourRepoName.git
cd YourRepoName
2. Run the Application
python face_recognition_system.py

## Project Structure
📂 Project Folder
│
├── face_recognition_system.py      # Main Application Code
├── faces/                          # Auto-created folder storing face images
└── README.md                       # Documentation File

## Technologies Used
GUI:-Tkinter
Face Detection:-	OpenCV (Haar Cascade)
Image Processing:-	PIL (Pillow)
Language:-	Python 3.x

## Future Improvements (Optional)

Implement actual Face Recognition (LBPH / CNN Model)

Store multiple face images per user

Add Database support for user records

Add Delete / Manage Saved Images feature

Enhance GUI styling for a smoother user experience
2. Run the Application
python face_recognition_system.py
