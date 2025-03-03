from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import time

def scrape_data(service_area):
    encoded_area = urllib.parse.quote(service_area)
    url = f"https://www2.hse.ie/services/pharmacies-flu-and-covid-vaccines/?service_area={encoded_area}"

    options = Options()
    options.headless = True  # Temporarily set to False to see the browser
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    print(driver.title)
    time.sleep(5)  # Adjust time as necessary

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    data_divs = soup.select('div[data-v-63959105]')  # Update this selector based on the webpage
    print(f"Found {len(data_divs)} data divs")  # Debugging print statement

    results = []
    for div in data_divs:
        try:
            name = div.find('h3').get_text(strip=True) if div.find('h3') else ''
            address = div.find('p', class_='hse-u-margin-bottom-2').get_text(strip=True) if div.find('p', class_='hse-u-margin-bottom-2') else ''
            phone = div.select_one("li:contains('Phone:') a").get_text(strip=True) if div.select_one("li:contains('Phone:') a") else ''
            website = div.select_one("li:contains('Website:') a").get('href', '').strip() if div.select_one("li:contains('Website:') a") else ''
            email = div.select_one("li:contains('Email:') a").get_text(strip=True) if div.select_one("li:contains('Email:') a") else ''

            result = [name, address, phone, website, email]
            results.append(result)
        except Exception as e:
            print(f"Error processing a data div: {e}")

    return results



service_areas = ["Carlow", "Cavan"]#add the rest area
all_data = []
for area in service_areas:
    print(f"Scraping data for {area}...")
    area_data = scrape_data(area)
    all_data.extend(area_data)


df = pd.DataFrame(all_data, columns=['Name', 'Address', 'Phone', 'Website', 'Email'])
df = df.drop_duplicates(subset=['Name'])
df.to_csv('vaccine_data2.csv', index=False)

print("Data scraping completed!")
