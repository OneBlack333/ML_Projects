## E-commerce User Segmentation Strategy for Business Growth
![image alt](https://github.com/OneBlack333/Images/blob/main/User%20segment.png)

## Business Problem.
1) Customer Segmentation: Group customers by personality and behavior to tailor marketing strategies, reduce costs, and improve effectiveness.
2) Campaign Response Prediction: Identify segments most likely to respond positively to promotions, boosting ROI and conversions.
3) Product Recommendation Optimization: Personalize suggestions based on behavior and preferences to enhance experience and drive sales.
4) High-Value Customer Identification: Spot and prioritize customers with the highest lifetime value for better retention and resource allocation.

## Analytical Approach.
Our analytical approach focuses on developing customer clusters and categorizing them to support targeted e-commerce activities. We will analyze historical shopping data, perform data preprocessing, apply feature engineering techniques, and utilize unsupervised learning methods to identify meaningful customer segments.

## There are 21 features that we are going to use to segment customers into different categories. We have completed feature engineering and data preprocessing.

![image alt](https://github.com/OneBlack333/Images/blob/main/features.jpg)

#### The data were not normalized and exhibited left skewness, so we applied a log transformation in an effort to normalize them.
## 4 clusters were created using both K-Means and DBSCAN algorithms, with K-Means producing the most effective results.

![image alt](https://github.com/OneBlack333/Images/blob/main/clusters%204.jpg)

## Basis on RFM score is a marketing analytics technique used to analyze and segment customers based on their purchasing behavior.

1) R: Recency – How recently a customer made a purchase
2) F: Frequency – How often they purchase
3) M: Monetary – How much money they spend

## Customer Segments
    high_value_engaged
    promising_new
    at_risk
    inactive

## Basis on above analysis we create these 4 category.

![image alt](https://github.com/OneBlack333/Images/blob/main/final%20user%20distribution.jpg)
