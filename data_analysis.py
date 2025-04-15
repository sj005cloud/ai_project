import pandas as pd
import matplotlib.pyplot as plt

def analyze_parking_patterns(data_file='data/historicaloccupency.csv'):
    df = pd.read_csv(data_file)
    
    area_trend = df.groupby(['Area', 'Day'])['Occupancy'].mean().unstack()
    area_trend.plot(kind='bar', figsize=(10,6))
    
    plt.title('Average Occupancy by Area & Day')
    plt.ylabel('Occupancy Rate')
    plt.xlabel('Area')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    analyze_parking_patterns()