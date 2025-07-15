import pandas as pd

def score_wallets(df):
    # Prevent division by zero by replacing 0 max values with 1
    max_deposit = df["total_deposited"].max() or 1
    max_withdraw = df["total_withdrawn"].max() or 1

    # Feature: deposit quality
    df["deposit_score"] = df["total_deposited"] / max_deposit

    # Feature: how responsibly the user repays
    df["repay_ratio"] = df["total_repaid"] / (df["total_borrowed"] + 1e-6)  # Avoid zero-div

    # Feature: withdrawal behavior
    df["withdrawal_score"] = df["total_withdrawn"] / max_withdraw

    # Penalty for liquidation
    df["liquidation_penalty"] = df["liquidated"].apply(lambda x: -0.3 if x == 1 else 0)

    # Final score: combine all features (adjustable weights)
    df["final_score"] = (
        0.4 * df["deposit_score"] +
        0.3 * df["repay_ratio"] +
        0.2 * df["withdrawal_score"] +
        df["liquidation_penalty"]
    )

    # Scale to 0–1000 range
    df["credit_score"] = (df["final_score"].clip(lower=0).fillna(0) * 1000).clip(0, 1000).astype(int)

    return df[["wallet", "credit_score"]]
