import unittest
import sys
import scriptscreencite
from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def test_fullpage_screenshot(self):
        self.driver.get("https://www.moskvaonline.ru/")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/msk.png")
        self.driver.get("https://www.moskvaonline.ru/about/contacts")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/aboutcontacts.png")
        self.driver.get("https://www.moskvaonline.ru/about/partners")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/partners.png")
        self.driver.get("https://www.moskvaonline.ru/about/personal-data")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/personal-data.png")
        self.driver.get("https://www.moskvaonline.ru/about/terms-of-use")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/terms-of-use.png")
        self.driver.get("https://www.moskvaonline.ru/actions")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/actions.png")
        self.driver.get("https://www.moskvaonline.ru/address")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/address.png")
        self.driver.get("https://www.moskvaonline.ru/articles")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/articles.png")
        self.driver.get("https://www.moskvaonline.ru/exclusive")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/exclusive.png")
        self.driver.get("https://www.moskvaonline.ru/orders/home?tariff_id=100055013")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/zayvkapodkl.png")
        self.driver.get("https://www.moskvaonline.ru/rates?house_id=147748")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/inetitv.png")
        self.driver.get("https://www.moskvaonline.ru/nomera")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomera.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/vip")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomeravip.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/iz-dvuh-cifr")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomeraiz-dvuh-cifr.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/nomera-8800")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomera-8800.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/zolotoj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomerazolotoj.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/besplatnye")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomerabesplatnye.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/platinovyj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomeraplatinovyj.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/serebrjanyj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomeraserebrjanyj.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/federalnye")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomerafederalnye.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/bronzovyj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomerabronzovyj.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/actions")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonactions.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomera.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera/iz-dvuh-cifr")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomeraiz-dvuh-cifr.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera/nomera-8800")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomeranomera-8800.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera/zolotoj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomerazolotoj.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera/besplatnye")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomerabesplatnye.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera/platinovyj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomeraplatinovyj.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera/serebrjanyj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomeraserebrjanyj.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera/federalnye")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomerafederalnye.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/nomera/bronzovyj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonnomerabronzovyj.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobile.png")
        self.driver.get("https://www.moskvaonline.ru/nomera/bronzovyj")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/nomerabronzovyj.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/bezlimitnyj-internet")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobilebezlimitnyj-internet.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/mezhdunarodnye")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobilemezhdunarodnye.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/dlja-plansheta")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobiledlja-plansheta.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/dlja-modema")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobiledlja-modema.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/4g")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobile4g.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/3g")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobile3g.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/bezlimitnaja-svjaz")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobilebezlimitnaja-svjaz.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/po-rossii")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobilepo-rossii.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon/ratesmobile/esim")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafonratesmobileesim.png")
        self.driver.get("https://www.moskvaonline.ru/operatory/megafon")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatorymegafon.png")
        self.driver.get("https://www.moskvaonline.ru/operatory")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/operatory.png")
        self.driver.get("https://www.moskvaonline.ru/orders/home?tariff_id=102782009")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/zayavka.png")
        self.driver.get("https://www.moskvaonline.ru/orders/office")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/office.png")
        self.driver.get("https://www.moskvaonline.ru/orders/sat")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/sat.png")
        self.driver.get("https://www.moskvaonline.ru/orders/tohome")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/tohome.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/domashnij-internet")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesdomashnij-internet.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/internet-100-mbit")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesinternet-100-mbit.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/internet-300-mbit")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesinternet-300-mbit.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/internet-500-mbit")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesinternet-500-mbit.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/internet-i-mobilnaya-svyaz")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesinternet-i-mobilnaya-svyaz.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/internet-i-tv")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesinternet-i-tv.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/internet-tv-mobile")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesinternet-tv-mobile.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/nedorogoj-domashnij-internet")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesnedorogoj-domashnij-internet.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates/online-kinoteatr")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonratesonline-kinoteatr.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon/rates")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafonrates.png")
        self.driver.get("https://www.moskvaonline.ru/providers/megafon")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providersmegafon.png")
        self.driver.get("https://www.moskvaonline.ru/providers")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/providers.png")
        self.driver.get("https://www.moskvaonline.ru/rates?house_id=2801124")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ineeetitv.png")
        self.driver.get("https://www.moskvaonline.ru/rates")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/rates.png")
        self.driver.get("https://www.moskvaonline.ru/rates?house_id=2801124&filter=domashniy-internet")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/rateshouse_id=2801124&filter=domashniy-internet.png")
        self.driver.get("https://www.moskvaonline.ru/rates?filter=internetAndTV&house_id=2801124")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesfilter=internetAndTV&house_id=2801124.png")
        self.driver.get("https://www.moskvaonline.ru/rates?filter=onlyTV&house_id=2801124")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesfilter=onlyTV&house_id=2801124.png")
        self.driver.get("https://www.moskvaonline.ru/rates?filter=bezlimitniy-intenet&house_id=2801124")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesfilter=bezlimitniy-intenet&house_id=2801124.png")
        self.driver.get("https://www.moskvaonline.ru/rates?filter=mobile&house_id=2801124")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesfilter=mobile&house_id=2801124.png")
        self.driver.get("https://www.moskvaonline.ru/rates/domashnij-internet")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesdomashnij-internet.png")
        self.driver.get("https://www.moskvaonline.ru/rates/internet-i-mobilnaya-svyaz")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesinternet-i-mobilnaya-svyaz.png")
        self.driver.get("https://www.moskvaonline.ru/rates/internet-tv-mobile")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesinternet-tv-mobile.png")
        self.driver.get("https://www.moskvaonline.ru/rates/domashnij-internet")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesdomashnij-internet.png")
        self.driver.get("https://www.moskvaonline.ru/rates/internet-i-tv")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesinternet-i-tv.png")
        self.driver.get("https://www.moskvaonline.ru/rates/nedorogoj-domashnij-internet")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesnedorogoj-domashnij-internet.png")
        self.driver.get("https://www.moskvaonline.ru/rates/internet-100-mbit")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesinternet-100-mbit.png")
        self.driver.get("https://www.moskvaonline.ru/rates/internet-300-mbit")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesinternet-300-mbit.png")
        self.driver.get("https://www.moskvaonline.ru/rates/internet-500-mbit")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesinternet-500-mbit.png")
        self.driver.get("https://www.moskvaonline.ru/rates/online-kinoteatr")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesonline-kinoteatr.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobile.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/dlja-noutbuka")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobiledlja-noutbuka.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/bez-abonentskoj-platy")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobilebez-abonentskoj-platy.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/bezlimitnaja-svjaz")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobilebezlimitnaja-svjaz.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/3g")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobile3g.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/perenos_nomera")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobileperenos_nomera.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/4g")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobile4g.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/vygodnye")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobilevygodnye.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/po-rossii")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobilepo-rossii.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/esim")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobileesim.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/dlja-modema")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobiledlja-modema.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/dlja-plansheta")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobiledlja-plansheta.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/mezhdunarodnye")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobilemezhdunarodnye.png")
        self.driver.get("https://www.moskvaonline.ru/ratesmobile/bezlimitnyj-internet")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesmobilebezlimitnyj-internet.png")
        self.driver.get("https://www.moskvaonline.ru/rates/internet-i-mobilnaya-svyaz")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesinternet-i-mobilnaya-svyaz.png")
        self.driver.get("https://www.moskvaonline.ru/rates/internet-tv-mobile")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/ratesinternet-tv-mobile.png")
        self.driver.get("https://www.moskvaonline.ru/rating")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/rating.png")
        self.driver.get("https://www.moskvaonline.ru/reviews")
        scriptscreencite.fullpage_screenshot(self.driver, "C:/Users/Марина/OneDrive/Рабочий стол/релиз/мол/пк/reviews.png")


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])