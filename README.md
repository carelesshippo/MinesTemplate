# Coding Problems Runner and Template
## [`generate.py`](./generate.py)
Running `python generate.py ProblemName` will generate ProblemName.java, and a folder in tests with that problem name
## [`runner.py`](./runner.py)
Running `python runner.py ProblemName.java` (or `problemname.py`) will run all the test cases that are in the folder with that same problem name (case-sensitive).

## Folder structure
```
|-- runner.py
|-- generate.py
|-- README.md
|-- Template.java
|-- Problem1.java
|-- problem2.py
|-- tests
    |-- Problem1
        |-- 1
            |-- 1.in
            |-- 1.ans
        |-- anythingcanbehere
            |-- itdoesntevenhavetohavethesamename.in
            |-- theansfilenamedoesntmattereither.ans
    |-- problem2
        |-- noansfilenecessary
            |-- wowSoCool.in
```
