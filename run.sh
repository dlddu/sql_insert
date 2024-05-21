#!/bin/bash

## 테스트 데이터를 만들자
docker build . -t big-data &&
mkdir ./tpce/bin ./tpce/flat_out ./tpce/obj ./tpce/lib;
### 테스트 데이터를 만드는 프로그램 빌드
docker run -it --rm -v $(pwd)/tpce:/tpce -w /tpce/prj big-data make &&
### 테스트 데이터 만들기
docker run -it --rm -v $(pwd)/tpce:/tpce -w /tpce big-data ./bin/EGenLoader -c 1000 -t 1000 -f 288000 -w 1 &&
## db 띄우고 데이터 넣기
docker compose down -v && docker compose up -d &&
## 벤치마크를 돌리자
### 벤치마크 프로그램 (SimpleTest) 빌드
docker build . -f Dockerfile_SimpleTest -t percona
### 벤치마크 프로그램을 실행할 수 있는 컨테이너 실행 (벤치마크는 알아서 실행하기)
docker run -it --rm -w /tpce-mysql --network $(basename $(pwd))_app_db_network percona