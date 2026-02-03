# AI-Driven UI/UX Design System

## 📌 Project Overview
This project is an AI-powered decision support system designed to assist UI/UX designers. It addresses "choice paralysis" by using Machine Learning to predict optimal design elements (Layout, Fonts, and Color Palettes) based on the website category.

## 🚀 Features
- **Smart Predictions:** Uses 5 Random Forest classifiers to generate design systems.
- **Full Design System:** Recommends Layout, Font, Primary, Secondary, and Tertiary colors.
- **Interactive UI:** Built with **Flask** for a responsive web interface.
- **Visual Feedback:** Instantly renders the suggested color palette and typography.

## 🛠️ Tech Stack
- **Frontend/Backend:** Python (Flask), HTML/CSS
- **Machine Learning:** Scikit-Learn (Random Forest)
- **Data Processing:** Pandas, NumPy

## 📂 Project Structure
- `app1.py`: The main Flask application.
- `Train_model.py`: Script used to train the machine learning models.
- `models/`: Contains the 5 pre-trained .pkl model files.
- `templates/`: HTML files for the web interface.

## ⚙️ How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
