from bs4 import BeautifulSoup
import urllib3


def main(url, syntax, attrs):
    """Acquire values of indexes from the SET website. Use "Inspect" option in modern web browsers to find the right
    combinations of syntax and attrs.

    :param url: Complete URL
    :type url: str
    :param syntax: HTML syntax
    :type syntax: str
    :param attrs: Attributes in the HTML syntax that you are looking for.
    :type attrs: dict
    :return: Value of the specified index.
    """
    http = urllib3.PoolManager()
    content = http.request('GET', url)
    soup = BeautifulSoup(content.data, "html.parser")
    target_element = soup.find(syntax, attrs=attrs)
    target_element_next = target_element.find_next('td')
    value = target_element_next.contents[0]

    return value


if __name__ == '__main__':
    # Configurations
    set_url = 'https://www.settrade.com/C13_MarketSummary.jsp'
    target_syntax = 'a'
    target_attrs = {"href": "/C13_MarketSummary.jsp?detail=SET50", "class": "link-stt"}

    val = main(set_url, target_syntax, target_attrs)

    # Report
    print('According to: ' + set_url)
    print('The current SET50 value is: ' + str(val))
    # According to: https://www.settrade.com/C13_MarketSummary.jsp
    # The current SET50 value is: 981.60

