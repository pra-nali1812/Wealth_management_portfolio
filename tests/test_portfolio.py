import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_view_portfolio_requires_login(client):
    response = client.get('/view_portfolio')
    # Should redirect to login if not authenticated
    assert response.status_code == 302
    assert '/login' in response.headers.get('Location', '')

def test_portfolio_page(client):
    response = client.get('/portfolio')
    # This route may require login; adjust as needed
    assert response.status_code in (200, 302) 