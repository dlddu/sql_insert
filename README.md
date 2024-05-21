## 작업 중
- benchmark 실행

## Prerequisite
- Docker 설치
   - 맥 기준 brew install --cask docker

## TPC-E 데이터 생성
1. bash build_tpce.sh 실행
2. docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce && ./bin/EGenLoader'
   - 처음엔 테스트 목적으로 docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce && ./bin/EGenLoader -c 1000 -t 1000 -f 288000 -w 1' 정도의 옵션을 추천
3. 2번의 명령어가 실행되면 flat_out 폴더 아래에 csv 형식의 데이터가 생성됨

## 데이터 저장
1. 데이터 생성이 완료되면, docker compose up -d로 db 띄우기 및 데이터 적재

## 벤치마크 실행
중간 발표 이후

## 참고 자료
https://github.com/Percona-Lab/tpce-mysql
