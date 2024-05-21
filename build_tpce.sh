#!/bin/bash

docker build . -t big-data
mkdir ./tpce/bin ./tpce/flat_out ./tpce/obj ./tpce/lib
docker run -it --rm -v $(pwd)/tpce:/tpce big-data bash -c 'cd /tpce/prj && make'