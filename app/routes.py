from app import app, models
from flask import render_template
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/berlin-lichtenberg')
def berlinlichtenberg():
    var = get_auslastung_lichtenberg()
    return render_template('berlin-lichtenberg.html', var=var)

@app.route('/berlin-charlottenburg')
def berlincharlottenburg():
    var = get_auslastung_charlottenburg()
    return render_template('berlin-charlottenburg.html', var=var)



def get_auslastung_lichtenberg():
    try:
        url = "https://www.mcfit.com/de/fitnessstudios/studiosuche/studiodetails/studio/berlin-lichtenberg/"
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(url)

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "lxml")

        elems = soup.find_all('div', {'class': 'sc-iJCRLp eDJvQP'})
        # print(elems)
        auslastung = str(elems).split("<span>")[1]
        # print(auslastung)
        auslastung = auslastung[:auslastung.rfind('</span>')]
        print(auslastung)

        ergebnis = {'auslastung': auslastung}

        return ergebnis

    finally:
        try:
            driver.close()
        except:
            pass

def get_auslastung_charlottenburg():
    try:
        url = "https://www.mcfit.com/de/fitnessstudios/studiosuche/studiodetails/studio/berlin-charlottenburg/"
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(url)

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "lxml")

        elems = soup.find_all('div', {'class': 'sc-iJCRLp eDJvQP'})
        # print(elems)
        auslastung = str(elems).split("<span>")[1]
        # print(auslastung)
        auslastung = auslastung[:auslastung.rfind('</span>')]
        print(auslastung)

        ergebnis = {'auslastung': auslastung}

        return ergebnis

    finally:
        try:
            driver.close()
        except:
            pass


