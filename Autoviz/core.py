import pandas as pd

def load_data(filepath):
    """Load dataset from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(df):
    """Basic preprocessing: drop null values."""
    try:
        df = df.dropna()
        return df
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        return None
