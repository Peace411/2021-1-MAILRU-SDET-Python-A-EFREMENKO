#! /bin/bash
echo $PYTHONPATH
pytest -s -v /tmp/source_code/mysql_tests/test_mysql.py
pytest -s -v /tmp/source_code/ui_tests/tests/test_ui.py