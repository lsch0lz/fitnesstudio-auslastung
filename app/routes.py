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
    studio = "berlin-lichtenberg"
    var = get_auslastung(studio)
    return render_template('berlin-lichtenberg.html', var=var)

@app.route('/berlin-charlottenburg')
def berlincharlottenburg():
    studio = "berlin-charlottenburg"
    var = get_auslastung(studio)
    return render_template('berlin-charlottenburg.html', var=var)


@app.route('/berlin-lichterfelde')
def berlinlichterfelde():
    studio = "berlin-lichterfelde"
    var = get_auslastung(studio)
    return render_template('berlin-lichterfelde.html', var=var)


@app.route('/berlin-mitte')
def berlinmitte():
    studio = "berlin-mitte"
    var = get_auslastung(studio)
    return render_template('berlin-mitte.html', var=var)





def get_auslastung(studio):
    try:
        url = "https://www.mcfit.com/de/fitnessstudios/studiosuche/studiodetails/studio/"
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(url + studio)

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

