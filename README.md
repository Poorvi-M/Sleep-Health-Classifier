# Sleep Health Classifier

A machine learning-based web application that predicts sleep health status using lifestyle, physiological, and behavioral inputs. The project demonstrates a complete ML pipeline from preprocessing to deployment using Streamlit.

---

## Project Overview

Sleep health is influenced by multiple factors such as stress, activity levels, and heart rate. This project builds a classification model to analyze these factors and predict sleep health categories.

### Key Capabilities
- Accepts user input via an interactive UI  
- Processes real-world health-related features  
- Predicts sleep health category using a trained ML model  
- Provides quick and intuitive results  

---

## Features

- End-to-end ML pipeline  
- Data preprocessing & feature engineering  
- Model training and evaluation  
- Streamlit-based interactive UI  
- Real-time prediction system  

---

## Tech Stack

- **Language:** Python  
- **Libraries:**  
  - pandas  
  - numpy  
  - scikit-learn  
  - xgboost (optional)  
- **Frontend/UI:** Streamlit  
- **Tools:** Git, GitHub

  ---

## Installation & Setup + Run (One Shot)

Copy and run EVERYTHING below in your terminal:

```bash
# clone repository
git clone https://github.com/Poorvi-M/Sleep-Health-Classifier.git
cd Sleep-Health-Classifier

# create virtual environment
python -m venv venv

# activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# upgrade pip (recommended)
python -m pip install --upgrade pip

# install dependencies
pip install -r requirements.txt

# run the application
streamlit run app.py
```
---
## Run on Localhost

After running the above command, open:

http://localhost:8501
or Network URL shown in terminal
