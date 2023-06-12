# political-agenda
This pack is made for scraping data from website https://justfacts.votesmart.org/ and further processing the collected info
# Libraries used
Selenium, Plotly, Geckodriver, SpaCy
# Files description 


| File | What it does |
|-----:|-----------|
| Statement collection| Used for scraping the primary data of the statement. This includes date, title and link. The collected data is saved in json file.|
| Statement details| Used for further scraping of each collected statement. This includes: title, link, type of statement, author, date, location, issues, text and source. The collected data is collected in a new json file. |
| Statement entities and Entities append| Used for finding named entities in the text of the statement and adding them to the corresponding json file.      |
|Countries list|Takes all named entities from the "GPE" and saves them in a new json file|
|Countries uni| Unifies countries, if they have diffetent names|
|Countries chart| Creates a countries chart using plotly|
