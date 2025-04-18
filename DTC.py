from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import pickle

def train_model():
    iris = load_iris()
    X = iris.data
    Y = iris.target
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, Y_train)
    
    
    with open("model.pkl", "wb") as f:
        pickle.dump(clf, f)
    
    
    with open("test_data.pkl", "wb") as f:
        pickle.dump((X_test, Y_test), f)

    print("Model trained and saved as model.pkl")

def predict():
    
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    
    with open("test_data.pkl", "rb") as f:
        X_test, Y_test = pickle.load(f)

    
    Y_pred = model.predict(X_test)

    
    sample = [4.5, 2.3, 1.5, 0.2]  
    single_pred = model.predict([sample])
    print(f"Prediction for {sample}: {int(single_pred[0])}")

    
    print("\nAccuracy:", accuracy_score(Y_test, Y_pred))
    print("\nClassification Report:\n", classification_report(Y_test, Y_pred))
    print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))

if __name__ == "__main__":
    train_model()
    predict()
