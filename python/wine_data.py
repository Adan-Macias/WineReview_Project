import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

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
    ax1.set_title('Winde Industry Quality', color='white', weight='bold')
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
    ax3.set_xlabel('Points', color='white')
    ax4.grid(axis='y', color='white')
    ax4.set_facecolor('black')
    legend1 = ax4.legend((patches[15], patches[10], patches[5], patches[0]), (pie_labels1),
                loc='upper right', bbox_to_anchor=(1,.9), facecolor='white', title='Quality Intervals')
    legend2 = ax4.legend(loc='lower right', bbox_to_anchor=(1,.6))
    ax4.set_xlabel('Wine Rating', color='white')
    ax4.add_artist(legend1)
    
    plt.tight_layout()
    plt.savefig('C:/Users/melen/Desktop/PORTFOLIO/WineReview_Project/Data_Visuals/wine_quality.png', bbox_inches='tight')


def main():
    # Invoke functions
    superiorWineVisuals()

# Invoke main  
main()
