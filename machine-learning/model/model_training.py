from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

def train_random_forest(X_train, y_train):
    """Treina um modelo de Random Forest."""
    model = RandomForestClassifier(max_depth=20, n_estimators=100)
    model.fit(X_train, y_train)
    return model

def train_svm(X_train, y_train):
    """Treina um modelo SVM."""
    model = SVC(C=50, kernel='rbf')
    model.fit(X_train, y_train)
    return model

def train_knn(X_train, y_train):
    """Treina um modelo KNN."""
    model = KNeighborsClassifier(n_neighbors=2, weights='distance')
    model.fit(X_train, y_train)
    return model

def train_logistic_regression(X_train, y_train):
    """Treina um modelo de Regressão Logística."""
    model = LogisticRegression(C=5, solver="newton-cg", max_iter=1000)
    model.fit(X_train, y_train)
    return model
