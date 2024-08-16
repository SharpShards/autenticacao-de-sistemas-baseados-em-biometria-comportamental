import pandas as pd
from data_processing import load_data, split_data
from model_training import train_random_forest, train_svm, train_knn, train_logistic_regression
from metrics import calculate_metrics

def main():
    # Carregar dados
    df_fea = load_data('results/features.xlsx')
    
    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = split_data(df_fea)
    
    # Lista de classificadores
    classifiers = {
        "Random Forest": train_random_forest,
        "SVM": train_svm,
        "KNN": train_knn,
        "Regressão Logística": train_logistic_regression
    }
    
    # DataFrame para armazenar resultados
    analise = pd.DataFrame(columns=["id", "classificador", "accuracy", "frr", "far", "f1-score", "validação cruzada", "desvio padrão"])
    
    # Treinar e avaliar cada classificador
    for id, (name, train_function) in enumerate(classifiers.items()):
        model = train_function(X_train, y_train)
        acc, far, frr, f1, val_score, std_dev = calculate_metrics(model, X_test, y_test)
        
        # Armazenar resultados
        registro = pd.DataFrame([{
            "id": id, 
            "classificador": name, 
            "accuracy": acc, 
            "frr": frr, 
            "far": far, 
            "f1-score": f1, 
            "validação cruzada": val_score, 
            "desvio padrão": std_dev
        }])
        
        analise = pd.concat([analise, registro], ignore_index=True)
    
    # Salvar resultados
    analise.to_excel('results/metrics.xlsx', index=False)
    print("Análise completa e resultados salvos em 'results/metrics.xlsx'.")

if __name__ == "__main__":
    main()
