from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  
    options.add_argument("--start-maximized")  

    
    context.browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    
    context.browser.execute_script("document.body.style.zoom='100%'")


def after_all(context):
    
    context.browser.quit()