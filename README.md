# github-action-test
Github Actions 이용하여 매일 뉴스 스크래핑 하기

## 설정방식
1. Github Repo Page에서 Actions Tab 들어가 원하는 Workflow 선택 (여기선 Python package 사용중)
2. Configure후 /workflow/.yml 파일로 이동
3. 이하 .yml 파일 설정 예시

```python
# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

# 이름 지정
name: Python Scrapper

on:
  schedule:
#   분 / 시 / 일 / 월 / 요일
#   '*/10 * * * *' 10분씩마다 실행
#   '0 0 * * *' 매일 UTC 0시 0분마다 실행(한국시간 9시)
    - cron: '0 23 * * *'
#   Push / Pull branch 설정
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.10"]
    # Python version 설정 (위의 matrix: python-version에 설정된 ver에서 Test
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    # 첨부해둔 requirements.txt에서 의존성 패키지 Download
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    # Scrapping 파일 실행
    - name: Run Scrapper
      run: |
        python "scrapping.py"
    # Commit
    - name: Commits
      run: |
        git config --local user.email "wonhyeok.contact@gmail.com"
        git config --local user.name "WonhyeokJUng"
        git add news.json
        git commit -m "[feat]Auto Update File" 
#     - name: Test with pytest
#       run: |
#         pytest
    # Push
    - name: Push
      uses: ad-m/github-push-action@master
      with:
        branch: 'master'
        github_token: $ 
```
