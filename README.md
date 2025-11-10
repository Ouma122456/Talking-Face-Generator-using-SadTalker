# 🎥 Talking Face Generator using SadTalker

Generate realistic **talking videos** from a **single image** and **text or audio input** using deep learning.  
This project is powered by **[SadTalker (CVPR 2023)](https://github.com/Winfredy/SadTalker)** — a state-of-the-art talking face generation framework.

---

## 🧠 Overview

The **Talking Face Generator** allows users to:
- 🖼️ Upload or select an image  
- 🗣️ Write text or upload an audio file  
- 🎬 Automatically generate a video where the person in the image speaks the text with realistic facial animation  

It uses advanced deep learning models to generate smooth and expressive facial movements synchronized with speech.

---

## 🚀 Features

✅ Text-to-Speech (TTS) or custom audio input  
✅ Realistic lip-sync and facial motion using 3D face coefficients  
✅ Image enhancement using **GFPGAN** or **RestoreFormer**  
✅ Adjustable animation parameters (pose, expression, smoothness)  
✅ Intuitive **Gradio** web interface  
✅ Video export in `.mp4` format  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Interface | Gradio |
| Deep Learning | PyTorch |
| Animation Model | SadTalker |
| Text-to-Speech | Coqui TTS |
| Image Enhancement | GFPGAN / RestoreFormer |
| Language | Python |
