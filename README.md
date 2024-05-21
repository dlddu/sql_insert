## 작업 중
- ddl.sql, main.py 파일의 tables 변수 채우는 중
   - ddl.sql에 create table 쿼리 추가할 때는 꼭 한 줄로 추가해주세요
   - main.py 파일의 tables 변수에는 (파일 이름, 테이블 이름) 순으로 추가해주세요
      - 파일은 tpce/flat_out 폴더 아래에 있습니다

## Prerequisite
- Visual Studio Code 설치
   - 맥 기준 brew install --cask visual-studio-code
- Docker 설치
   - 맥 기준 brew install --cask docker

## TPC-E 데이터 생성
1. bash run.sh 실행
2. docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce && ./bin/EGenLoader'
   - 처음엔 테스트 목적으로 docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce && ./bin/EGenLoader -c 1000 -f 288000 -w 1' 정도의 옵션을 추천
3. 2번의 명령어가 실행되면 flat_out 폴더 아래에 csv 형식의 데이터가 생성됨

## 데이터 저장
1. 데이터 생성이 완료되면, vscode의 devcontainer 기능으로 해당 폴더 열기
  - 맥 기준 Command + Shift + P => Open Folder in Container...
2. scripts 폴더 내의 sql 명령어들 실행

## 벤치마크 실행
중간 발표 이후

## 참고 자료
https://github.com/Percona-Lab/tpce-mysql
