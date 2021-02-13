import pytest
from functions.sennder import Sennder
func = Sennder()


@pytest.fixture(scope="session")
def sennder():
    return func

def pytest_unconfigure():
    func.quit()

