# Decalcifier

## 📌 Project Overview

Decalcifier is a machine learning-based API that predicts the number of hours required to decalcify different types of bone samples based on specific parameters.&#x20;

## 🚀 How It Works

The model was trained on manually gathered data and uses a **Decision Tree Regressor** to predict the decalcification time based on:

- The **type of bone** (e.g., bone marrow, premolar tooth, etc.)
- The **type of fluid** used for decalcification (e.g., HCl, EDTA, etc.)
- The **percentage concentration** of the fluid
- The **date** when the decalcification was performed (day, month, year)

### 📊 Quantitative Insights

- **About 3800 data points** were collected in total for this project.
- The model achieved an **R² score of 0.9948695408163637%**, indicating exceptional predictive performance.
- We leveraged **explainable AI** and exported the decision tree, allowing us to fully understand how the model makes its predictions.

The trained model is integrated into a Flask API that allows users to send input data and receive predictions.

---

## ⚙️ Setup Instructions

Follow these steps to set up the project locally:

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd Decalcifier
```

### 2️⃣ Install Dependencies

Make sure you have Python installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask API

```bash
python app.py
```

By default, the API will be available at `http://127.0.0.1:5000/`

---

## 🌍 API Usage

### 🔹 Base URL

```
http://127.0.0.1:5000/
```

### 🔹 Endpoints

#### 1️⃣ Check API Status

**Request:**

```http
GET /
```

**Response:**

```
Welcome, please smile more
```

#### 2️⃣ Predict Decalcification Time

**Request:**

```http
POST /predict
```

**Request Body (JSON):**

```json
{
  "sample": "bone_marrow",
  "fluid": "HCl",
  "percentage": 12.5,
  "day": 5,
  "month": 5,
  "year": 2023
}
```

**Response:**

```json
{
  "prediction": 48.5
}
```

(The response value is the estimated number of hours required for decalcification.)

---

## 📤 Deployment

The project is deployed using **Azure App Service**. You can deploy it manually or use the `.github/workflows` pipeline for automated deployment.

---

## 🛠 Possible Improvements

- Experimenting with other machine learning models (e.g., Random Forest, XGBoost)
- Adding more data for better accuracy
- Optimizing API response time
- Deploying using **Docker** for better scalability

---

### 💡 Contributing

Feel free to fork the repository, make improvements, and submit a pull request.

---

### 📧 Contact

If you have any questions, reach out to the project maintainers.

---

✨ **Happy Learning!**

