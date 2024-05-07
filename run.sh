#!/bin/bash

docker build . -t big-data
docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce/prj && make'