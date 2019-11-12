
from fixture.application import application
import pytest

@pytest.fixture()
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture
