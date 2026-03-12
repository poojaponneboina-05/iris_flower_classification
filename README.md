# 🌸 Iris Flower Classification using Machine Learning

## 📌 Project Overview

The **Iris Flower Classification** project is a simple Machine Learning application that predicts the species of an Iris flower based on its physical measurements.

The application uses a trained Machine Learning model and a **Streamlit web interface** where users can enter flower measurements and instantly get the predicted flower species.

---

## 📊 Dataset

This project uses the famous **Iris Dataset**, which contains **150 samples** of iris flowers.
Each sample includes the following features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The model predicts one of the three species:

* 🌼 Setosa
* 🌷 Versicolor
* 🌹 Virginica

---

## 🛠 Technologies Used

* Python
* Machine Learning (Scikit-learn)
* NumPy
* Streamlit
* GitHub

---

## 🤖 Machine Learning Model

A **Random Forest Classifier** is used to train the model.
The trained model is saved as a `.pkl` file and used in the Streamlit application for prediction.

---

## 🚀 How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 2: Train the Model

```bash
python train_model.py
```

### Step 3: Run the Streamlit App

```bash
streamlit run app.py
```

---

## 💻 Application Interface

The Streamlit app allows users to input the following values:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

After clicking **Predict**, the application displays the predicted iris species.

---

## 📂 Project Structure

```
iris-flower-classification
│
├── app.py
├── train_model.py
├── iris_model.pkl
├── requirements.txt
└── README.md
```

---

## 🎯 Project Purpose

This project demonstrates:

* Basic Machine Learning model training
* Model saving and loading using pickle
* Creating an interactive web application using Streamlit
* Deploying ML projects using GitHub and Streamlit Cloud

---

## 👨‍💻 Author

Project developed as part of a **Machine Learning practice project**.


Live Demo


https://irisflowerclassification-4hvvyja3c9wdmqdqqegdkk.streamlit.app/


