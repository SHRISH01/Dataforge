def encode_categorical(df, columns):
    """One-hot encode categorical columns."""
    try:
        df = pd.get_dummies(df, columns=columns, drop_first=True)
        return df
    except Exception as e:
        print(f"Error encoding categorical variables: {e}")
        return None
