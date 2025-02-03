# Campaign Performance Analysis - January 2025
## [Access the report file for complete analysis information]

## Overview

This project analyzes the marketing campaign performance for three clients: **ABC**, **DEF**, and **XYZ** from **January 1, 2025** to **January 31, 2025**. The analysis includes key performance indicators (KPIs) such as **Click-Through Rate (CTR)**, **Conversion Rate**, **Return on Investment (ROI)**, **Cost Per Acquisition (CPA)**, and **Profit Margin**. The goal is to evaluate the effectiveness of each client's marketing campaigns and provide insights for optimization.

## Table of Contents

1. [Dataset Information](#dataset-information)
2. [Approach and Methodology](#approach-and-methodology)
3. [Key Insights](#key-insights)
4. [Recommendations](#recommendations)
5. [How to Run the Code](#how-to-run-the-code)
6. [Dependencies](#dependencies)

## Dataset Information

The dataset includes the following columns:

- **p_date**: Date of the campaign.
- **Client Name**: The name of the client (ABC, DEF, XYZ).
- **Cost (USD)**: The total cost of the campaign.
- **Clicks**: The number of clicks the ad received.
- **Impressions**: The number of times the ad was displayed.
- **Sales**: The number of products sold.
- **GMV (Gross Merchandise Value)**: The total sales revenue generated.

These fields were used to calculate the following metrics for each campaign:

- **CTR (Click-Through Rate)**
- **Conversion Rate**
- **ROI (Return on Investment)**
- **CPA (Cost Per Acquisition)**

## Approach and Methodology

The following approach was taken to analyze the campaign data:

1. **Data Cleaning**: Cleaned and formatted the dataset to ensure consistency and readiness for analysis.
2. **Metric Calculation**: Calculated the key performance indicators (KPIs) for each client and campaign.
   - **CTR**: `(clicks / impressions) * 100`
   - **Conversion Rate**: `(sales / clicks) * 100`
   - **ROI**: `((GMV - Cost) / Cost) * 100`
   - **CPA**: `Cost / Sales`
3. **Visualization**: Created visualizations using **Tableau** to present the findings and insights.
   - Time series graphs to track performance trends over the month.
   - Comparison charts to assess the effectiveness of campaigns across clients.
   - Cost vs. ROI scatter plots to identify performance inefficiencies.
   - Heatmap representing the ROI on a day-by-day basis for each client, helping to
     identify fluctuations.
![VISUAL1](https://drive.google.com/uc?export=view&id=11RFJUagjZHfvGiOfdwY-Q9n0SDX2uKR8)
![VISUAL1](https://drive.google.com/uc?export=view&id=1KryKOZ2ThP53cScJooGvAJ-17kSJAipf)
![VISUAL1](https://drive.google.com/uc?export=view&id=16ezTPd8Lz1i_UKqGhxUjI-tKX-QO5LOT)
![VISUAL1](https://drive.google.com/uc?export=view&id=1UwLY5AbbvBo7HIKksH6PuYmVfs2gVatP)

## Key Insights

The analysis revealed the following key insights:

1. **ABC's Consistent ROI and High Efficiency**:

   - **ABC** consistently delivered high **ROI** and **Conversion Rates**, demonstrating excellent returns on ad spend with cost efficiency.
   - The high **CTR** and stable **conversion rates** indicate that **ABC** effectively targeted and engaged their audience.
2. **XYZ's Inconsistent Performance and High Costs**:

   - **XYZ** experienced significant fluctuations in **CTR**, **Conversion Rate**, and **ROI**. They had high **costs** with low returns, leading to negative **ROI** on multiple occasions.
   - Despite high **CTR**, their conversion rate was low, indicating issues in converting clicks into sales.
3. **DEF's Moderate Performance with High Costs**:

   - **DEF** showed steady performance with high **CTR** and **Conversion Rates** but had higher **CPA** compared to **ABC**, which resulted in lower **ROI**.
   - There is room for improvement by reducing **acquisition costs** and improving **ROI**.
4. **Cost vs ROI**:

   - **ABC** achieved high **ROI** with relatively low **costs**, making their campaign the most cost-effective.
   - In contrast, **XYZ** had high **costs** and low **ROI**, signaling inefficiencies in their campaign strategy.
5. **Heatmap: Daily Fluctuations**:

   - **ABC** showed consistent **ROI** throughout January, while **XYZ** experienced significant drops in **ROI** on various days, suggesting potential issues with ad fatigue or poor targeting.

## Recommendations

Based on the analysis, the following recommendations were made:

1. **For Client ABC**:

   - Continue with the current marketing strategy and scale successful tactics.
   - Monitor for ad fatigue and audience saturation.
2. **For Client XYZ**:

   - Focus on improving **Conversion Rates** by optimizing the landing page and user experience.
   - **Reevaluate budget allocation** to shift spend toward high-performing ads and channels.
3. **For Client DEF**:

   - Focus on reducing **CPA** by optimizing customer acquisition strategies.
   - Analyze ad creatives and targeting to improve **ROI**.

## How to Run the Code

1. Clone or download the repository.
2. Open the dataset (CSV format) in Python or your preferred tool for data analysis.
3. Use the provided **Python code** for calculating KPIs.
4. If you want to access the Tableau dashboard visualization, make sure you already have the database and set the configuration in your local.

## Dependencies

- Python 3.x
- pandas
- mysql
- Tableau (for advanced visualizations)
