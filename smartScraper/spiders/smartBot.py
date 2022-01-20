from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
from selenium import webdriver
from time import sleep

class smartBot():
  def __init__(self, response):
    self.response = response

  def render(self, request):
    if 'js_instructions' in request:
      if 'driver' in self.response.request.meta:
        self.driver = self.response.request.meta['driver']
      else:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        self.driver  = webdriver.Chrome(options=options)
        self.driver.get(self.response.request.url)
      for command in request['js_instructions']:
        for key, value in command.items():
          self.executeScript(key, value)
      new_response = HtmlResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
      self.driver.close()
      return new_response
    return self.response

  def executeScript(self, key, value):
    try:
      if key=='click':
        self.driver.find_element(By.CSS_SELECTOR, value).click()
      elif key=='wait':
        sleep(value)
      elif key=='scroll_down':
          self.driver.execute_script(f"window.scrollTo(0, {value})")
      elif key=='fill':
          self.driver.find_element(By.CSS_SELECTOR, value[0]).send_keys(value[1])
      elif key=="run_script":
          self.driver.execute_script(value)
    except NoSuchElementException:
      pass
