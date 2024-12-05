# fastapi-poetry-template
좌호빈 화이팅  
간단하게 FastAPI와 Poetry + Sentry을 사용하는 템플릿입니다.

## 야미
FastAPI X Poetry와 함께 쓰세요.   
app/ : 주요 코드  
app/core/ : 서버에 핵심 기능 (response, error, deps 등)  
app/router/ : fastapi.APIRouter.  
app/schema/ : response나 DTO를 위한 pydantic 모델.  


## 설정 파일
settings는 자동으로 ``.env`` 파일을 읽어서 환경 변수를 설정합니다.  
``.env`` typing을 검사하려면 ``app/core/config.py``를 확인하세요.


## 개발 환경 설정

이 프로젝트는 Python 가상 환경(venv)을 사용합니다. 아래 단계를 따라 개발 환경을 설정하세요.

### 사전 요구 사항

- Python 3.11 이상
- pip (최신 버전)
- poetry (최신 버전)

### 설치 단계

1. 프로젝트 클론

```bash
git clone https://github.com/your-team/cool-project.git
```


2. Poetry 설치
- Windows:
  ```bash
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
  ```
- macOS 및 Linux:
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

3. 의존성 패키지 설치
```bash 
poetry install
```

### 환경 변수 설정

`.example.env` 파일을 `.env`로 복사하고, 필요한 환경 변수를 설정하세요.

### 프로젝트 실행 방법
```bash
poetry run python3 -m app
```


### + Sentry 설정
Sentry를 사용하려면, `.env` 파일에 `SENTRY_DSN`을 추가하세요.
https://sentry.io
