## AI-Driven Telecom Churn Forecasting
![image alt](https://github.com/OneBlack333/Images/blob/main/churn-prediction.png)


## Business Problem

1. Customer Churn Prediction: Identify which customers are likely to stop using a product or service.
2. Pricing Strategy Analysis: Evaluate and refine pricing models to maximize revenue and competitiveness.
3. Optimizing Product Bundles: Determine the best combination of products to increase sales and customer satisfaction.

## Analytical Approach

Our analytic approach focuses on developing a predictive model to predict churn prediction for telecom companny is going to occur or not. We will analyze churn data, perform data preprocessing, feature engineering, and test various machine learning algorithms. We also used Artificial Neural Network(ANN) to increase overall accuracy.

## These are the features we used to predict rainfall.

1) gender: Customer’s gender (e.g., Male, Female).
2) SeniorCitizen: Indicates if the customer is a senior citizen (1 = Yes, 0 = No).
3) Partner: Whether the customer has a partner (Yes or No).
4) Dependents: Whether the customer has dependents (Yes or No).
5) tenure: Number of months the customer has been with the company.
6) PhoneService: Whether the customer has phone service (Yes or No).
7) MultipleLines: Whether the customer has multiple phone lines.
8) InternetService: Type of internet service (DSL, Fiber optic, or No).
9) OnlineSecurity: Whether the customer has online security add-on.
10) OnlineBackup: Whether the customer has online backup add-on.
11) DeviceProtection: Whether the customer has device protection add-on.
12) TechSupport: Whether the customer has tech support add-on.
13) StreamingTV: Whether the customer has streaming TV service.
14) StreamingMovies: Whether the customer has streaming movies service.
15) Contract: Type of contract (Month-to-month, One year, Two year).
16) PaperlessBilling: Whether the customer uses paperless billing.
17) PaymentMethod: Method of payment (e.g., Electronic check, Mailed check).
18) MonthlyCharges: The amount charged to the customer monthly.
19) TotalCharges: Total amount charged to the customer.
20) Churn: Whether the customer has left the company (Yes or No).
a) Yes means the customer has left the company (they churned).
b) No means the customer is still with the company (they did not churn).

Note: After encoding fetures gets incresase

## MonthlyCharges for pricing Strategy.
![Image](https://github.com/OneBlack333/Images/blob/main/monthly_charges.png)

## Churn Hotspots:

1) 70–100: Highest churn – Competition issue.
2) 100–120: Premium churn – Indicating critical peak
3) <40: Minor churn peak – possibly low-margin but Commitment users.

## Suggestion:

1) Incremental price rises (e.g., 1-2 annually) tied to visible minor feature additions.
2) Revalue the most churned charges price.
3) For high value charges give special discount need extra managment.
4) Split this problematic tier.Create a new tier from 70 - 100 give more features and reduce features below 60.
5) After A/B testing find the optimal balance between 70-110.

![Thank you](https://media.giphy.com/media/gEP2k49ndOqJDBSPZl/giphy.gif)

