import unittest
import sys
import scriptscreentopzapros
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("https://www.google.ru/")

    def test_fullpage_screenshot(self):
        poisk = self.driver.find_element(By.XPATH, "//input[@type='text']")
        # мтс
        poisk.send_keys('мтс интернет тарифы')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/mtsinettariff.png")
        self.driver.back()
        poisk.send_keys('мтс подключить интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/mtspodklinet.png")
        self.driver.back()
        poisk.send_keys('мтс тарифы 2023')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/mtstariff2023.png")
        self.driver.back()
        poisk.send_keys('мтс домашний интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/mtshouseinet.png")
        self.driver.back()
        poisk.send_keys('тарифные планы мтс')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/tariffplanmts.png")
        self.driver.back()
        poisk.send_keys('выгодные тарифы мтс')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/vygodtariffmts.png")
        self.driver.back()
        poisk.send_keys('мтс домашний интернет и тв')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/mtshouseinetitv.png")
        self.driver.back()
        poisk.send_keys('тарифы мтс на интернет и телевидение')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/tariffmtsnainetitelevid.png")
        self.driver.back()
        poisk.send_keys('мтс домашний интернет тарифы')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтс/mtshouseinettariff.png")
        self.driver.back()

        # билайн
        poisk.send_keys('билайн домашний интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/билайн/bilhouseinet.png")
        self.driver.back()
        poisk.send_keys('тарифы билайн 2023 с интернетом')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/билайн/tariffbil2023sinet.png")
        self.driver.back()
        poisk.send_keys('билайн интернет тарифы')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/билайн/bilinettariff.png")
        self.driver.back()
        poisk.send_keys('beeline домашний интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/билайн/beelhouseinet.png")
        self.driver.back()
        poisk.send_keys('билайн тв и интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/билайн/biltviinet.png")
        self.driver.back()
        poisk.send_keys('скорость интернета билайн')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/билайн/skorostinetabil.png")
        self.driver.back()

        # домру
        poisk.send_keys('дом ру интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/домру/domruinet.png")
        self.driver.back()
        poisk.send_keys('дом ру тарифы')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/домру/domrutariff.png")
        self.driver.back()
        poisk.send_keys('дом ру интернет тарифы')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/домру/domruinettariff.png")
        self.driver.back()
        poisk.send_keys('дом ру интернет и телевидение')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/домру/domruinetitelev.png")
        self.driver.back()
        poisk.send_keys('подключить интернет дом ру')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/домру/podklinetdomru.png")
        self.driver.back()
        poisk.send_keys('dom ru интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/домру/domruuinet.png")
        self.driver.back()
        poisk.send_keys('подключить дом ру')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/домру/podkldomru.png")
        self.driver.back()

        # ростелеком
        poisk.send_keys('ростелеком интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/ростелеком/rostelekinet.png")
        self.driver.back()
        poisk.send_keys('домашний интернет ростелеком')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/ростелеком/houseinetrostelek.png")
        self.driver.back()
        poisk.send_keys('ростелеком тарифы на интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/ростелеком/rostelektariffnainet.png")
        self.driver.back()
        poisk.send_keys('ростелеком подключение интернета')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/ростелеком/rostelekpodklinet.png")
        self.driver.back()
        poisk.send_keys('ростелеком интернет и тв')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/ростелеком/rostelekinetitv.png")
        self.driver.back()
        poisk.send_keys('тарифы ростелеком 2023')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/ростелеком/tariffrostelek2023.png")
        self.driver.back()
        poisk.send_keys('ростелеком тарифы на интернет и телевидение')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/ростелеком/rostelektariffnainetitelev.png")
        self.driver.back()
        poisk.send_keys('ростелеком тарифы и цены')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/ростелеком/rostelektariffiprice.png")
        self.driver.back()

        # мегафон
        poisk.send_keys('мегафон домашний интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мегафон/megafonhouseinet.png")
        self.driver.back()
        poisk.send_keys('мегафон интернет для дома')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мегафон/megafoninetdlydoma.png")
        self.driver.back()
        poisk.send_keys('домашний интернет мегафон тарифы')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мегафон/houseinetmegafontariff.png")
        self.driver.back()
        poisk.send_keys('мегафон домашний интернет и телевидение')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мегафон/megafomhouseinetitelevid.png")
        self.driver.back()
        poisk.send_keys('мегафон акции')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мегафон/megafonakcii.png")
        self.driver.back()
        poisk.send_keys('домашний интернет мегафон отзывы')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мегафон/houseinetmegadonotzyv.png")
        self.driver.back()

        # мгтс
        poisk.send_keys('мгтс тарифы')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мгтс/mgtstariff.png")
        self.driver.back()
        poisk.send_keys('домашний интернет мгтс')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мгтс/houseinetmgts.png")
        self.driver.back()
        poisk.send_keys('мгтс акции')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мгтс/mgtsakcii.png")
        self.driver.back()
        poisk.send_keys('мгтс тарифы на интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мгтс/mgtstariffnainet.png")
        self.driver.back()
        poisk.send_keys('мгтс тарифы на интернет домашний')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мгтс/mgtstariffnainethouse.png")
        self.driver.back()
        poisk.send_keys('мгтс интернет и тв')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мгтс/mgtsinetitv.png")
        self.driver.back()

        # мтсhome
        poisk.send_keys('mts home интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтсhome/mtshomeinet.png")
        self.driver.back()
        poisk.send_keys('mts home')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтсhome/mtshome.png")
        self.driver.back()
        poisk.send_keys('мтс хоум')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтсhome/mtshoum.png")
        self.driver.back()
        poisk.send_keys('тарифы мтс хоум')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтсhome/tariffmtshoum.png")
        self.driver.back()
        poisk.send_keys('мтс хоме интернет')
        poisk.send_keys(Keys.ENTER)
        scriptscreentopzapros.fullpage_screenshot(self.driver,
                                                  "C:/Users/Марина/OneDrive/Рабочий стол/топзапрос/мтсhome/mtshomeeinet.png")
        self.driver.back()


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])

