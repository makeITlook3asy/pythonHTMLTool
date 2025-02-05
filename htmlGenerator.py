from typing import Union
class HTML_File():
    def __init__(self,filename:str):
        self.filename = filename
        self.out_file = open(self.filename + ".html",'w')
        self.body_string = ""

    def add_p_element(self,content:str,color:str = "#FF0000"):
        self.body_string += f'{HTML_Elements.p_element(content,color)}'

    def add_b_element(self,content:str,color:str):
        self.body_string += f'{HTML_Elements.b_element(content,color)}'

    def add_hr_element(self):
        self.body_string += f'{HTML_Elements.hr_element()}'

    def add_h_element(self,element):
        self.body_string += f'{HTML_Elements.h_element(element)}'

    def add_div_open_element(self):
        self.body_string += f'{HTML_Elements.div_element_open()}'

    def add_div_close_element(self):
        self.body_string += f'{HTML_Elements.div_element_close()}'

    def add_collapse_start(self,title:str):
        self.body_string += f'{HTML_Elements.collapse_element_start(title)}'

    def add_collapse_end(self):
        self.body_string += f'{HTML_Elements.collapse_element_end()}'

    def addTable(self,table):
        self.body_string += table

    def addImage(self,image:str,width:str = "auto", height:str = "auto",link:str=""):
        self.body_string += HTML_Elements.img_element(image,width,height,link)

    def create_file(self,titlename:str):
        self.out_file = open(self.filename + ".html",'w')
        self.out_file.write(f'<html>\n{HTML_Elements.head_element(titlename)}{HTML_Elements.body_element(self.body_string)}</html>')
        self.out_file.close()


class Table():
    def __init__(self,heading:str = ""):
        self.heading = heading
        self.content = f'<h3>{self.heading}</h3>\n<table style="table-layout: fixed; width: 100%;border-collapse: collapse; border: 3px solid black;page-break-inside: avoid;">'

    def addRow(self,columns:int,text:list,is_bold = False,images_at_index:list = [],width:str="100%",height:str="100%",color:str="#FF0000"):
        self.content += "<tr>\n"
        for i in range(columns):
            if len(images_at_index) > 0 and i in images_at_index:
                self.content += f'{HTML_Elements.td_img_elment(text[i],width,height)}'
            else:
                self.content += f'{HTML_Elements.td_element(text[i],is_bold,color)}'
        self.content += "</tr>\n"

    def addHeaderRow(self,columns:int,text:list):
        self.content += "<tr>\n"
        for i in range(columns):
            self.content += f'{HTML_Elements.th_element(text[i])}'
        self.content += "</tr>\n"

    def create(self) -> str:
        self.content += "</table>\n"
        return self.content
    
class HTML_Elements():

    br_element = "<br>"

    @staticmethod
    def p_element(content:str,color:str="#FF0000"):
        return f'<p style="color: {color};">{content}</p>\n'
      
    @staticmethod
    def hr_element():
        return f'<hr>\n'

    @staticmethod
    def b_element(content:str,color:str):
        return f'<b style="color: {color};">{content}</b>\n'

    @staticmethod
    def h_element(content:str,heading_type:str="h2"):
        return f'<{heading_type}>{content}</{heading_type}>\n'

    @staticmethod
    def div_element_open():
        return '<div style="page-break-inside: avoid;">'

    @staticmethod
    def div_element_close():
        return '</div>'

    @staticmethod
    def collapse_element_start(title:str):
        return f'<details><summary>{title}</summary>'

    @staticmethod
    def collapse_element_end():
        return '</details>'

    @staticmethod
    def head_element(title:str):
        return f'<head>\n<title>{title}</title>\n</head>\n'
    
    @staticmethod
    def body_element(content:str):
        return f'<body>\n{content}</body>\n'
    
    @staticmethod
    def td_element(content:str, is_bold:bool = False,color:str="#FF0000"):
        font_weight = "normal" if not is_bold else "bold"
        return f'<td style="border: 3px solid black;text-align: center;color: {color}; font-weight: {font_weight}">{content}</td>\n'
    
    @staticmethod
    def td_img_elment(img:str,width:str,height:str):
        return f'<td align="center"; style="border: 3px solid black;"><img src="{img}" height={height} width={width}></img></td>'
    
    @staticmethod
    def th_element(content:str,is_bold:bool=False,color:str="#FF0000"):
        font_weight = "normal" if not is_bold else "bold"
        return f'<th style="border: 3px solid black;text-align: center;color: {color}; font-weight: {font_weight}">{content}</th>\n'
    
    @staticmethod
    def img_element(img:str,width:int, height:int, link:str = ""):
        if link != "":
            img_str = f'<a href={link}><img src="{img}" width="{width}" height="{height}"></a>\n'
        else:
            img_str = f'<img src="{img}" width="{width}" height="{height}">\n'
        return img_str
    

