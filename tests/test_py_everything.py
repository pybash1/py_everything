import sys, unittest # Do not remove or change this statement
sys.path.append("..") # Do not remove or change this statement
import py_everything as pye # Do not remove or change this statement
import py_everything.automation as pye_auto # Do not remove or change this statement
import py_everything.date_utils as pye_date # Do not remove or change this statement
import py_everything.fileIO as pye_fileIO # Do not remove or change this statement
import py_everything.maths as pye_maths # Do not remove or change this statement
import py_everything.py_everything_exceptions as pye_exception # Do not remove or change this statement
import py_everything.requestsLib as pye_request # Do not remove or change this statement
import py_everything.search as pye_search # Do not remove or change this statement
import py_everything.web as pye_web # Do not remove or change this statement

# Do not change the filename.
# Do not change the folder name.

# Add tests here and push or pull request to testthem on GitHub.
# Format:
'''
class TestPyEverything(unittest.TestCase):
    def test_[function_name]():
        code to test goes here
        example given below - 
        assert py_everything.maths.add(2, 4) == 6
'''
class TestPyEverything(unittest.TestCase):
    def test_add(self):
        assert pye_maths.add(2, 4) == 6

    def test_subtract(self):
        assert pye_maths.subtract(10, 5, 2) == 3

    def test_multiply(self):
        assert pye_maths.multiply(5, 3, 2) == 30

    def test_divide(self):
        assert pye_maths.divide(120, 10, "float") == 12.0

    def test_divide_2(self):
        assert pye_maths.divide(120, 10, "int") == 12

    def test_float_div(self):
        assert pye_maths.float_div(120, 10) == 12.0

    def test_int_div(self):
        assert pye_maths.int_div(120, 10) == 12

    def test_mod(self):
        assert pye_maths.mod(123, 2) == 1

    def test_eval_exp(self):
        assert pye_maths.eval_exp("(2+3-1)*2") == 8

    def test_avg(self):
        assert pye_maths.avg([2, 4, 6, 8]) == 5

    def test_install_modules(self):
        assert pye.install_modules("playsound") == True

    def test_read_file(self):
        assert pye_fileIO.read_file("read.txt") == 'demo\n'

    def test_write_file(self):
        assert pye_fileIO.write_file("write.txt", "demo data") == True

    def test_clear_file(self):
        assert pye_fileIO.clear_file("clear.txt") == True

    def test_search_list(self):
        listToTest = ["py", "pypi", "anything", "something", "python", "other", "middlepy", "notmatch", "endpy"]
        assert pye_search.search_list(listToTest, "py") == ["py", "pypi", "python", "middlepy", "endpy"]

    def test_search_list_2(self):
        listToTest = ["py", "pypi", "anything", "something", "python", "other", "middlepy", "notmatch", "endpy"]
        assert pye_search.search_list(listToTest, "py", filter="start") == ["py", "pypi", "python"]

    def test_search_list_3(self):
        listToTest = ["py", "pypi", "anything", "something", "python", "other", "middlepy", "notmatch", "endpy"]
        assert pye_search.search_list(listToTest, "py", filter="end") == ["py", "middlepy", "endpy"]

    def test_search_list_4(self):
        listToTest = ["py", "pypi", "anything", "something", "python", "other", "middlepy", "notmatch", "endpy"]
        assert pye_search.search_list(listToTest, "py", filter="exact") == ["py"]
