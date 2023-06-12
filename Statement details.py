import json
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def save_json(path, file):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file, f, indent=4)



urls = []
with open() as f:
    data = json.load(f)


driver = webdriver.Firefox(executable_path=)
first = True
main_dir =
count = len(os.listdir(main_dir))
i = len(os.listdir(main_dir))
for element in data:
    link = element["link"]
    if link in urls:
        continue
    else:
        urls.append(link)
    count += 1
    i += 1
    driver.get(link)
    try:
        extra_button = driver.find_element(By.XPATH, '//*[@id="helpusPopUpNoThanksQuote"]')
        extra_button.click()
    except Exception as err:
        print('No pop-up')

    try:
        local = driver.find_elements(By.XPATH, value='//div[@class="col"]/span')
        problem = driver.find_elements(By.XPATH, value='//a[@class="badge badge-pill badge-info"]')
        tag = driver.find_elements(By.XPATH, '//h4/strong')

        info_0 = [item.text for item in tag]
        type = info_0

        info = [item.text for item in local]
        location = info

        info_1 = [item.text for item in problem]
        issue = info_1

    except NoSuchElementException:
        type = None
        location = None
        issue = None

    statement = {
        'Title': driver.find_element(By.XPATH, '//h3[@class="title"]').text,
        'URL': link,
        'Type': type,
        'Author': [
            {'name': item.get_attribute('textContent'), 'url': item.get_attribute('href')}
            for item in driver.find_elements(By.XPATH, '//div[@id="additionalCandidatesPublicStatementCollapse"]//a')
        ],
        'Date': driver.find_element(By.XPATH, '//div[@class="col"]/span').text,
        'Location': location,
        'Issues': issue,
        'Text': "\n".join(
            [item.text for item in driver.find_elements(By.XPATH, '//*[@id="publicStatementDetailSpeechContent"]/p')]),
        'Source': driver.find_element(By.XPATH, '//*[@id="publicStatementDetailSpeechContent"]/strong/a').get_attribute(
            'href')
    }

    print(count)
    save_json(, statement)
driver.close()
