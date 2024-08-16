from data_collection import collect_data
from feature_extraction import extract_features
from helper_functions import normalize_and_save_features

def main():
    df_key, df_mou, df_beh = collect_data("data/main.csv")
    print("\nDataframes gerados!")

    df_fea = extract_features(df_key, df_mou, df_beh)
    print("\nFeatures calculadas!")

    normalize_and_save_features(df_fea, 'results/features.xlsx')

if __name__ == "__main__":
    main()
