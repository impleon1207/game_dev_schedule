# 게임 개발 일정 계산기

게임 제작 단계별 예상 소요 일수를 입력해 총 작업 기간과 예상 완료일을 계산하는 간단한 한국어 웹 서비스입니다. 입력 데이터는 서버에 저장하지 않습니다.

## 주요 기능
- 프로젝트 이름과 시작일 입력
- 기획 및 조사, 디자인, 프로그래밍, 테스트, 보고서 작성 기간 입력
- 총 예상 일수와 완료일 계산
- 음수 기간 입력 오류 처리
- GitHub Actions를 통한 자동 테스트
- Render 배포 설정(`render.yaml`)으로 웹 서비스 배포 및 자동 배포 구성

## 로컬 실행 방법
Python 3.10 이상을 권장합니다.

```powershell
python -m pip install -r requirements.txt
python app.py
```

브라우저에서 `http://127.0.0.1:5000`에 접속합니다.

## 테스트
```powershell
python -m pytest -q
```

## GitHub 및 배포 방법
1. GitHub에서 새 **Public** 저장소를 만듭니다.
2. 이 폴더의 파일을 저장소에 업로드합니다.
3. 저장소의 **Actions** 탭에서 `Test and validate` 작업이 성공하는지 확인합니다.
4. Render 계정에서 GitHub 저장소를 연결해 Web Service를 생성하거나, Render의 Blueprint 기능으로 `render.yaml`을 적용합니다.
5. Build Command는 `pip install -r requirements.txt`, Start Command는 `gunicorn app:app`인지 확인합니다.
6. 배포가 완료되면 Render가 제공하는 공개 URL에 접속해 일정 계산을 직접 확인합니다.
7. Render 서비스 설정에서 Auto-Deploy가 활성화되어 있는지 확인합니다. 이후 `main` 브랜치에 코드를 push하면 새 버전이 자동 배포됩니다.

## 검증할 항목
- 홈페이지가 정상적으로 열리는가?
- 기간 2, 3, 5, 2, 1일을 입력했을 때 합계가 13일로 나오는가?
- 시작일이 2026-11-02일 때 계산된 완료일이 2026-11-14로 나오는가?
- 음수 기간 입력 시 오류 안내가 나오는가?
- GitHub Actions 테스트가 성공하는가?
- 공개 배포 URL에서 기능이 동작하는가?
- 코드를 수정하고 push한 뒤 자동 배포가 되는가?

## 주의
서비스의 완료일 계산은 입력한 기간이 연속된 달력 날짜로 진행된다고 가정합니다. 주말, 공휴일, 병렬 작업은 계산하지 않습니다. 실제 공개 배포 및 자동 배포 여부는 계정에서 배포한 뒤 직접 확인해야 합니다.
