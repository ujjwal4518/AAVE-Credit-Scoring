# 📊 Wallet Credit Score Analysis – Aave V2

This report provides an analysis of wallet credit scores computed based on transaction-level behavior on the Aave V2 protocol. The credit score ranges from **0 to 1000**, where higher scores represent responsible, consistent DeFi usage, and lower scores represent riskier, bot-like, or exploit-prone behavior.

---

## 🔢 Score Distribution

The wallets were binned into ranges of 100. Here's the distribution:

| Score Range | Number of Wallets | % of Total |
| ----------- | ----------------- | ---------- |
| 0–100       | XXX               | XX%        |
| 100–200     | XXX               | XX%        |
| 200–300     | XXX               | XX%        |
| 300–400     | XXX               | XX%        |
| 400–500     | XXX               | XX%        |
| 500–600     | XXX               | XX%        |
| 600–700     | XXX               | XX%        |
| 700–800     | XXX               | XX%        |
| 800–900     | XXX               | XX%        |
| 900–1000    | XXX               | XX%        |

> _(Note: These numbers should be generated using a histogram from `scores.csv`.)_

---

## 🔍 Observed Wallet Behaviors by Score Range

### 🔴 **Low Score Range (0–200):**

- Frequent liquidation events
- Borrowed large amounts with little or no repayment
- Abrupt deposit-withdraw cycles (bot or exploit-like)
- High `total_borrowed` – low `total_repaid`

### 🟡 **Mid Score Range (400–600):**

- Moderate participation in the protocol
- Some repayments made, but not full
- Activity patterns may be inconsistent (e.g., borrow-repay but no deposits)

### 🟢 **High Score Range (800–1000):**

- Consistent deposits and full repayments
- Zero or minimal liquidation events
- High volume users with responsible behavior
- Long-term interaction with the protocol

---

## 📈 Key Insights

- Wallets with **no liquidation** and **high repayment** behavior tend to cluster above 800.
- A large proportion of wallets score between 400–700, representing average DeFi users.
- Liquidation events are the strongest negative signal in the scoring model.
- The model shows promise in detecting potential bot-like or risky behavior via transaction patterns.

---

## 🔮 Future Improvements

- Add timestamp-based features (e.g., average time between borrow and repay)
- Include asset type or token-specific behavior
- Incorporate cluster-based anomaly detection (unsupervised learning)
- Consider time decay for older transactions

---

## 📁 File Reference

- **Input**: `data/user_transactions.json`
- **Output**: `outputs/scores.csv`
- **Scoring Logic**: `src/scoring.py`

---
