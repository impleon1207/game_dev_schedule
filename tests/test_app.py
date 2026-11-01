from app import app

def test_homepage_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "게임 개발 일정 계산기".encode() in response.data

def test_calculation_result():
    client = app.test_client()
    response = client.post("/", data={
        "project_name": "테스트 게임",
        "start_date": "2026-11-02",
        "planning": "2",
        "design": "3",
        "coding": "5",
        "testing": "2",
        "report": "1",
    })
    assert response.status_code == 200
    assert "13일".encode() in response.data
    assert "2026-11-14".encode() in response.data

def test_negative_days_rejected():
    client = app.test_client()
    response = client.post("/", data={
        "project_name": "잘못된 입력",
        "start_date": "2026-11-02",
        "planning": "-1",
        "design": "0",
        "coding": "0",
        "testing": "0",
        "report": "0",
    })
    assert "0 이상의 정수".encode() in response.data
