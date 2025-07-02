import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_performance_requires_login(client):
    response = client.get('/performance')
    # Should redirect to login if not authenticated, or 404 if not accessible
    assert response.status_code in (302, 401, 404)
    if response.status_code == 302:
        assert '/login' in response.headers.get('Location', '')

def test_performance_page(client):
    response = client.get('/performance')
    assert response.status_code in (200, 302) 