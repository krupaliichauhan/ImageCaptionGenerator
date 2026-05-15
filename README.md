# ImageCaptionGenerator
Generates the caption for your image.

<b>Image Caption Generator</b><br>
--> An end-to-end deep learning project that generates meaningful captions for images using computer vision and natural language processing.

# 🧠 Image Caption Generator

An AI-powered Image Caption Generator built using Deep Learning, Computer Vision, and Natural Language Processing.

This project uses a pretrained CNN model for image feature extraction and an LSTM-based decoder to generate captions for images automatically.

---

# 🚀 Features

- Upload image and generate captions
- CNN-based feature extraction
- NLP text preprocessing
- LSTM caption generation
- End-to-end deep learning pipeline

---

# 🛠️ Tech Stack

## Programming Language
- Python

## Libraries & Frameworks
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Pillow

## Deep Learning Models
- InceptionV3 (CNN Encoder)
- LSTM (Caption Decoder)

## Tools
- Jupyter Notebook
- Git & GitHub

---

# 🧠 Project Architecture

Image → CNN Feature Extractor → Feature Vector → LSTM Decoder → Caption Generation

---

# 📂 Project Structure

```bash
ImageCaptionGenerator/
│
├── app/
├── data/
│   ├── Images/
│   └── captions.txt
│
├── models/
│   ├── features.pkl
│   ├── tokenizer.pkl
│   └── image_caption_model.keras
│
├── notebooks/
│   └── image_caption_generator.ipynb
│
├── utils/
├── README.md
├── requirements.txt
└── .gitignore
--------------------------

📊 Dataset

Dataset Used:
    Flickr8k Dataset

Contains:
    8000 images
    Multiple captions per image
--------------------------

⚙️ Workflow

1) Load image dataset
2) Extract image features using InceptionV3
3) Clean and preprocess captions
4) Convert text into sequences
5) Train LSTM model
6) Generate captions for unseen images
--------------------------

🧪 Model Output

Feature Vector Shape: (1, 2048)
Vocabulary Size: 8781
Maximum Caption Length: 37
--------------------------

🚀 Future Improvements

Attention Mechanism
Transformer-based captioning
Beam Search decoding
Better UI using Flask/React
Deployment on AWS

--------------------------
👩‍💻 Author

Krupali Chauhan
Aspiring AI Engineer | Web Developer | AI & Cloud Enthusiast
--------------------------
⭐ If You Like This Project
Give this repository a star ⭐