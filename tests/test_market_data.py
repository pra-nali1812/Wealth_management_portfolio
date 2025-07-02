import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_market_stock_endpoint(client):
    response = client.get('/api/market/stock')
    assert response.status_code in (200, 302, 400)  # 400 if missing params, 200 if default 