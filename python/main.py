from os.path import abspath, join
from re import sub
from xml.dom.minidom import parse, Document, Element

ROOT = abspath('../')

INPUT_FILE = join(ROOT, 'input.svg')
OUTPUT_FILE = join(ROOT, 'output.svg')


def main():
    with parse(INPUT_FILE) as dom:
        dom: Document
        svg: Element = dom.firstChild
        svg.setAttribute('width', '100%')
        svg.removeAttribute('content')
        svg.removeAttribute('onclick')
        svg.removeAttribute('style')

        content: str = svg.toprettyxml(indent='', newl='')
        content = sub('\n\s*', '', content)

        with open(OUTPUT_FILE, 'w') as f:
            f.write(content)

main()
