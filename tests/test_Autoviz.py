import pytest
from Autoviz.core import load_data, preprocess_data

def test_load_data():
    df = load_data("tests/sample_data.csv")
    assert df is not None

def test_preprocess_data():
    df = load_data("tests/sample_data.csv")
    processed_df = preprocess_data(df)
    assert processed_df.isnull().sum().sum() == 0
