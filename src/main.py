#./main.sh
# hello world
from textnode import TextNode,TextType
print("hello world")


def main():
    textNode=TextNode("This is some anchor text", TextType.Link, "https://www.boot.dev")
    print(textNode)














if __name__ == "__main__":
    main()