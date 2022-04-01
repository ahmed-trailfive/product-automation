import os
import random
import shutil
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from apps.firestore.db import DatabaseInitialize
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class GoogleStorageImage:
    """
    This class handles Image Downloading from Google Storage
    """

    # download image from google storage
    def download_image(self, url: str, path: str) -> None:
        try:
            response = requests.get(url, stream=True)
            with open(path, "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
        except Exception as e:
            # log the error
            print(e)


class ProxyServers:
    """
    This class handles Proxy Servers
    """

    # add the list of proxies
    proxies = [
        "167.172.248.53:3128",
        "194.226.34.132:5555",
        "203.202.245.62:80",
        "141.0.70.211:8080",
        "118.69.50.155:80",
        "201.55.164.177:3128",
        "51.15.166.107:3128",
        "91.205.218.64:80",
        "128.199.237.57:8080",
    ]
    # return a random proxy
    def get_proxy(self) -> str:
        return random.choice(self.proxies)

    # return the proxy list
    def get_proxy_list(self) -> list:
        return self.proxies


class SeleniumDriver:
    """
    This class handles chrome driver
    """

    # initialize the driver
    def __init__(self, proxy_server: bool = False, headless: bool = True):
        # set the chrome options
        chrome_options = Options()
        if proxy_server:
            proxy = ProxyServers().get_proxy()
            chrome_options.add_argument(f"--proxy-server={proxy}")
        if headless:
            chrome_options.add_argument("--headless")
        # set the chrome driver
        try:
            self.driver = webdriver.Chrome(
                service=Service(os.path.abspath("apps/product/selenium/chromedriver")),
                options=chrome_options,
            )
        except Exception as e:
            print(e)

    def open(self, url: str):
        """open the url"""
        self.driver.get(url)
        return self.driver

    def get_page_source(self):
        """get the page source"""
        return self.driver.page_source

    def get_page_title(self):
        """get the page title"""
        return self.driver.title

    def get_url(self):
        """get the url"""
        return self.driver.current_url


class Automation:
    """
    Automate the process of posting ads on sprzedajemy.pl
    """

    website = "https://sprzedajemy.pl/nowe-ogloszenie/kategoria/10692"
    title_xpath = "//*[@id='title']"
    description_xpath = "//*[@id='description']"
    price_xpath = "//*[@id='price']"
    file_upload_xpath = "//*[@id='fileUpload']"

    def __init__(self, request):
        self.collection = request.app.db.get_collections()

    def put_input_elements(
        self, title: str, description: str, price: str, image: list
    ) -> None:
        """put the data in the input elements

        Args:
            title (string): title of the product
            description (string): description of the product
            price (string): description of the product
            image (List): List of images
        """
        driver = SeleniumDriver().open(self.website)
        input_title = driver.find_element(by=By.XPATH, value=self.title_xpath)
        input_description = driver.find_element(
            by=By.XPATH, value=self.description_xpath
        )
        input_price = driver.find_element(by=By.XPATH, value=self.price_xpath)
        input_image = driver.find_element(by=By.XPATH, value=self.file_upload_xpath)

        # set the values
        input_title.send_keys(title)
        input_description.send_keys(description)
        input_price.send_keys(price)
        for i in image:
            try:
                # download image from google storage store in current directory
                path = i.rsplit("/", 1)[-1]
                GoogleStorageImage.download_image(i, path)
                # upload image to form
                input_image.send_keys(abspath + path)
            except:
                # upload not available iamge
                abspath = os.path.abspath(os.getcwd())
                input_image.send_keys(abspath + "/notavailable.png")

        driver.close()

    # def get_data(self, max_threads: int = 2) -> None:
    #     """create threads for each collection

    #     Args:
    #         max_threads (int, optional): number of threads to create at a time. Defaults to 2.
    #     """
    #     for i in self.collection:
    #         docs = self.db.get_documents(i.id)
    #         with concurrent.futures.ThreadPoolExecutor(
    #             max_workers=max_threads
    #         ) as executor:
    #             for doc in docs:
    #                 data = doc.to_dict()
    #                 title = data["title"]
    #                 description = data["description"]
    #                 price = data["price"]
    #                 image = data["images"]
    #                 executor.submit(
    #                     self.put_input_elements, title, description, price, image
    #                 )


# auto = Automation()
# auto.get_data()
