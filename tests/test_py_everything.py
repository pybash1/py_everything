import py_everything as pye  # Do not remove or change this statement
import py_everything.automation as pyeAuto
import py_everything.dateUtils as pyeDate
import py_everything.fileIO as pyeFileIO
import py_everything.maths as pyeMaths
import py_everything.error as pyeError
import py_everything.search as pyeSearch
import py_everything.web as pyeWeb  # Do not remove or change this statement
import py_everything.htmlXml as pyeHtml
import py_everything.mensuration as pyeMensuration
import py_everything.conversion as pyeConversion
import sys
import unittest  # Do not remove or change this statement
sys.path.append("..")  # Do not remove or change this statement
# Do not remove or change this statement
# Do not remove or change this statement
# Do not remove or change this statement
# Do not remove or change this statement
# Do not remove or change this statement
# Do not remove or change this statement
# Do not remove or change this statement
# Do not remove or change this statement
# Do not remove or change this statement

# Do not change the filename.
# Do not change the folder name.

# Add tests here and push or pull request to testthem on GitHub.
# Format:
# class TestPyEverything(unittest.TestCase):
#     def test_[function_name]():
#         code to test goes here
#         example given below -
#         assert py_everything.maths.add(2, 4) == 6


class TestPyEverything(unittest.TestCase):
    def test_add(self):
        assert pyeMaths.add(2, 4) == 6

    def test_subtract(self):
        assert pyeMaths.subtract(10, 5, 2) == 3

    def test_multiply(self):
        assert pyeMaths.multiply(5, 3, 2) == 30

    def test_divide(self):
        assert pyeMaths.divide(120, 10, "float") == 12.0

    def test_divide_2(self):
        assert pyeMaths.divide(120, 10, "int") == 12

    def test_float_div(self):
        assert pyeMaths.floatDiv(120, 10) == 12.0

    def test_int_div(self):
        assert pyeMaths.intDiv(120, 10) == 12

    def test_mod(self):
        assert pyeMaths.mod(123, 2) == 1

    def test_eval_exp(self):
        assert pyeMaths.evalExp("(2+3-1)*2") == 8

    def test_avg(self):
        assert pyeMaths.avg([2, 4, 6, 8]) == 5

    def test_read_file(self):
        assert pyeFileIO.readFile("read.txt") == 'demo\n'

    def test_write_file(self):
        assert pyeFileIO.writeFile("write.txt", "demo data") is True

    def test_clear_file(self):
        assert pyeFileIO.clearFile("clear.txt") is True

    def test_search_list(self):
        listToTest = ["py", "pypi", "anything", "something",
                      "python", "other", "middlepy", "notmatch", "endpy"]
        assert pyeSearch.searchList(listToTest, "py") == [
            "py", "pypi", "python", "middlepy", "endpy"]

    def test_search_list_2(self):
        listToTest = ["py", "pypi", "anything", "something",
                      "python", "other", "middlepy", "notmatch", "endpy"]
        assert pyeSearch.searchList(listToTest, "py", filter="start") == [
            "py", "pypi", "python"]

    def test_search_list_3(self):
        listToTest = ["py", "pypi", "anything", "something",
                      "python", "other", "middlepy", "notmatch", "endpy"]
        assert pyeSearch.searchList(listToTest, "py", filter="end") == [
            "py", "middlepy", "endpy"]

    def test_search_list_4(self):
        listToTest = ["py", "pypi", "anything", "something",
                      "python", "other", "middlepy", "notmatch", "endpy"]
        assert pyeSearch.searchList(listToTest, "py", filter="exact") == ["py"]

    def test_get_elements_by_id(self):
        assert pyeHtml.getElementsById("app", "index.html") == [
            '<div id="app">something</div>', '<div id="app">something</div>', '<div id=\'app\' class="app">something</div>']

    def test_get_elements_by_class(self):
        assert pyeHtml.getElementsByClass("app", "index.html") == [
            "<p class='app'>something</p>", '<div id=\'app\' class="app">something</div>', "<div class='app'>something</div>"]

    def test_get_element_by_tag(self):
        assert pyeHtml.getElementByTag("p", "index.html") == [
            '<p>something</p>']

    def test_get_element_by_id(self):
        assert pyeHtml.getElementById("app", "index.html") == [
            '<div id="app">something</div>']

    def test_get_element_by_class(self):
        assert pyeHtml.getElementByClass("app", "index.html") == [
            "<p class='app'>something</p>"]


if __name__ == '__main__':
    unittest.main()
