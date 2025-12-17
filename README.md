# 🎓 Student Performance Analyzer

> **End-to-end Machine Learning regression project** that predicts student exam scores based on behavioral and demographic features using advanced ML pipelines, hyperparameter tuning, and explainable AI.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📊 Project Overview

This project analyzes **20,000 student records** from a Kaggle dataset to predict **exam scores** using machine learning. The solution combines:
- **Industry-grade preprocessing pipelines** (ColumnTransformer with StandardScaler & OneHotEncoder)
- **Hyperparameter optimization** using GridSearchCV
- **Explainable AI** with permutation importance
- **Interactive web app** deployed on Streamlit

### 🎯 Key Achievements
- **MAE**: 6.89 | **RMSE**: ~17.44% | **R²**: High predictive accuracy
- Identified **study_hours** and **class_attendance** as strongest predictors
- Production-ready ML pipeline saved for reuse
- User-friendly Streamlit interface with real-time predictions

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Programming** | Python 3.8+ |
| **ML Framework** | scikit-learn, pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Deployment** | Streamlit |
| **Version Control** | Git, GitHub |

---

## 💻 Project Structure

```
student-performance-analyzer/
│
├── data/
│   ├── raw/                    # Original Kaggle dataset
│   └── processed/              # Cleaned data (optional)
│
├── notebooks/
│   └── analysis.ipynb          # Full EDA and model development
│
├── models/
│   └── trained_pipeline.pkl    # Saved ML pipeline
│
├── app/
│   └── streamlit_app.py        # Deployment script
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── LICENSE                     # MIT License
```

---

## 🚀 Getting Started

### Prerequisites
```bash
python --version  # Ensure Python 3.8+
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/mayank-goyal09/student-performance-analyzer.git
cd student-performance-analyzer
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### ▶️ Running the App

**Launch Streamlit App:**
```bash
streamlit run app/streamlit_app.py
```

The app will open at `http://localhost:8501` 🌐

---

## 📊 Methodology

### 1️⃣ Data Preprocessing
- **Dataset**: 20,000 rows with mixed numeric and categorical features
- **Target Variable**: `exam_score`
- **Feature Engineering**: Dropped `student_id`, handled categorical variables
- **Pipeline**: ColumnTransformer with:
  - **StandardScaler** for numeric features
  - **OneHotEncoder** for categorical features

### 2️⃣ Model Development
- **Algorithm**: K-Nearest Neighbors (KNN) Regressor
- **Hyperparameter Tuning**: GridSearchCV for optimal `n_neighbors`
- **Cross-Validation**: Robust model evaluation

### 3️⃣ Model Evaluation
- **Metrics**: MAE (6.89), RMSE (~17.44%), R²
- **Error Analysis**: Analyzed worst prediction errors
- **Feature Importance**: Permutation importance revealed:
  - 📈 **study_hours**: Strongest predictor
  - 📋 **class_attendance**: Second most important

### 4️⃣ Deployment
- **Streamlit App** with:
  - User input form for predictions
  - Real-time score estimation
  - **Insights Section** showing top feature importances
  - Clean, interactive UI

---

## 🎯 Results

### Model Performance
| Metric | Value |
|--------|-------|
| **MAE** | 6.89 |
| **RMSE%** | ~17.44% |
| **R² Score** | High accuracy |

### Feature Importance (Top 3)
1. 📈 **Study Hours** - Primary driver of exam performance
2. 📋 **Class Attendance** - Strong positive correlation
3. 📄 **Additional factors** - Moderate impact

---

## 📸 Screenshots

*Add screenshots of your Streamlit app here*

---

## 🔮 Future Enhancements

- [ ] Experiment with ensemble models (Random Forest, XGBoost)
- [ ] Add SHAP values for deeper explainability
- [ ] Implement feature engineering (polynomial features)
- [ ] Deploy to cloud platform (Streamlit Cloud, Heroku)
- [ ] Create API endpoint using FastAPI
- [ ] Add A/B testing framework

---

## 📝 Lessons Learned

✅ **Industry-grade pipelines** ensure reproducibility and maintainability  
✅ **Hyperparameter tuning** significantly improves model performance  
✅ **Feature importance analysis** provides actionable insights  
✅ **Streamlit** enables rapid deployment without complex infrastructure  

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 💬 Contact

**Mayank Goyal**  
📧 Email: [itsmaygal09@gmail.com](mailto:itsmaygal09@gmail.com)  
💔 LinkedIn: [mayank-goyal](https://www.linkedin.com/in/mayank-goyal-4b8756363/)  
👨‍💻 GitHub: [@mayank-goyal09](https://github.com/mayank-goyal09)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🚀 Acknowledgments

- Kaggle for the Student Performance dataset
- scikit-learn community for excellent ML tools
- Streamlit for making deployment effortless

---

<div align="center">
  <strong>If this project helped you, consider giving it a ⭐!</strong>
</div>