import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from testdating import TestDating
import HTMLTestRunner


def main():
    search_tests = unittest.TestLoader().loadTestsFromTestCase(TestDating)
    suite_tests = unittest.TestSuite([search_tests])

    with open(os.path.join(os.getcwd(), 'TestReport.html'), "w") as hlr:
        runner = HTMLTestRunner.HTMLTestRunner(stream=hlr, title='Test Dataing Report', description='Test Suite')
        runner.run(suite_tests)


if __name__ == "__main__":
    main()