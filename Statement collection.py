import json
from datetime import datetime

from lxml.html import fromstring, tostring
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    links = []
    driver = webdriver.Firefox(executable_path=)
    first = True
    for i in links:
        driver.get(i)
        pages = []
        speeches_links = []
        new_speeches_links = []
        start_date = datetime(2019, 1, 1)
        end_date = datetime(2022, 12, 31)
        while True:
            try:
                html = fromstring(driver.page_source)
                rows = html.xpath('//*[@id="statementsObjectsTables"]/tbody/tr')
                flag = False
                for row in rows:
                    row = fromstring(tostring(row))
                    cells = row.xpath('//td')
                    date_str = "".join((cells[0].xpath('text()')[0]).split())
                    print(date_str)
                    date = datetime.strptime(date_str, '%m/%d/%Y')

                    if start_date <= date <= end_date:
                        Senator = {
                            'date': date_str,
                            'title': cells[1].xpath('a/text()')[0],
                            'link': cells[1].xpath('a/@href')[0]
                        }
                        speeches_links.append(Senator)
                        print(Senator)
                    if date < start_date:
                        flag = True
                        break
                    if date > start_date:
                        pass
                if flag:
                    break
                next_button = driver.find_elements(By.XPATH, '//li[@class="page-item"]/a')[-1]
                next_button.click()

                try:
                    extra_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable(
                            driver.find_element(By.XPATH, '//*[@id="helpusPopUpNoThanksQuote"]')))
                    extra_button.click()
                except NoSuchElementException:
                    pass
                except TimeoutException:
                    pass
                except StaleElementReferenceException:
                    pass
                except ElementClickInterceptedException:
                    pass

            except NoSuchElementException:
                break


        save_json(, speeches_links)

    driver.close()
