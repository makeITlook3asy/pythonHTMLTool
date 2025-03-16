from htmlGenerator import HTML_File,HTML_Elements,Table

html_file = HTML_File("test")
html_file.add_h_element("Test HTML File","h1")
html_file.add_hr_element()
html_file.add_div_open_element(["width: 50%","background-color: red"])
html_file.add_p_element("Some relevant information!"*10)
html_file.add_b_element(f"More very important information {HTML_Elements.br_element} Much more stuff")
html_file.add_b_element(f"More very important information {HTML_Elements.br_element} Much more stuff",["color:#ffffff"])
html_file.add_div_close_element()
table_1 = Table(3,"Table 1")
table_1.addHeaderRow(["Information 1","Information 2","Information 3"])
table_1.addRow(["Hello World","Hello there","Hey, how are you?"])
table_1.addRow(["info1","info2","info3"],images_at_index={1:"binary_test.png"},width="30%")
html_file.add_div_open_element()
html_file.addTable(table_1.create())
html_file.add_div_close_element()
html_file.add_div_open_element()
html_file.add_h_element("Some random heading","h4",["color:#fff000","background-color:#000000"])
html_file.add_collapse_start("Collapse Element")
html_file.add_p_element("Item 1",["color:#FF0000"])
html_file.add_p_element("Item 2")
html_file.add_p_element("Item 3")
html_file.add_p_element("Item 4")
html_file.add_collapse_end()
html_file.add_div_close_element()
html_file.create_file("test")