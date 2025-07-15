# 💰 Aave Credit Scoring Engine

This project implements a **DeFi credit scoring system** that evaluates on-chain behavior of wallets interacting with the Aave V2 protocol. Each wallet is assigned a **credit score from 0 to 1000**, where a higher score indicates more responsible usage.

---

## 🧠 Problem Statement

We were provided with raw, transaction-level data from Aave V2, covering key user actions like:

- `deposit`
- `borrow`
- `repay`
- `redeemUnderlying`
- `liquidationCall`

Using this historical behavior, the goal is to design a **machine learning or rules-based pipeline** that evaluates risk and scores wallets accordingly.

---

## 🧩 Features Engineered

From the raw JSON data, we aggregated the following **per-wallet features**:

| Feature            | Description                              |
| ------------------ | ---------------------------------------- |
| `num_deposits`     | Number of times the user deposited funds |
| `num_borrows`      | Number of borrows                        |
| `num_repays`       | Number of repayments                     |
| `num_withdrawals`  | Redeems (withdrawals)                    |
| `num_liquidations` | Times the wallet got liquidated          |
| `total_deposited`  | Total value deposited                    |
| `total_borrowed`   | Total value borrowed                     |
| `total_repaid`     | Total value repaid                       |
| `total_withdrawn`  | Total value withdrawn                    |
| `liquidated`       | Binary flag: 1 if user ever liquidated   |

---

## 🧮 Scoring Logic

Each wallet starts with a **base score of 500**, then gets **rewards or penalties** based on behavior:

- ➕ Rewards:

  - Deposits and repayments increase score
  - No liquidation earns a bonus

- ➖ Penalties:

  - High borrow with low repay reduces score
  - Liquidation reduces score significantly

- ➖➕ The final score is **clipped between 0 and 1000**

Implemented in: [`src/scoring.py`](src/scoring.py)

---

## 🏗️ Project Structure

aave-credit-scoring/
├── data/ ← Input raw JSON file
├── outputs/ ← Scored wallet outputs (CSV)
├── src/ ← All Python scripts
├── analysis.md ← Score distribution & insights
├── README.md ← Project overview

## 📁 Input Data

Download the full dataset from the challenge link and place it in the `data/` folder:

📎 Raw JSON (~87MB):  
https://drive.google.com/file/d/1ISFbAXxadMrt7Zl96rmzzZmEKZnyW7FS/view
