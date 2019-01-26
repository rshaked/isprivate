""" Boils beatifulsoup: grab html """

import ast
import requests
from bs4 import BeautifulSoup


def soup_from_name(username):
    """ Grabs bs4 object from html page """
    # html_source = urlopen('https://www.instagram.com/'+ str(username) + '/')
    url = 'https://www.instagram.com/'+ str(username) + '/'
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0)" \
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    html_source = requests.get(url, headers=headers).text
    return BeautifulSoup(html_source, 'html.parser')
    #react-root > section > main > div > div.Nd_Rl._2z6nI > article > div._4Kbb_ > div > h2
    # print(soup.body.span.section.main.div.div.article.div.div.h2)

def soup_to_script_dict(soup):
    """ Returns dict from inside first 'script' object of instagram page """
    for script in soup.body.find_all('script'):
        if 'is_private' in script.string:
            ret = ast.literal_eval(script.string[20:-1].strip().replace(
                'false', 'False').replace(
                    'true', 'True').replace(
                        'null', "'null'"))
            return ret
    return None


def is_private_bool(script_dict):
    """ Returns is_private boolean value from user dictionary object """
    return script_dict['entry_data']['ProfilePage'][0]['graphql']['user']['is_private']

def is_name_private(username):
    """ Public function for getting is_private from username """
    return is_private_bool(
                soup_to_script_dict(
                    soup_from_name(username)))
    # return is_private_bool(
    #     soup_to_script_dict(
    #         soup_from_name(username)))
