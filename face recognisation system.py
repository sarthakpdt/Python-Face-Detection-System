import cv2
import os
import time
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class FaceRecognitionSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition System")
        self.master.geometry("600x400")
        self.master.config(bg="#f0f0f0")
        self.data_path = 'faces'
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.master, bg="#f0f0f0")
        frame.pack(expand=True, fill="both")

        title_label = tk.Label(frame, text="Face Recognition System", font=("Helvetica", 20, "bold"), fg="black", bg="#f0f0f0")
        title_label.pack(pady=10)

        button_frame = tk.Frame(frame, bg="#f0f0f0")
        button_frame.pack(expand=True, fill="both", padx=20)

        self.capture_button = tk.Button(button_frame, text="Capture My Picture", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10, relief="raised", borderwidth=3, command=self.capture_face)
        self.capture_button.pack(side="left", expand=True, padx=20, pady=20)

        self.view_button = tk.Button(button_frame, text="See Previous Images", font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white", padx=20, pady=10, relief="raised", borderwidth=3, command=self.view_saved_faces)
        self.view_button.pack(side="right", expand=True, padx=20, pady=20)

    def capture_face(self):
        name = simpledialog.askstring("Input", "Enter your name:")
        if name:
            cap = cv2.VideoCapture(0)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            start_time = time.time()

            while True:
                ret, frame = cap.read()
                elapsed_time = time.time() - start_time

                cv2.putText(frame, f"Capturing in: {int(10 - elapsed_time)}s", (200, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

                if elapsed_time >= 10:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                    for (x, y, w, h) in faces:
                        scale_factor = 1.5
                        new_w = int(w * scale_factor)
                        new_h = int(h * scale_factor)

                        new_x = max(0, x - (new_w - w) // 2)
                        new_y = max(0, y - (new_h - h) // 2)

                        new_x_end = min(frame.shape[1], new_x + new_w)
                        new_y_end = min(frame.shape[0], new_y + new_h)

                        face_img = frame[new_y:new_y_end, new_x:new_x_end]
                        file_path = os.path.join(self.data_path, f"{name}.jpg")
                        cv2.imwrite(file_path, face_img)
                        messagebox.showinfo("Success", f"Image saved as {name}.jpg!")
                        cap.release()
                        cv2.destroyAllWindows()
                        return

                cv2.imshow('Capturing Face', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

    def view_saved_faces(self):
        top = tk.Toplevel(self.master)
        top.title("Saved Faces")
        top.geometry("300x300")
        top.config(bg="#f0f0f0")

        files = [f for f in os.listdir(self.data_path) if f.endswith(".jpg")]
        if not files:
            messagebox.showinfo("No Images", "No images found!")
            return

        listbox = tk.Listbox(top, font=("Helvetica", 12))
        listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        for file in files:
            listbox.insert(tk.END, file[:-4])

        def show_selected_image():
            selected_name = listbox.get(tk.ACTIVE)
            if selected_name:
                self.display_image(selected_name)

        btn = ttk.Button(top, text="Show Image", command=show_selected_image)
        btn.pack(pady=10)

    def display_image(self, name):
        image_path = os.path.join(self.data_path, f"{name}.jpg")
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((400, 400), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            top = tk.Toplevel(self.master)
            top.title(name)
            top.geometry("450x450")
            top.config(bg="#f0f0f0")

            label = tk.Label(top, image=img_tk)
            label.image = img_tk
            label.pack(pady=20)
        else:
            messagebox.showerror("Error", "Image not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()