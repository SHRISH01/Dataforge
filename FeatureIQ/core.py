def handle_missing_values(df, strategy="mean"):
    """Handle missing values in the dataset."""
    try:
        for col in df.select_dtypes(include=["float64", "int64"]).columns:
            if strategy == "mean":
                df[col].fillna(df[col].mean(), inplace=True)
            elif strategy == "median":
                df[col].fillna(df[col].median(), inplace=True)
            elif strategy == "mode":
                df[col].fillna(df[col].mode()[0], inplace=True)
        return df
    except Exception as e:
        print(f"Error handling missing values: {e}")
        return None
