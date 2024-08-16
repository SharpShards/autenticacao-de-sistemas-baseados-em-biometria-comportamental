import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import cross_val_score

def calculate_metrics(model, X_test, y_test):
    """Calcula métricas para um modelo treinado."""
    pred = model.predict(X_test)
    acc = round(accuracy_score(y_test, pred) * 100, 2)
    
    conf_matrix = confusion_matrix(y_test, pred)
    far, frr = calculate_far_frr(conf_matrix)
    f1 = round(f1_score(y_test, pred, average='weighted') * 100, 2)
    val_score, std_dev = cross_val_metrics(model, X_test, y_test)
    
    return acc, far, frr, f1, val_score, std_dev

def calculate_far_frr(conf_matrix):
    """Calcula FAR e FRR a partir da matriz de confusão."""
    far_l = []
    frr_l = []
    
    for loop in range(conf_matrix.shape[0]):
        TP = conf_matrix[loop, loop]
        FP = np.sum(conf_matrix[:, loop]) - TP
        FN = np.sum(conf_matrix[loop, :]) - TP
        TN = np.sum(conf_matrix) - TP - FP - FN

        far_l.append(FP / (FP + TN))
        frr_l.append(FN / (FN + TP))
    
    far = round(np.mean(far_l) * 100, 2)
    frr = round(np.mean(frr_l) * 100, 2)
    
    return far, frr

def cross_val_metrics(model, X_train, y_train, cv=5):
    """Calcula validação cruzada e desvio padrão."""
    scores = cross_val_score(model, X_train, y_train, cv=cv)
    score_mean = round(np.mean(scores) * 100, 2)
    std_dev = round(np.std(scores) * 100, 2)
    return score_mean, std_dev
