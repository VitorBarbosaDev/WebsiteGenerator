from htmlnode import HTMLNode


class LEAFNode(HTMLNode):
    def __init__(self,tag: str ,value: str ,props: dict | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if(self.value is None):
            raise ValueError

        if(self.tag is None):
            return self.value

        if(self.props is None or self.props == {}):
            return f"<{self.tag}>{self.value}</{self.tag}>"

        propString=""
        i= 0
        for key, value in self.props.items():
            if(i>0):
                propString += f" "
            propString += f"{key}=\"{value}\""
            i+=1
             
        return f"<{self.tag} {propString}>{self.value}</{self.tag}>"


    def __repr__(self):
                return f"LEAFNode({self.tag}, {self.value},{self.props})"
    
    def __eq__(self, other):
          if not isinstance(other, LEAFNode):
            return NotImplemented
    
          return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
          )