#!/bin/bash

docker build . -t big-data &&
mkdir ./tpce/bin ./tpce/flat_out ./tpce/obj ./tpce/lib;
docker run -it --rm -v $(pwd)/tpce:/tpce -w /tpce/prj big-data make &&
docker run -it --rm -v $(pwd)/tpce:/tpce -w /tpce big-data ./bin/EGenLoader -c 1000 -t 1000 -f 288000 -w 1 &&
docker compose down -v && docker compose up -d &&
docker build . -f Dockerfile_SimpleTest -t percona
docker run -it --rm -w /tpce-mysql percona