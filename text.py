from bs4 import BeautifulSoup
from requests import get


url = 'https://en.wikipedia.org/wiki/Naruto'
htmlString = get(url).text
html = BeautifulSoup(htmlString, 'lxml')
entries = html.find_all('div', {'class':'entry-body'})
text = [e.get_text() for e in entries]
print '{} posts were found.'.format(len(text))
print text[0]