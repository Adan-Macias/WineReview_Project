import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def superiorWineVisuals():
    wine = pd.read_csv('/Users/melen/Desktop/PORTFOLIO/WineReview_Project/Data/winemag-data-130k.csv')

    # Wine scale intervals (Ratings)
    interval1 = wine.loc[(wine['points'] >= 95) & (wine['points'] <= 100)].count()[0]
    interval2 = wine.loc[(wine['points'] >= 90) & (wine['points'] <= 94)].count()[0]
    interval3 = wine.loc[(wine['points'] >= 85) & (wine['points'] <= 89)].count()[0]
    interval4 = wine.loc[(wine['points'] >= 80) & (wine['points'] <= 84)].count()[0]

    # Best wine by country
    bestWine_ByCountry = []
    superiorWine = wine.loc[(wine['points'] >= 95) & (wine['points'] <= 100)]
    for country in superiorWine['country'].value_counts():
        bestWine_ByCountry.append(country)

    # Labeling & Coloring
    pie_labels1 = ('Superior: 95-100', 'Outstanding: 90-94', 'Very Good: 85-90', 'Good: 80-84')
    pie_labels2 = ('U.S', 'France', 'Italy', 'Austria', 'Portugal', 'Germany', 'Spain', 'Australia')
    colors = ['goldenrod', 'seagreen', 'slateblue', 'maroon']

    # Pie Chart Visual #1
    plt.figure(figsize=(14,12), facecolor='black')
    ax1 = plt.subplot(2,2,1)
    ax1.pie([interval1, interval2,interval3, interval4], 
            explode=(0.6,0,0,0),autopct='%.2f%%', colors=colors, shadow=True)
    ax1.set_title('Wine Quality Portions', color='white', weight='bold')
    ax1.legend(pie_labels1, loc='upper right', bbox_to_anchor=(1.2,1), fontsize=8.5, title='Ranking[Points]')

    # Pie chart Visual #2 
    ax2 = plt.subplot(2,2,2)
    ax2.pie([bestWine_ByCountry[0], bestWine_ByCountry[1], bestWine_ByCountry[2],bestWine_ByCountry[3],
            bestWine_ByCountry[4],bestWine_ByCountry[5],bestWine_ByCountry[6],bestWine_ByCountry[7]],
            autopct='%.2f%%', explode=(0,0,0,0.3,0.3,0.3,0.3,0.3),
            shadow=True)
    ax2.set_title('Best Wine By Sources: Points 95-100', color='white', weight='bold')
    ax2.legend(pie_labels2, loc='upper right',facecolor='white', bbox_to_anchor=(1.2,1), 
                fontsize=8.5, title='Country')

    # Bar chart where Points >=95 by province
    ax3 = plt.subplot(2,2,3)
    ax3 = superiorWine['province'].value_counts().head(10).plot(kind='bar', color='goldenrod')
    ax3.set_title('Superior Wine By Province And Points 95-100', color='white', weight='bold')
    ax3.set_xlabel('Province', color='white')
    ax3.tick_params(axis='x', colors='white', rotation=45)
    ax3.set_facecolor('black')

    # Histogram Visual based on points
    ax4 = plt.subplot(2,2,4)
    n,bin1,patches = ax4.hist(wine['points'], color='limegreen', ec='black', bins=20)

    # Find the mean in points
    pointsMean = wine['points'].mean()

    # Filling bar intervals per wine quality
    bar = 0
    while bar <=19:
        if bar >=15 and bar <=19:
            patches[bar].set_fc('goldenrod')
        elif bar >=10 and bar <=14:
            patches[bar].set_fc('seagreen')
        elif bar >=5 and bar <=9:
            patches[bar].set_fc('slateblue')
        else:
            patches[bar].set_fc('maroon')
        bar+=1
    ax4.set_title('Wine Total Point Distribution[Good-Superior]', color='white', weight='bold')
    ax4.axvline(pointsMean, color='red', linewidth=4, label='Mean')
    ax4.tick_params(axis='x', colors='white')
    ax4.tick_params(axis='y', colors='white')
    ax4.set_xlabel('Points', color='white')
    ax4.grid(axis='y', color='white')
    ax4.set_facecolor('black')
    legend1 = ax4.legend((patches[15], patches[10], patches[5], patches[0]), (pie_labels1),
                loc='upper right', bbox_to_anchor=(1,.9), facecolor='white', title='Quality Intervals')
    legend2 = ax4.legend(loc='lower right', bbox_to_anchor=(1,.6))
    ax4.set_xlabel('Wine Rating', color='white')
    ax4.add_artist(legend1)
    plt.tight_layout()
    plt.savefig('C:/Users/melen/Desktop/PORTFOLIO/WineReview_Project/Data_Visuals/wine_quality.png', bbox_inches='tight')

def winePrice():
    wine = pd.read_csv('/Users/melen/Desktop/PORTFOLIO/WineReview_Project/Data/winemag-data-130k.csv')
    # Dropping Null values located in price column
    wine = wine.dropna(subset=['price'])

    # Extract target varieties and filter
    bestVariations = wine['variety'].value_counts().head(24).index.tolist()
    bestVariations_counts = wine['variety'].value_counts().head(24).tolist()
    bestVariations_counts.sort()
    
    # Data Visual #1
    plt.figure(figsize=(12,11),facecolor="black")
    ax1 = plt.subplot2grid((10,2), (0,0), rowspan=7, colspan=2)
    ax1.set_title('Top 25 Wine Variations By Volume', color='white', weight='bold')
    ax1.scatter(y=bestVariations, x=bestVariations_counts, s=80, color='maroon')
    ax1.grid(axis='y', color='white', linestyle='--', alpha=0.1)
    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='white')
    ax1.set_xlabel('Volume', color='white', weight='bold')
    ax1.set_ylabel('Wine Variation', color='white', weight='bold')
    ax1.set_facecolor('black')

    
    # Extracting top 25 variety data and calculating means per points/price
    variationsPriceMean = []
    variationsPointMean = []
    for variety in bestVariations:
        x = wine[(wine.variety == variety) & (wine.price > 0)]
        meanPrice = x.price.mean()
        meanPrice = round(meanPrice,2)
        
        meanPoints = x.points.mean()
        meanPoints = round(meanPoints,0)

        variationsPriceMean.append(meanPrice)
        variationsPointMean.append(meanPoints)

    # Data Visual #2
    ax2 = plt.subplot2grid((10,2), (7,0), rowspan=3, colspan=1)
    variationsPointMean.sort()
    ax2.scatter(bestVariations, variationsPointMean, color='blue', alpha=0.7, linewidth=3)
    ax2.grid(axis='x', color='white', linestyle='--', alpha=0.1)
    ax2.grid(axis='y', color='white', linestyle='solid', alpha=0.1)
    ax2.tick_params(axis='x', colors='white', rotation=90)
    ax2.tick_params(axis='y', colors='white')
    ax2.set_xlabel('Wine Variety', color='white', weight='bold')
    ax2.set_ylabel('Points Avg ', color='white', weight='bold')
    ax2.set_facecolor('black')

    # Data Visual #3
    ax3 = plt.subplot2grid((10,2), (7,1), rowspan=3, colspan=1)
    variationsPriceMean.sort()
    ax3.vlines(x=bestVariations, ymin=0, ymax=variationsPriceMean, color='green', alpha=0.7, linewidth=5)
    ax3.grid(axis='y', color='white', linestyle='--', alpha=0.1)
    arrange_yticks = np.arange(0, 100, 20)
    ax3.tick_params(axis='x', colors='white', rotation=90)
    ax3.tick_params(axis='y', colors='white')
    ax3.set_yticks(arrange_yticks)
    ax3.set_xlabel('Wine Variety', color='white', weight='bold')
    ax3.set_ylabel('Price Avg', color='white', weight='bold')
    ax3.set_facecolor('black')
    plt.tight_layout()
    plt.savefig('C:/Users/melen/Desktop/PORTFOLIO/WineReview_Project/Data_Visuals/top25_variations.png', bbox_inches='tight')
    
def main():
    # Invoke functions
    superiorWineVisuals()
    winePrice()

# Invoke main  
main()
