# Fast scan Python code to check it "compilable"

PYTHONPATH=$(pwd) pylint --disable=C0301,C0114,W0212,W0612,R0914,C0103,C0116,W0612,C0411,W1508,W0703,W0107 --recursive=y main.py
