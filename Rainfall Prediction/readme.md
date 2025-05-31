## Rainfall Prediction Simple to Advanced Project.
![image alt](https://github.com/OneBlack333/Images/blob/e7dc7aff46feb10c7f2a8dea44f96492fdb38630/AI%20generated%20Beautiful%20rain%20day%20view.jpg)

## Business Problem.
1) Supply Chain & Risk Management: Enabling businesses to anticipate weather-related disruptions, especially in logistics and construction sectors.
2) Disaster Preparedness & Response: Helping governments and NGOs plan for floods or landslides, improving emergency response strategies.
3) Agricultural Planning: Helping farmers optimize crop planting and harvesting schedules to reduce losses due to unpredictable rainfall.
4) Water Resource Management: Assisting government and utility companies in planning water storage and distribution in drought-prone areas.

## Analytical Approach.
Our analytic approach focuses on developing a predictive model to predict rainfall is going to occur or not. We will analyze historical weather data, perform data preprocessing, feature engineering, and test various machine learning algorithms. We also used Artificial Neural Network(ANN) to increase overall accuracy.

### These are the features we used to predict rainfall.
![image alt](https://github.com/OneBlack333/Images/blob/272c72d90717fa4eebbb5ae13a274ddfe9e07c3a/rain_column.png)

### To improve accuracy, I created features specifically related to rainfall prediction. These columns help in determining the likelihood and intensity of rainfall.
![image alt](https://github.com/OneBlack333/Images/blob/272c72d90717fa4eebbb5ae13a274ddfe9e07c3a/rain%20feature%20engineeering.png)

### The best model we get is Gradient Boosting Classifier and in which part GBC is doing well & where it needs improvement.
![image alt](https://github.com/OneBlack333/Images/blob/272c72d90717fa4eebbb5ae13a274ddfe9e07c3a/rain%20classification%20report.png)

1) High Precision (0.86) for Rain (Class 1): Ensures most predicted "rain" events are accurate, reducing false alarms.

2) High Recall (0.94) for Rain: Captures 94% of actual rain events, minimizing missed predictions.

3) Balanced Accuracy (0.85): Overall performance is strong, with weighted metrics favoring the majority class (rain).

4) Practical Focus: Prioritizes detecting rain (critical for warnings) over non-rain cases, reflected in the higher recall for Class 1.

### Confusion Matrix
![image alt](https://github.com/OneBlack333/Images/blob/272c72d90717fa4eebbb5ae13a274ddfe9e07c3a/rain_confusion_matrix.png)

## Conclusion
1) The best-performing models were GBC(Gradient Boosting Classifier).
2) Their simplicity and reduced risk of overfitting made them more effective than complex algorithms, especially with our limited dataset.

![https://tenor.com/view/thank-you-merci-ty-thanks-thanku-gif-7239271062540128493]
