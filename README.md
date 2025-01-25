Investor sentiment reflects the collective emotions of market participants toward stocks or market conditions, often derived from financial data, news, and social media. Sentiment analysis has become a key tool for forecasting trends. Herd behavior occurs when investors mimic others, driven by fear of missing out or the belief that others are better informed.
This study explores how major news events, particularly during crises like COVID-19, impact investor psychology, with implications for market stability, decision-making, and risk management.

Problem Statement:

Core Issue:
Major news events during crises intensify investor sentiment, driving irrational decisions and herd behavior. This disrupts market efficiency, leading to volatility, mispricing, and systemic risks.

Objective:

Analyze how news events influence investor sentiment and herd behavior in the Indian stock market (NIFTY-50).
Validate the impact of sentiment on market returns and herding during volatile periods.

Methodology:

Sentiment Analysis: Used VADER, BERT, and FinBERT models, with features like moving averages and event dates.
Herding Analysis: Computed CSAD and CSSD to measure deviations from market averages during stress periods.
Regression: Analyzed relationships between market returns and CSAD/CSSD scores to identify herding.
Predictive Modeling: Applied Random Forest, Gradient Boosting, and XGBoost to predict stock returns based on sentiment scores.

Results:

Sentiment Analysis: FinBERT effectively aligned sentiment scores with market movements, highlighting the value of domain-specific models.
Stock Data Integration: Combined NIFTY-50 data with sentiment scores to study their impact on market behavior.

Predictive Modeling: XGBoost outperformed other models, with high R² and low MSE, confirming sentiment's predictive role during volatile periods.

CAR Analysis: Negative CAR values during key events (e.g., March 24) showed heightened investor uncertainty and pessimism.

Herding Analysis: CSAD and CSSD results indicated herding behavior, with reduced return dispersion as market returns rose.

Conclusion:

The study reveals that news-driven sentiment significantly impacts market returns and fosters herd behavior during crises. Investors tend to follow market trends, reducing return dispersion during volatile times. These findings enhance understanding of external influences on investor behavior and the psychological dynamics of financial markets.
