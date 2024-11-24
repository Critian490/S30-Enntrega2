import pytest
from main import extract_static_data

def test_extract_static_data():
    mock_url = "https://mockurl.com"
    mock_data = ("Producto de prueba", "99.99")
    assert extract_static_data(mock_url) == mock_data
