# Docs

## Basic Usage
The basic usage for this package is given below

```python
>>> import py_everything
>>> from py_everything import search
>>> search.search_files('python', 'C:\Programming\\')
C:\Programming\python.txt
C:\Programming\python_project.py
C:\Programming\python_py_everything.docx
>>> my_list = [2, 4, 5, 3, 7, 5, 6, 3 , 12 , 9, 6]
>>> py_everything.maths.avg(my_list)
5.636363636363637
```

## Detailed Packages List
## Packages:
- `py_everything`
- `py_everything.automation`
- `py_everything.date_utils`
- `py_everything.fileIO`
- `py_everything.maths`
- `py_everything.requestsLib`
- `py_everything.search`
- `py_everything.web`

## Functions:
### py_everything:
- `hello_world`
- `print_no_newline`
- `clearPycache`
- `install_modules`

### py_everything.automation:
- `email_bot`
- `email_address_slicer`
- `yt_downloader`
- `roll_dice`
- `timer`

### py_everything.date_utils:
- `get_date`
- `get_date_time`
- `get_time`
- `get_custom_format`

### py_everything.fileIO:
- `read_file`
- `write_file`
- `clear_file`

### py_everything.maths:
- `add`
- `subtract`
- `multiply`
- `divide`
- `float_div`
- `int_div`
- `expo`
- `mod`
- `eval_exp`
- `avg`

### py_everything.requestsLib:
- `getR`
- `postR`
- `putR`
- `deleteR`
- `patchR`
- `optionsR`
- `headR`
- `getContent`
- `getText`
- `getJson`
- `getHeader`
- `getSpecificHeader`

### py_everything.search:
- `search_files`
- `search_dirs`
- `search_exts`
- `search_list`

### py_evrything.web:
- `google_search`
- `yt_search`
- `github_search`
- `so_search`
- `amz_in_search`
- `amz_com_search`
- `pypi_search`
- `rtdocs_search`
- `open_new_tab`
- `open_new_window`

## Classes:
### py_everything.date_utils:
- `Date`

### py_everything.fileIO:
- `FileIOBase`

### py_everything.maths:
- `MathsBase`
- `MathsAdvanced`

### py_everything.requestsLib:
- `ReqLibBase`
- `ReqLibAdvanced`

### py_everything.web:
- `webSearchBase`
- `webSearchAdvanced`
