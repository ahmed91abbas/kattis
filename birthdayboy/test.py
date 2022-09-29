import sys
import os
import main
import time
from unittest import TestCase

test_case = TestCase()


def run_test(test_nbr):
    sys.stdin = open(os.path.join('data', f'{test_nbr}.in'), 'r')
    with open(os.path.join('data', f'{test_nbr}.ans'), 'r') as f:
        expected = f.read()
    start_time = time.time()
    result = main.run()
    print(f'Test case {test_nbr} ran in {time.time() - start_time:.5f} seconds')
    test_case.assertEqual(expected.rstrip(), result.rstrip())


def run_all_tests():
    tests = set([os.path.splitext(f)[0] for f in os.listdir('data')])
    for test in tests:
        run_test(test)


if __name__ == '__main__':
    run_all_tests()
