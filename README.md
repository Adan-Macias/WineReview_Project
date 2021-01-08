# WineReview: Project Overview
- Provides analysis on wine review data containing close to 130k datapoints
- Purpose of this project focuses on superior wine information based on a grading scale 80 - 100
- Provides various data visualizations on superior wine interval along with a distribution of all intervals as per wine points
- Visuals are auto saved after every execution and contained in a single subplot grid.


 # Code & Resources 
 #### Python Version: 3.7
 #### Packages: pandas, matplotlib
 #### Kaggle
  - URL: https://www.kaggle.com/zynicide/wine-reviews?select=winemag-data-130k-v2.csv
     
 # Dataframe filtering:
  - Scale intervals are generated with Dataframe boolean conditions.
  - Intervals are specific to each wine rating such as Superior, Outstanding, Very Good, and Good.
  - This process isolates the superior quality interval in overall wine industry which remains the target data.
 
 # Data visualization: Superior Wine Analysis and Overall Quality Distribution
 ### Pie Chart 1:
   * Overall wine dataset is analyzed for wine point intervals and each interval is then isolated.
   * Wine intervals contains different pools or amounts as per ranking.
   * Results in 1.86% of total wine data to have superior wine and most of the wine industry containing "Very Good" at 52.70%
 ### Pie Chart 2:
   * This chart is a continuation of Pie Chart 1 and provides more details on superior wine(1.86%).
   * The main sources of superior wine production is displayed at interval 95 - 100 on chosen dataset.
   * Results demonstrate U.S provides largest portion of superior wine with 41.55% while Australia is the lowest at 1.97%
 ### Bar Chart:   
   * A micro level of the 1.86% is demonstrated where superior wine is prodiced by province.
   * Results demonstrate a very high volume of superior wine with a source/province of California
 ### Histogram:
   * A distribution of all wine intervals are shown in this visual which provides clear view of wine ratings in the wine industry.
   * A mean is provided where the mos common rating in the overall wine industry is 88 points.
   * Intervals (85-84) and (90-94) contain the largest portions of the wine dataset while superior remains very low at 1.86%.
 
 ![](https://raw.githubusercontent.com/Adan-Macias/WineReview_Project/master/Data_Visuals/wine_quality.png)
 
 # Data visualization: Top 25 Wine Variation With Points/Price Means
 ### Scatter Plot: 
   * Provides data visual of filtered wine variations(top 25 in dataset).
   * Wine variations are plotted along volume/amount present in wine dataset and therefore assuming most popular reviewed variations.
 ### Scatter Plot 2: 
   * Provides wine point averages for each wine variety for top 25 reviewed wines.
   * This chart can provide assistance with wine variety choices based on wine ratings.
 ### Bar Chart: 
   * Provides the average price as per wine variety and clearly shows patterns between points and price.
   * This data can be beneficial to wine lovers who desire to experiment and take rating/prices as influential factors in buying decisions.
 
 ![](https://raw.githubusercontent.com/Adan-Macias/WineReview_Project/master/Data_Visuals/top25_variations.png)


