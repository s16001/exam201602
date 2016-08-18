import unittest
import sys
import math
from io import StringIO, SEEK_SET
from datetime import date

from exam import exam, test


class StdIOHook:
    def __init__(self):
        self.held = None

    def set_hook_stdout(self):
        self.held = sys.stdout
        sys.stdout = StringIO()  # type: StringIO

    def release_hook_stdout(self):
        sys.stdout.close()
        sys.stdout = self.held
        self.held = None

    def reset_stdout(self):
        if self.held is not None:
            sys.stdout.truncate(0)
            sys.stdout.seek(0, SEEK_SET)


class TestTest(unittest.TestCase, StdIOHook):
    def setUp(self):
        self.set_hook_stdout()

    def test_test(self):
        test.test()
        self.assertEqual(sys.stdout.getvalue(), 'ok\n')

    def test_test2(self):
        test.test()
        self.assertEqual(sys.stdout.getvalue(), 'ok\n')
        self.reset_stdout()
        test.test2()
        self.assertEqual(sys.stdout.getvalue(), 'ng\n')

    def tearDown(self):
        self.release_hook_stdout()


class ExamTest(unittest.TestCase, StdIOHook):
    def setUp(self):
        self.set_hook_stdout()

    def tearDown(self):
        self.release_hook_stdout()

    def test_hello(self):
        exam.hello('John')
        self.assertEqual(sys.stdout.getvalue(), 'hello, John!\n')

    def test_length(self):
        exam.length('Dive into python3!')
        self.assertEqual(sys.stdout.getvalue(), '18\n')
        self.reset_stdout()
        exam.length('Python Tutorial')
        self.assertEqual(sys.stdout.getvalue(), '15\n')

    def test_slicing2to5(self):
        exam.slicing2to5('Dive into python3!')
        self.assertEqual(sys.stdout.getvalue(), 've \n')
        self.reset_stdout()
        exam.slicing2to5('Python Tutorial')
        self.assertEqual(sys.stdout.getvalue(), 'tho\n')

    def test_number_sign(self):
        exam.number_sign(-3)
        self.assertEqual(sys.stdout.getvalue(), '-\n')
        self.reset_stdout()
        exam.number_sign(0)
        self.assertEqual(sys.stdout.getvalue(), '0\n')
        self.reset_stdout()
        exam.number_sign(10)
        self.assertEqual(sys.stdout.getvalue(), '+\n')


    def test_prime_number(self):
        exam.prime_number(2)
        self.assertEqual(sys.stdout.getvalue(), 'ok\n')
        self.reset_stdout()
        exam.prime_number(3)
        self.assertEqual(sys.stdout.getvalue(), 'ok\n')
        self.reset_stdout()
        exam.prime_number(4)
        self.assertEqual(sys.stdout.getvalue(), 'ng\n')
        self.reset_stdout()
        exam.prime_number(5)
        self.assertEqual(sys.stdout.getvalue(), 'ok\n')
        self.reset_stdout()
        exam.prime_number(6)
        self.assertEqual(sys.stdout.getvalue(), 'ng\n')
        self.reset_stdout()
        exam.prime_number(7)
        self.assertEqual(sys.stdout.getvalue(), 'ok\n')
        self.reset_stdout()
        exam.prime_number(8)
        self.assertEqual(sys.stdout.getvalue(), 'ng\n')
        self.reset_stdout()
        exam.prime_number(9)
        self.assertEqual(sys.stdout.getvalue(), 'ng\n')
        self.reset_stdout()
        exam.prime_number(10)
        self.assertEqual(sys.stdout.getvalue(), 'ng\n')
        self.reset_stdout()
        exam.prime_number(11)
        self.assertEqual(sys.stdout.getvalue(), 'ok\n')

    def test_sum_from_1_to(self):
        exam.sum_from_1_to(1)
        self.assertEqual(sys.stdout.getvalue(), '1\n')
        self.reset_stdout()
        exam.sum_from_1_to(5)
        self.assertEqual(sys.stdout.getvalue(), '15\n')
        self.reset_stdout()
        exam.sum_from_1_to(1000)
        self.assertEqual(sys.stdout.getvalue(), '500500\n')
        self.reset_stdout()
        exam.sum_from_1_to(777)
        self.assertEqual(sys.stdout.getvalue(), '302253\n')
        self.reset_stdout()

    def test_factorial(self):
        exam.factorial(0)
        self.assertEqual(sys.stdout.getvalue(), '1\n')
        self.reset_stdout()
        exam.factorial(4)
        self.assertEqual(sys.stdout.getvalue(), '24\n')
        self.reset_stdout()
        exam.factorial(9)
        self.assertEqual(sys.stdout.getvalue(), '362880\n')
        self.reset_stdout()
        exam.factorial(13)
        self.assertEqual(sys.stdout.getvalue(), '6227020800\n')
        self.reset_stdout()
        exam.factorial(7)
        self.assertEqual(sys.stdout.getvalue(), '5040\n')
        self.reset_stdout()

    def test_cubic_list(self):
        self.assertEqual(
            exam.cubic_list([1, 2, 3, 4, 5]), [1, 8, 27, 64, 125])
        self.assertEqual(exam.cubic_list(
            [-3, -2, -1, 0, 1, 2, 3]), [-27, -8, -1, 0, 1, 8, 27])

    def test_calc_hypotenuse(self):
        self.assertEqual(exam.calc_hypotenuse(1, 2), math.sqrt(5))
        self.assertEqual(exam.calc_hypotenuse(3, 4), 5.0)
        self.assertEqual(exam.calc_hypotenuse(9, 12), 15.0)

    def test_calc_subtense(self):
        self.assertEqual(exam.calc_subtense(15, 12), 9)
        self.assertEqual(exam.calc_subtense(5, 3), 4)
        self.assertEqual(exam.calc_subtense(1, 2), math.sqrt(3))

    def test_calc_area_triangle(self):
        self.assertEqual(exam.calc_area_triangle(3, 4, 5), 6)
        self.assertEqual(exam.calc_area_triangle(9, 12, 15), 54)
        self.assertEqual(exam.calc_area_triangle(10, 15, 20), 72.61843774138907)

    def test_point_two_digits(self):
        exam.point_two_digits(1.4142135623730951, 1.7320508075688772, 2.23606797749979)
        self.assertEqual(sys.stdout.getvalue(), '1.41 1.73 2.24\n')
        self.reset_stdout()
        exam.point_two_digits(2.449489742783178, 2.6457513110645907, 2.8284271247461903)
        self.assertEqual(sys.stdout.getvalue(), '2.45 2.65 2.83\n')
        self.reset_stdout()
        exam.point_two_digits(2, 3, 4)
        self.assertEqual(sys.stdout.getvalue(), '2.00 3.00 4.00\n')
        self.reset_stdout()

    def test_list_sort(self):
        self.assertEqual(exam.list_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(exam.list_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(exam.list_sort([3, 3, 2, 9]), [2, 3, 3, 9])
        self.assertEqual(exam.list_sort([-1, -2, -3, -4]), [-4, -3, -2, -1])

    def test_reverse_string(self):
        self.assertEqual(exam.reverse_string('hello, python'), 'nohtyp ,olleh')
        self.assertEqual(exam.reverse_string('dive into python 3'), '3 nohtyp otni evid')

    def test_days_from_date(self):
        self.assertEqual(exam.days_from_date(date(1969, 12, 25)), 16899)
        self.assertEqual(exam.days_from_date(date(2001, 4, 1)), 5479)
        self.assertEqual(exam.days_from_date(date(2015, 4, 1)), 366)
