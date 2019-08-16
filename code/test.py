from selenium import webdriver
capabilities = {
  'chromeOptions': {
    'androidPackage': 'com.android.chrome',
  }
}
driver = webdriver.Remote('http://localhost:9515', capabilities)
driver.get('http://google.com')
driver.quit()
