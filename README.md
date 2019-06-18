# Overview
Fast office is a lightweight python framwork for office and website automation of windows.

# Install
* Install python3.x first and make sure python is added into PATH.
* Execute install.bat to install requirements
* Current chrome driver version is 74. U can download more Chrome drivers match your Chrome browser from http://chromedriver.chromium.org/downloads

# Coding
Just write python code in main.py and execute it. U can also use compile.bat to compile the main.py to exe.

## Web
* create a web object: web = Web(url)
* click element: web.click(xpath)
* read element value: web.read(xpath)
* write to element: web.write(xpath)
* get source page: web.html()

## Word
* create a word object: word = Word(path)
* replace text: word.replace(old_str, new_str)
* save doc: word.save()

## Excel
* create an Excel object: excel = Excel(path)
* switch the sheet by name: excel.sheet(name)
* switch the sheet by number: excel.sheet(number)
* get cell value: excel.get(row, col)
* write to cell: excel.write(row, col, text)
* save xls: excel.save()
