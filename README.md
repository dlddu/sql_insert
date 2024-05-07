# TPC-E 데이터 생성

1. bash run.sh 실행
2. docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce && ./bin/EGenLoader'
   - 처음엔 테스트 목적으로 ... EGenLoader -t 1000 -f 1 -w 1 정도의 옵션을 추천
3. 데이터 생성이 완료되면, vscode의 devcontainer 기능으로 해당 폴더 열기
4. 작업 중
