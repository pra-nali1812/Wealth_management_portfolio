import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_strategies_recommend_view(client):
    response = client.get('/strategies/recommend/view?user_id=1')
    assert response.status_code in (200, 404, 400) 