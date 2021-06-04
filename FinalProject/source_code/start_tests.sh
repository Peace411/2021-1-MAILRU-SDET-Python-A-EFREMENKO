#! /bin/bash
echo $PYTHONPATH

pytest -s -v -n"${N}" /tmp/source_code/  --alluredir /tmp/alluredir

