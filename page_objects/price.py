import re

from bs4 import BeautifulSoup

from page_objects.page_object import PageObj


class Price(PageObj):
    
    def _price_cut_off(self, line: str):
        pattern = r"^((\s*\d*)*)₽"
        try:
            res = re.search(pattern, line)
            res = re.sub(r'\D', '', res.group(1))
            return int(res)
        except Exception:
            print('_price_cut_off: ERROR')


    def _parse_price(self):
        processed_page = BeautifulSoup(self.get_page(), 'html.parser')
        try:
            res = processed_page.find('div', class_='a1-a5').get_text()
            return self._price_cut_off(res)
        except Exception:
            print('Uncorrect link')


    @property
    def now(self):
        return self._parse_price()
