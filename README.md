# Fraud-detection
Create accurate and strong fraud detection models that handle the unique challenges of fraud cases for e-commerce transactions and bank credit transactions. 
## Task 1: Data Analysis and Preprocessing
### Findings - E-commerce Data
- **Class Imbalance:** 9.3% Fraud. Requires SMOTE/Oversampling.
- **Key Feature:** `time_since_signup` showed that 100% of instant purchases (0-1s) were fraudulent.
- **Geography:** Identified Top 5 high-risk countries via IP mapping.

### Findings - Credit Card Data
- **Class Imbalance:** Extreme (0.17% Fraud).
- **Preprocessing:** Performed Robust Scaling on 'Amount' and 'Time' to match PCA-transformed features (V1-V28).