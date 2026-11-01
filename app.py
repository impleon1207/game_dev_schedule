from datetime import date, timedelta
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        project_name = request.form.get("project_name", "").strip() or "게임 개발 프로젝트"
        task_names = ["기획 및 조사", "디자인", "프로그래밍", "테스트", "보고서 작성"]
        field_names = ["planning", "design", "coding", "testing", "report"]
        try:
            days = [int(request.form.get(name, "0")) for name in field_names]
            if any(day < 0 for day in days):
                raise ValueError
            total = sum(days)
            start_raw = request.form.get("start_date", "")
            start_date = date.fromisoformat(start_raw) if start_raw else date.today()
            finish_date = start_date + timedelta(days=max(total - 1, 0))
            result = {
                "project_name": project_name,
                "tasks": list(zip(task_names, days)),
                "total": total,
                "start_date": start_date.isoformat(),
                "finish_date": finish_date.isoformat(),
            }
        except (ValueError, TypeError):
            error = "기간은 0 이상의 정수로 입력하고 시작일을 확인해 주세요."
    return render_template("index.html", result=result, error=error, today=date.today().isoformat())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", "5000")))
