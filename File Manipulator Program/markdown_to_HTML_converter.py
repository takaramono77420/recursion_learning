import sys
import markdown

def markdown_to_HTML_converter(markdown_file, html_file):

    contents = ''

    with open(markdown_file, 'r', encoding='utf-8') as f:
        contents = f.read()
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(markdown.markdown(contents))


def __main__(argv):
    
    markdown_to_HTML_converter(argv[1], argv[2])


if __name__ == "__main__":
    __main__(sys.argv)