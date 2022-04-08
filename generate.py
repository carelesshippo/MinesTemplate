#!/usr/bin/env python3
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='The problem name')

    args = parser.parse_args()
    name = args.name
    template_read = open('./Template.java', 'r')
    new_file = open(f'./{name}.java', 'x')
    content = template_read.read()
    new_file.write(content.replace('Template', name))
    new_file.close()
    os.mkdir(f'./tests/{name}')
    print('Created file and input directory')
