import matplotlib.pyplot as plt
import seaborn as sns

def create_boxplot(df, column):
    """Create a boxplot for a single column."""
    try:
        sns.boxplot(y=df[column])
        plt.title(f"Boxplot for {column}")
        plt.show()
    except Exception as e:
        print(f"Error creating boxplot: {e}")

def create_histogram(df, column):
    """Create a histogram for a single column."""
    try:
        df[column].hist(bins=30)
        plt.title(f"Histogram for {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()
    except Exception as e:
        print(f"Error creating histogram: {e}")
