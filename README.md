# 💰 Uncovering the Invisible: ML-Based Early Detection of Online Money Laundering

> A Machine Learning-powered solution for detecting suspicious online banking activity by analyzing cybercrime reports and banking data.

---

## 🚀 Project Overview

Online money laundering poses a significant threat to financial systems and digital ecosystems. This project presents a machine learning-based system that can identify potentially fraudulent bank accounts by analyzing cyber crime reports in conjunction with banking activity data.

This solution aids financial institutions and law enforcement in **early detection and prevention** of digital money laundering activities.

---

## 📂 Datasets Used

- **Cyber_crime_data.csv**: Contains cybercrime reports with identifiers like Aadhar number, PAN number, incident type, etc.
- **Bank_account_data.csv**: Contains details of bank accounts, including KYC details, account type, transaction patterns, etc.

---

## 🧠 Machine Learning Pipeline

1. **Data Preprocessing**
   - Merging datasets on unique identifiers (Aadhar & PAN)
   - Feature engineering & cleaning
   - Labeling suspicious accounts

2. **Model Building**
   - Supervised ML classification (Random Forest, XGBoost, etc.)
   - Evaluation: Accuracy, Precision, Recall, F1-score

3. **Deployment**
   - Streamlit web app for real-time predictions
   - Easy interface for investigators or financial analysts

---

## ⚙️ Tech Stack

- **Languages**: Python
- **Libraries**: Pandas
- **Web App**: Streamlit
- **Model Saving**: Pickle/Joblib

---

## 📊 Results

- Achieved **100% accuracy** on labeled dataset using Random Forest
- High precision and recall on unseen test data
- Web app deployed locally for real-time account screening

---

## 🖥️ Streamlit App (Demo)

> 📌 https://money-laundering-detector-qmgcsaayzfmh5mepyaxudy.streamlit.app/

- Upload account data and receive instant fraud probability
- View model explanations and key risk factors

---

## 📌 How to Run Locally

# Clone the repo
git clone https://github.com/your-username/uncovering-the-invisible.git
cd uncovering-the-invisible

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

📁 Folder Structure

.
├── data/
│   ├── Bank_account_data.csv
│   └── Cyber_crime_data.csv
├── models/
│   └── rf_model.pkl
├── notebooks/
│   └── EDA_and_Modeling.ipynb
├── app.py
├── requirements.txt
└── README.md

📬 Contact
If you're interested in this work or want to collaborate on anti-fraud or cybersecurity projects:

Name: Anitha M

LinkedIn: https://www.linkedin.com/in/anitha1921/

GitHub: https://github.com/AnithaM-97/

⭐ Acknowledgements
Thanks to open-source communities and cybercrime reporting frameworks that inspired this project.

⚠️ Disclaimer
This is an academic/project-based simulation and should not be used in real-world investigations without proper validation and regulatory compliance.

---
