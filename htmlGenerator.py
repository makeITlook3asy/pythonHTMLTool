from typing import Union
class HTML_File():
    def __init__(self,filename:str):
        self.filename = filename if ".html" in filename else filename + ".html"
        self.body_string = ""

    def add_p_element(self,content:str,style_attribs:list=[]):
        self.body_string += f'{HTML_Elements.p_element(content,style_attribs)}'

    def add_b_element(self,content:str,style_attribs:list=[]):
        self.body_string += f'{HTML_Elements.b_element(content,style_attribs)}'

    def add_hr_element(self):
        self.body_string += f'{HTML_Elements.hr_element()}'

    def add_h_element(self,element:str,heading_type:str="h2",style_attribs:list=[]):
        self.body_string += f'{HTML_Elements.h_element(element,heading_type,style_attribs)}'

    def add_div_open_element(self,style_attribs:list=[]):
        self.body_string += f'{HTML_Elements.div_element_open(style_attribs)}'

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
        self.out_file = open(self.filename,'w')
        self.out_file.write(f'<html>\n{HTML_Elements.head_element(titlename)}{HTML_Elements.body_element(self.body_string)}</html>')
        self.out_file.close()


class Table():
    def __init__(self,columns:int,heading:str = ""):
        self.cols = columns
        self.heading = heading
        self.content = f'<h3>{self.heading}</h3>\n<table style="table-layout: fixed; width: 100%;border-collapse: collapse; border: 3px solid black;page-break-inside: avoid;">'

    def addRow(self,text:list,is_bold = False,images_at_index:dict = {},width:str="100%",height:str="100%",color:str="#000000"):
        self.content += "<tr>\n"
        addImg = False
        for i in range(self.cols):
            for key,img in images_at_index.items():
                if i == key:
                    addImg = True
                    img_src = img
            if addImg:
                self.content += f'{HTML_Elements.td_img_elment(img_src,width,height,text[i])}'
                addImg = False
            else:
                self.content += f'{HTML_Elements.td_element(text[i],is_bold,color)}'
        self.content += "</tr>\n"

    def addHeaderRow(self,text:list):
        self.content += "<tr>\n"
        for i in range(self.cols):
            self.content += f'{HTML_Elements.th_element(text[i])}'
        self.content += "</tr>\n"

    def create(self) -> str:
        self.content += "</table>\n"
        return self.content
    
class HTML_Elements():

    br_element = "<br>"

    @staticmethod
    def p_element(content:str,style_attribs:list=[]):
        styles = ' style="' + ";".join(style_attribs) + ';"' if len(style_attribs) > 0 else ""
        return f'<p{styles}>{content}</p>\n'
      
    @staticmethod
    def hr_element():
        return f'<hr>\n'

    @staticmethod
    def b_element(content:str,style_attribs:list=[]):
        styles = ' style="' + ";".join(style_attribs) + ';"' if len(style_attribs) > 0 else ""
        return f'<b{styles}>{content}</b>\n'

    @staticmethod
    def h_element(content:str,heading_type:str="h2",style_attribs:list=[]):
        styles = ' style="' + ";".join(style_attribs) + ';"' if len(style_attribs) > 0 else ""
        return f'<{heading_type}{styles}>{content}</{heading_type}>\n'

    @staticmethod
    def div_element_open(style_attribs:list=[]):
        styles = ' style="' + ";".join(style_attribs) + ';"' if len(style_attribs) > 0 else ""
        return f'<div{styles}>'

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
    def td_element(content:str, is_bold:bool = False,color:str="#000000"):
        font_weight = "normal" if not is_bold else "bold"
        return f'<td style="border: 3px solid black;text-align: center;color: {color}; font-weight: {font_weight}">{content}</td>\n'
    
    @staticmethod
    def td_img_elment(img:str,width:str,height:str,text:str):
        if text == "":
            return_str = f'<td align="center"; style="border: 3px solid black;"><img src="{img}" height={height} width={width}></img></td>'
        else:
            return_str = f'<td align="center"; style="border: 3px solid black;"><div><p>{text}</p><img src="{img}" height={height} width={width}></img></div></td>'
        return return_str
    @staticmethod
    def th_element(content:str,font_weight:str = "bold",color:str="#000000"):
        return f'<th style="border: 3px solid black;text-align: center;color: {color}; font-weight: {font_weight}">{content}</th>\n'
    
    @staticmethod
    def img_element(img:str,width:int, height:int, link:str = ""):
        if link != "":
            img_str = f'<a href={link}><img src="{img}" width="{width}" height="{height}"></a>\n'
        else:
            img_str = f'<img src="{img}" width="{width}" height="{height}">\n'
        return img_str
    

"""
mehr css Gestaltungsmöglichkeiten: hintergrundfarbe, widht, lenght:
    1) beliebige style Attribute können über eine Liste übergeben werden
    2) bestimmte Style Attribute gelten global
    3) Möglichkeit css file zu generieren?
in Tabelle, wenn man Bild einfügt soll es auch möglich sein, darüber Text einzufügen
"""