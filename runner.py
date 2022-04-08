#!/usr/bin/env python3

import time
import os
import sys
import argparse
from subprocess import Popen, PIPE

class Fore:
    MAGENTA = "\u001b[35;1m"
    CYAN = "\u001b[36;1m"
    RED = "\u001b[31;1m"
    GREEN = "\u001b[32;1m"
    BLUE = "\u001b[34;1m"
    RESET = "\u001b[0m"

JAVA_PATH = '/Users/ollie/.sdkman/candidates/java/11.0.14-zulu/bin'
JAVA_C = f'{JAVA_PATH}/javac'
JAVA_RUN = f'{JAVA_PATH}/java'

class Runner:
    def __init__(self, file_name):
        self.file_name = file_name
        self.init()

    def init(self):
        pass

    def compile(self):
        return (None, None)

    def execute(self, stdin):
        return (None, None)

class JavaRunner(Runner):
    def init(self):
        file_without_extension = os.path.splitext(file)[0]
        self.cleaned = file_without_extension.split('\\')[-1].split('/')[-1]

    def compile(self):
        return Popen([JAVA_C, '-d', './build', f'{self.file_name}']).communicate()

    def execute(self, stdin):
        return Popen([JAVA_RUN, '-cp', './build', self.cleaned], stdout=PIPE, stdin=stdin, stderr=PIPE).communicate()

class PythonRunner(Runner):
    def execute(self, stdin):
        return Popen(['python', self.file_name], stdout=PIPE, stdin=stdin, stderr=PIPE).communicate()

def run_test(runner: Runner, inp):
    start_time = time.time_ns()
    out, err = runner.execute(inp)
    end_time = time.time_ns()
    if out:
        out = out.decode()
    if err:
        err = err.decode()
    return (out, err, int((end_time - start_time) / 1000000))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The file name with extension')

    args = parser.parse_args()
    file = args.file
    file_split = os.path.splitext(file)
    extension = file_split[1]
    problem_name = file_split[0].split('\\')[-1].split('/')[-1]

    if extension == '.java':
        runner = JavaRunner(file)
    elif extension == '.py':
        runner = PythonRunner(file)
    else:
        print(f'Unknown file extension {extension}')
        sys.exit()

    print(Fore.MAGENTA + 'Compiling...' + Fore.RESET)
    compile_start = time.time_ns()
    compile_out, compile_err = runner.compile()
    compile_end = time.time_ns()
    if compile_out:
        print(Fore.CYAN + 'Compile out:' + Fore.RESET)
        print(compile_out)
    if compile_err:
        print(Fore.RED + 'Compile error:' + Fore.RESET)
        print(compile_err)
    print(Fore.MAGENTA + f'Compiled in {int((compile_end - compile_start) / 1000000)}ms\n' + Fore.RESET)

    problem_dir = os.path.join('.', 'tests', problem_name)
    dirs = sorted(os.listdir(problem_dir))

    passes = 0
    fails = 0
    neutrals = 0
    for ioname in dirs:
        case_dir = os.path.join(problem_dir, ioname)
        if os.path.isdir(case_dir):
            in_files = [file for file in os.listdir(case_dir) if file.endswith('.in')]
            out_files = [file for file in os.listdir(case_dir) if file.endswith('.ans')]
            if len(in_files) > 0:
                output, error, duration = run_test(runner, open(os.path.join(case_dir, in_files[0]), 'r'))
                print_output = True
                if len(out_files) > 0:
                    expected = open(os.path.join(case_dir, out_files[0]), 'r').read()
                    if output == expected:
                        print_output = False
                        print(Fore.GREEN + f'TEST {ioname} PASSED' + Fore.RESET)
                        passes += 1
                    else:
                        print_output = True
                        print(Fore.RED + f'TEST {ioname} FAILED' + Fore.RESET)
                        print(Fore.CYAN + 'Expected:' + Fore.RESET)
                        print(repr(expected))
                        fails += 1
                else:
                    print(Fore.BLUE + f'TEST {ioname}' + Fore.RESET)
                    neutrals += 1
                if print_output:
                    if output:
                        print(Fore.CYAN + 'Output:' + Fore.RESET)
                        print(repr(output))
                    else:
                        print(Fore.CYAN + 'No output' + Fore.RESET)
                if error:
                    print(Fore.RED + 'Runtime error:' + Fore.RESET)
                    sys.stdout.write(error)
                print(Fore.MAGENTA + f'Ran in {duration}ms\n' + Fore.RESET)
    print(Fore.GREEN + f'{passes} PASS' + Fore.RESET)
    print(Fore.RED + f'{fails} FAIL' + Fore.RESET)
    print(Fore.BLUE + f'{neutrals} NEUTRAL' + Fore.RESET)