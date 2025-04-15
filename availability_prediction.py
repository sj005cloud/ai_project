import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def predict_availability(data_file='data/historicaloccupency.csv'):
    df = pd.read_csv(data_file)

    
    # Label encoding for categorical data
    df['Day'] = df['Day'].astype('category').cat.codes
    df['Time'] = df['Time'].astype('category').cat.codes
    df['Area'] = df['Area'].astype('category').cat.codes
    df['SpotID'] = df['SpotID'].astype('category').cat.codes
    
    X = df[['Day', 'Time', 'Area', 'SpotID']]
    y = df['Occupancy']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Decision Tree
    dt_model = DecisionTreeClassifier()
    dt_model.fit(X_train, y_train)

    # Random Forest
    rf_model = RandomForestClassifier(n_estimators=100)
    rf_model.fit(X_train, y_train)

    print("Decision Tree Accuracy:", dt_model.score(X_test, y_test))
    print("Random Forest Accuracy:", rf_model.score(X_test, y_test))

if __name__ == '__main__':
    predict_availability()