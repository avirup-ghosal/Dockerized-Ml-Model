# 📦 Dockerized ML Model

A beginner-friendly machine learning project that trains a Decision Tree Classifier on the Iris dataset using scikit-learn, then runs it inside a Docker container for easy portability and reproducibility.

##  Features

- Trains a `DecisionTreeClassifier` on the Iris dataset
- Saves the trained model as a `.pkl` file using `pickle`
- Loads the model and makes predictions on sample input
- Fully containerized using Docker

## 🚀 Pull the Image

```bash
docker pull avirupghosal2023525/ml-model
```
## ▶️ Run the Container

```bash
docker run -d -p 8080:80 avirupghosal2023525/ml-model
```
