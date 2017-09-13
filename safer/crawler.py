from lxml import etree
from io import StringIO


def parse_html_to_tree(html_string):
    """
    Takes in an HTML string from a request such as request.text, and parses it with etree and returns an ElementTree
    object from lxml


    :param html_string: String of html.
    :return: ElementTree of said html.
    """
    if 'Sorry, no records matching' in html_string or 'BEGIN: No records found error' in html_string:
        return None
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html_string), parser)
    return tree
