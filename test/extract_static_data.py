import pytest
from unittest.mock import patch, Mock
from main import extract_static_data

def test_extract_static_data():
    mock_html = '''
    <html>
        <span id="productTitle">Producto de prueba</span>
        <span class="a-price-whole">99.99</span>
    </html>
    '''
    mock_response = Mock()
    mock_response.text = mock_html

    # Mock de requests.get
    with patch('main.requests.get', return_value=mock_response):
        product_name, product_price = extract_static_data("mock_url")
        
    assert product_name == "Producto de prueba"
    assert product_price == "99.99"
