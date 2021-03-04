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
