import time
from PageObjects.home import MainPage
from PageObjects.product import ProductPage
from PageObjects.registration import RegistrationPage
from conf import *
from conftest import *


def screen(driver):
    driver.get(website)
    time.sleep(1)
    main_page = MainPage(driver)
    main_page.click(MainPage.PRODUCTS[0])
    time.sleep(1)
    product_page = ProductPage(driver)
    product_page.click(ProductPage.MAIN_PICTURE)
    time.sleep(1)
    product_page.kaka(3)
    time.sleep(2)


def korzina(driver):
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.PRODUCTS_BUTTON_BUY[0])
    main_page.click(MainPage.PRODUCTS_BUTTON_BUY[1])
    main_page.click(MainPage.BUTTON_CART)
    time.sleep(3)


def pipupa(driver):
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.DROPDOWN_PC)
    main_page.click(MainPage.LI_PC)
    time.sleep(3)


def amogus(driver):
    driver.get(website)
    main_page = MainPage(driver)
    main_page.click(MainPage.BUTTON_REGLOG)
    main_page.click(MainPage.BUTTON_REGISTER)
    registration_page = RegistrationPage(driver)
    registration_page.registration()
    registration_page.click(RegistrationPage.BUTTON_TRUE_SUBNEWS)
    registration_page.click(RegistrationPage.BUTTON_ACCEPTANCE)
    registration_page.click(RegistrationPage.BUTTON_NEXT)
    time.sleep(3)


def sosiska(driver):
    driver.get(website)
    main_page = MainPage(driver)
    main_page.Pinput(MainPage.INPUT_SEARCH, "search")
    main_page.enter()
    time.sleep(3)


def favs(driver):
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    index = main_page.random(MainPage.PRODUCTS)
    main_page.click(MainPage.PRODUCTS_BUTTON_FAVORITE[index])
    time.sleep(3)


def cams(driver):
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.PRODUCTS[MainPage.LAST_INDEX])
    product_page = ProductPage(driver)
    product_page.click(ProductPage.SELECT_OPTION_COLOR)
    product_page.click(ProductPage.BUTTON_BUY)


def planshetik(driver):
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.DROPDOWN_TABLET)
    main_page.click(MainPage.PRODUCT_TABLET)
    product_page = ProductPage(driver)
    product_page.click(ProductPage.BUTTON_BUY)


def HTC(driver):
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.DROPDOWN_TELEPHONE_HTC)
    main_page.click(MainPage.PRODUCT_TELEPHONE_HTC)
    product_page = ProductPage(driver)
    product_page.click(ProductPage.BUTTON_BUY)


def rew(driver):
    driver.get(website)
    main_page = MainPage(driver)
    main_page.click(MainPage.PRODUCTS[0])
    product_page = ProductPage(driver)
    product_page.click(ProductPage.BUTTON_REVIEW)
    product_page._input(ProductPage.INPUT_NAME_REVIEW, first)
    product_page._input(ProductPage.INPUT_REVIEW, reviewt)
    product_page.click(ProductPage.BUTTON_REVIEW_MARK[4])
    product_page.click(ProductPage.BUTTON_NEXT_REVIEW)
    time.sleep(3)


screen(driver)
korzina(driver)
pipupa(driver)
amogus(driver)
sosiska(driver)
favs(driver)
cams(driver)
planshetik(driver)
HTC(driver)
rew(driver)


