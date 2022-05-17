from bs4 import BeautifulSoup

from flask import Flask, jsonify, make_response
import requests
import os
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
app = Flask(__name__)

@app.route("/")
def index():
    return "whois simple json api"

@app.route('/<email>')
def get_whois(email):

    try:
        URLicq = "https://icq.im/" + email

        raq = requests.get(URLicq, headers=HEADERS)
        soup = BeautifulSoup(raq.content, 'html.parser')
        items = soup.findAll('div', class_='icq-profile__box')
        items2 = soup.findAll('div', class_=f'icq-profile__avatar')

        icqs = []

        for item in items:
            name = item.find('h2', class_='icq-profile__name').get_text(strip=True)
            avalink = item.find('div', class_=f'icq-profile__avatar')

        name = f'{name}'
        avalink = f'{avalink}'
        avalink = avalink.replace(f'<div class="icq-profile__avatar" style="background-image: url(', f'').replace(f')"></div>', f'').replace(f"'", f'').replace("&amp;", "&")

        if not 'https' in avalink:
            avalink = f"https://agent.mail.ru{avalink}"


        for item in items:
            icqs.append({'status': 'ok'})
            icqs.append({'name': name})
            icqs.append({'avalink': avalink})
            icqs.append({'URLicq': URLicq})
        print(icqs)
        return f'{icqs}'

    except:
        icqs.append({'status': 'Error'})
        icqs.append({'name': ''})
        icqs.append({'avalink': ''})
        icqs.append({'URLicq': ''})
        print(icqs)
        return f'{icqs}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
