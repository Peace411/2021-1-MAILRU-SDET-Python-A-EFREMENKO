#! /bin/bash
echo $PYTHONPATH

pytest -s -v /tmp/source_code/mysql_tests/test_mysql.py --alluredir /tmp/alluredir
pytest -s -v /tmp/source_code/ui_tests/tests/test_ui.py --alluredir /tmp/alluredir