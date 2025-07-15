import os
from preprocess import preprocess_transactions
from scoring import score_wallets

def main():
    input_path = os.path.join("data", "user_transactions.json")
    output_path = os.path.join("outputs", "scores.csv")

    print("[INFO] Preprocessing transactions...")
    df_features = preprocess_transactions(input_path)

    print("[INFO] Scoring wallets...")
    df_scores = score_wallets(df_features)

    print("[INFO] Saving results to outputs/scores.csv")
    df_scores.to_csv(output_path, index=False)
    print("[DONE] Wallet scoring completed!")

if __name__ == "__main__":
    main()
