import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """Carrega dados do arquivo Excel."""
    return pd.read_excel(file_path)

def split_data(df, test_size=0.2):
    """Divide os dados entre treino e teste por label."""
    grouped = df.groupby('label')
    train_data = []
    test_data = []
    
    for _, group in grouped:
        train, test = train_test_split(group, test_size=test_size)
        train_data.append(train)
        test_data.append(test)
        
    df_train = pd.concat(train_data)
    df_test = pd.concat(test_data)
    
    train_labels = df_train.pop('label').to_numpy().astype(str)
    test_labels = df_test.pop('label').to_numpy().astype(str)
    
    return df_train, df_test, train_labels, test_labels
