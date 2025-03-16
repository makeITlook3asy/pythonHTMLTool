# Python HTML Generator
## General
The basic idea is to create an html file using Python. For this purpose the following classes are implemented: HTML_File(),Table() and HTML_Elements(). 
Check out example.py to see how the classes can be used. 
## Classes
### HMTL_File()
Contains functions to create the HTML file, add specific HTML elements to it and finally save it. It is very important to use the `create_file(self,titlename:str)`
to save the HTML file after adding all elements with the tab title *titlename*.
```
html_file = HTML_File("test")
```
creates an empty HTML file *test.html*.
Now it is possible to add specific HTML elements (f.e. p,hr,div ...) with content and style attributes to the HTML file. 
For example
```
html_file.add_h_element("Test HTML File","h1")
```
adds *Test HTML File*  as a heading of type h1. 
```
html_file.add_p_element("Item 1",["color:#FF0000"])
```
adds 'Item 1' as a new paragraph in red (#FF0000).
```
html_file.add_div_open_element(["width: 50%","background-color: red"])
```
starts a new div element with the width of 50% and a red background color.
It is very important to add
```
html_file.create_file("test")
```
at the end of the file to save the HTML file with the tab title *test*.
### Table()
Is used to create an HTML table with a specific number of columns.
```
table_1 = Table(3,"Table 1")
```
creates a table with three columns and 'Table 1' as heading.
```
table_1.addHeaderRow(["Information 1","Information 2","Information 3"])
table_1.addRow(["Hello World","Hello there","Hey, how are you?"])
```
adds a header row (bold) and a normal row to the table.
```
table_1.addRow(["info1","info2","info3"],images_at_index={1:"binary_test.png"},width="30%")
```
adds a row with an image (width = 30%) in its second column.
```
html_file.add_div_open_element()
html_file.addTable(table_1.create())
html_file.add_div_close_element()
```
opens a new div element to place the table in it.
### HTML_Elements
Contains HTML elements which are used from the functions of the HTML_File class. For example the `add_h_element(self,element:str,heading_type:str="h2",style_attribs:list=[])` calls 
`h_element(content:str,heading_type:str="h2",style_attribs:list=[])` to create and add a h element with a specific content, heading type (h1,h2 ...) and optional some style attributes.
