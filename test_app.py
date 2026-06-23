import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for our Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ============ HOME PAGE TESTS ============


def test_home_page_loads(client):
    """Test that the home page returns status 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_has_title(client):
    """Test that the home page contains our site title."""
    response = client.get("/")
    assert b"My Flask Site" in response.data


def test_home_page_has_nav(client):
    """Test that the navigation is included."""
    response = client.get("/")
    assert b"navbar" in response.data


def test_home_page_has_bootstrap(client):
    """Test that Bootstrap CSS is linked."""
    response = client.get("/")
    assert b"bootstrap" in response.data


# ============ CONTACT PAGE TESTS ============


def test_contact_page_loads(client):
    """Test that the contact page returns status 200."""
    response = client.get("/contact")
    assert response.status_code == 200


def test_contact_page_has_form(client):
    """Test that the contact page has a form."""
    response = client.get("/contact")
    assert b"<form" in response.data


# ============ LIBRARY PAGE TESTS ============
def test_library_page_loads(client):
    """Test that the library page returns status 200."""
    response = client.get("/library")
    assert response.status_code == 200


## ============ SEARCH ROUTE TESTS ============
def test_search_page_loads(client):
    """Test that the search route returns status 200."""


## ============ PAGE TESTS ============
def test_people_page_loads(client):
    """Test that the people page returns status 200."""
    response = client.get("/people")
    assert response.status_code == 200


def test_animals_loads(client):
    """Test that the animals page returns status 200."""
    response = client.get("/animals")
    assert response.status_code == 200


def test_nature_loads(client):
    """Test that the nature page returns status 200."""
    response = client.get("/nature")
    assert response.status_code == 200
