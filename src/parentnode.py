from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
    def to_html(self):
        if not self.tag:
            raise ValueError("All parents must have a tag")
        if self.children == None:
            return ValueError("All parents must have a children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{self.children}</{self.props}>"
    def __repr__(self): 
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"                               