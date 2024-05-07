## 작업 중
ddl.sql, main.py 파일의 tables 변수 채우는 중
ddl.sql에 create table 쿼리 추가할 때는 꼭 한 줄로 추가해주세요
main.py 파일의 tables 변수에는 (파일 이름, 테이블 이름) 순으로 추가해주세요

## Prerequisite
- Visual Studio Code 설치
   - 맥 기준 brew install --cask visual-studio-code
- Docker 설치
   - 맥 기준 brew install --cask docker

## TPC-E 데이터 생성
1. bash run.sh 실행
2. docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce && ./bin/EGenLoader'
   - 처음엔 테스트 목적으로 docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce && ./bin/EGenLoader -t 1000 -f 1 -w 1' 정도의 옵션을 추천
3. 2번의 명령어가 실행되면 flat_out 폴더 아래에 tsv 형식의 데이터가 생성됨

## 벤치마크 실행
1. 데이터 생성이 완료되면, vscode의 devcontainer 기능으로 해당 폴더 열기
  - 맥 기준 Command + Shift + P => Open Folder in Container...
2. main.py 파일 열어서 실행
