
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
