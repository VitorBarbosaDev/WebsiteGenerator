

class HTMLNode():
    def __init__(self,  tag: str | None = None,value: str | None = None,children: list | None = None,props: dict | None = None):
            self.tag = tag
            self.value = value
            self.children = children
            self.props = props

    def to_html(self):
          raise NotImplementedError

    def props_to_html(self):
        new_Str = ""

        for p in self.props:
              new_Str+= p

        return new_Str

    def __repr__(self):
            return f"HTMLNode({self.tag}, {self.value}, {self.children},{self.props})"

    def __eq__(self, other):
      if not isinstance(other, HTMLNode):
        return NotImplemented

      return (
        self.tag == other.tag
        and self.value == other.value
        and self.children == other.children
        and self.props == other.props
      )