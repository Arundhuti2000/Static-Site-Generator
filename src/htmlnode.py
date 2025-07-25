from typing import List
class HTMLNode:
    def __init__(self, tag:str, value:str, children:List['HTMLNode']=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    def props_to_html(self):
        if not self.props:
            return ""
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"