import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize = (13, 7))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, rvalue, pvalue, stderr = linregress(x,y)
    x1 = list(range(1880, 2051))
    y1 = []
    for x in x1:
        y1.append(slope*x + intercept)

    # Create second line of best fit
    xnew = df[df['Year']>= 2000]['Year']
    ynew = df[df['Year']>= 2000]['CSIRO Adjusted Sea Level']
    slope1, intercept1, rvalue1, pvalue1, stderr1 = linregress(xnew,ynew)    
    x2 = list(range(2000, 2051))
    y2 = []
    for xnew in x2:
        y2.append(slope1*xnew + intercept1)
        
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.plot(x1, y1, label = 'Rise in Sea Level', color='green')
    plt.plot(x2, y2, label = 'Rise in Sea Level', color='red')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
