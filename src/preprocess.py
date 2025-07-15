import json
import pandas as pd
from collections import defaultdict

def preprocess_transactions(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)

    print(f"[DEBUG] Loaded {len(data)} transactions")
    print(f"[DEBUG] Sample: {data[:2]}")

    wallet_features = defaultdict(lambda: {
        "num_deposits": 0,
        "num_borrows": 0,
        "num_repays": 0,
        "num_withdrawals": 0,
        "num_liquidations": 0,
        "total_deposited": 0.0,
        "total_borrowed": 0.0,
        "total_repaid": 0.0,
        "total_withdrawn": 0.0,
        "liquidated": 0
    })

    count_skipped = 0

    for txn in data:
        wallet = txn.get("userWallet")
        action = txn.get("action", "").lower()

        # Safely get nested amount value
        try:
            amount = float(txn.get("actionData", {}).get("amount", 0))
        except (TypeError, ValueError):
            amount = 0.0

        if not wallet:
            count_skipped += 1
            continue

        if action == "deposit":
            wallet_features[wallet]["num_deposits"] += 1
            wallet_features[wallet]["total_deposited"] += amount
        elif action == "borrow":
            wallet_features[wallet]["num_borrows"] += 1
            wallet_features[wallet]["total_borrowed"] += amount
        elif action == "repay":
            wallet_features[wallet]["num_repays"] += 1
            wallet_features[wallet]["total_repaid"] += amount
        elif action == "redeemunderlying":
            wallet_features[wallet]["num_withdrawals"] += 1
            wallet_features[wallet]["total_withdrawn"] += amount
        elif action == "liquidationcall":
            wallet_features[wallet]["num_liquidations"] += 1
            wallet_features[wallet]["liquidated"] = 1

    df = pd.DataFrame.from_dict(wallet_features, orient='index')
    df.index.name = 'wallet'
    df.reset_index(inplace=True)

    df = df[df["wallet"].notnull() & (df["wallet"] != "")]

    print(f"[INFO] Extracted features for {len(df)} wallets.")
    print(f"[INFO] Skipped {count_skipped} invalid transactions.")
    print("[DEBUG] Sample features:")
    print(df.head())

    return df
