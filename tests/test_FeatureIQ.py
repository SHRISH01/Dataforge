import pytest
from FeatureIQ.core import handle_missing_values

def test_handle_missing_values():
    import pandas as pd
    df = pd.DataFrame({"col1": [1, None, 3], "col2": [None, 2, 3]})
    processed_df = handle_missing_values(df, strategy="mean")
    assert processed_df.isnull().sum().sum() == 0
