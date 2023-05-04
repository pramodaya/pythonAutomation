from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)


def login():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://breathment.com/home")
    driver.maximize_window()

    # Click the XPath button
    driver.find_element("xpath", '/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]').click()

    links = driver.find_elements("xpath", "//a[@href]")

    for link in links:
        print(link.get_attribute("innerHTML"))
        if ("Login" in link.get_attribute("innerHTML")):
            link.click()
            break

    driver.find_element("xpath",
                              "/html/body/app-root/app-login/section/div/div/div/div/div/form/div[1]/div/input").send_keys(
        'chapzchnz@gmail.com')
    driver.find_element("xpath",
                              "/html/body/app-root/app-login/section/div/div/div/div/div/form/div[2]/div[2]/input").send_keys(
        'password')

    driver.find_element("xpath", '/html/body/app-root/app-login/section/div/div/div/div/div/form/div[3]/button').click()

    print("finished")
