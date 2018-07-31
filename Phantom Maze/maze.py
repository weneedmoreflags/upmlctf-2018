import requests, re

session   = requests.Session()

url  = 'https://maze.ctf.upml.tech/%s'

startText = session.get(url % '').text
startUrl  = re.findall('([a-zA-Z0-9]{32})', startText)[0]
urls      = [startUrl]

while True:
    r = session.post(url % 'next', data = {'id': urls[-1]})
    urls.append(r.text); print(urls[-1]); 
    text = session.get(url % ('maze/%s' % urls[-1])).text
    if 'Go to the next room' not in text or 'flag' in text.lower() or 'uctf' in text.lower(): 
        print(text)
        break
