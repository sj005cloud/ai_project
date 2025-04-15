import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def recommend_nearest_spots(current_location, data_file='data/parkingspots.csv'):
    spots_df = pd.read_csv(data_file)
    
    # Extract coordinates
    coordinates = spots_df[['Latitude', 'Longitude']].values
    
    # Fit NearestNeighbors
    knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
    knn.fit(coordinates)
    
    # Find nearest spots
    distances, indices = knn.kneighbors([current_location])
    
    recommended_spots = spots_df.iloc[indices[0]]
    return recommended_spots

# Example usage:
if __name__ == '__main__':
    # Replace this with your current GPS coordinates
    current_location = [28.6140, 77.2100]
    print(recommend_nearest_spots(current_location))