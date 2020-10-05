from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

class Daten():
    def get_auslastung(self):
        try:
            url="https://www.mcfit.com/de/fitnessstudios/studiosuche/studiodetails/studio/berlin-lichtenberg/"
            options = FirefoxOptions()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            driver.get(url)

            html_content = driver.page_source
            soup = BeautifulSoup(html_content, "lxml")

            elems = soup.find_all('div', {'class': 'sc-iJCRLp eDJvQP'})
            #print(elems)
            auslastung = str(elems).split("<span>")[1]
            #print(auslastung)
            auslastung = auslastung[:auslastung.rfind('</span>')]
            print(auslastung)

            ergebnis = {'auslastung': auslastung}
            return ergebnis

        finally:
            try:
                driver.close()
            except:
                pass

        return self.get_auslastung()


#bot = Daten()
#bot.get_auslastung()
