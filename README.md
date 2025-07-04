
# 📦 RealTime-AI-Object-Detection

🎯 A real-time AI-powered object detection app using **YOLOv5**, **OpenCV**, and a custom **Tkinter GUI**. This project allows users to detect and label objects through a live webcam feed with a clean, user-friendly interface.

---

## 🚀 Features

- 🧠 YOLOv5-based object detection (pre-trained on COCO dataset)
- 🎥 Real-time webcam capture
- 🔲 Bounding boxes with confidence scores
- 🖼️ Beautiful, modern GUI using Tkinter
- 🧩 Easy to extend and customize



## 🛠️ Tech Stack

- **Python 3.8+**
- **YOLOv5** (PyTorch-based)
- **OpenCV**
- **Tkinter**
- **Pillow**
- **NumPy**

---


## 🧠 How It Works

1. The GUI is built using Tkinter.
2. On clicking **Start Detection**, the webcam feed is captured using OpenCV.
3. YOLOv5 detects objects in each frame.
4. Bounding boxes and labels are drawn in real time.

---

## ✅ Sample Output

| Object Detected | Bounding Box | Label    | Confidence |
| --------------- | ------------ | -------- | ---------- |
| Person          | ✅            | `person` | 0.98       |
| Bottle          | ✅            | `bottle` | 0.91       |
| Chair           | ✅            | `chair`  | 0.87       |

---

## 🧩 Future Enhancements

* Deploy as desktop app using PyInstaller
* Add object filter dropdown (detect only "person", etc.)
* Save frames on detection
* FPS counter for performance

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 💡 Acknowledgments

* [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
* [OpenCV](https://opencv.org/)
* [PyTorch](https://pytorch.org/)

```

---

Would you like this `README.md` as a downloadable file or zipped with your full project folder?
```
