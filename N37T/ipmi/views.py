from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.

def get_cookies(request):
    url_html5 = 'https://146.0.241.206/cgi/url_redirect.cgi?url_name=man_ikvm_html5_bootstrap'
    url_mainmenu = 'https://146.0.241.206/cgi/url_redirect.cgi?url_name=mainmenu'
    url_test = 'https://ixi.ru'
    url = 'https://146.0.241.206/cgi/login.cgi'
    data = {'name': 'ADMIN',
            'pwd': 'EP9Mbd7e'}
    with requests.Session() as session:
        session.post(url, data, verify=False)  # авторизуешься
        response = session.get(url_test)  # получаешь данные с другой страницы сайта

    # session = requests.post(url, data=data, verify=False)
    # sid = session.cookies.get_dict()
    # response = HttpResponse('SID: {}'.format(sid['SID']))
    # response.set_cookie('SID', sid['SID'])
    return HttpResponse(response)