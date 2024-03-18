from bs4 import BeautifulSoup
import requests
import re

def NBC(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title, spotlight, and content text
    title_tag = soup.find("h1", class_="article-hero-headline__htag lh-none-print black-print article-hero-headline__htag--loading")
    spotlight_tag = soup.find("div", class_="styles_articleDek__Icz5H styles_loading__FrACj styles_withImage__SSIip")
    content_tags = soup.find("div", class_="article-body__content article-body-font--loading").find_all("p") if soup.find("div", class_="article-body__content article-body-font--loading") else None

    title = title_tag.get_text() if title_tag else "Title not found"
    spotlight = spotlight_tag.get_text() if spotlight_tag else "Spotlight not found"
    content_text = "\n".join([p.get_text() for p in content_tags]) if content_tags else "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        file.write(f"Spotlight: {spotlight}\n\n")
        file.write(f"Content Text:\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")

# Test the function1
#NBC("https://www.nbcnews.com/politics/immigration/thousands-foreign-students-u-s-student-visas-may-have-worked-n1109286?cid=public-rss_20200102", "scraped_data.txt")

def MSNBC(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    #pretty_html = soup.prettify()
    #with open('output.html', 'w') as file:
    # Write the pretty HTML to the file
    #    file.write(pretty_html)
    
    # Find the title
    title_tag = soup.find("div", class_="article-hero-headline layout-grid-item grid-col-10-l").find("h1", class_="article-hero-headline__htag lh-none-print black-print article-hero-headline__htag--loading")
    title = title_tag.get_text() if title_tag else "Title not found"

    # Find the spotlight
    spotlight_tag = soup.find("div", attrs={"data-testid": "article-dek"})
    spotlight = spotlight_tag.get_text() if spotlight_tag else "Spotlight not found"

    # Find the content text
    content_tags = soup.find("div", class_="article-body__content").find_all("p") if soup.find("div", class_="article-body__content") else None
    content_text = "\n".join([p.get_text() for p in content_tags]) if content_tags else "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        file.write(f"Spotlight: {spotlight}\n\n")
        file.write(f"Content Text:\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")
    
#MSNBC("https://www.msnbc.com/rachel-maddow-show/has-trump-really-reversed-course-legal-immigration-msna1192436", "scraped_data.txt")

def alternet(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title
    title_tag = soup.find("h1", class_="headline h1")
    title = title_tag.get_text() if title_tag else "Title not found"

    # Find the content text
    content_tags = soup.find("div", class_="body-description").find_all("p") if soup.find("div", class_="body-description") else None
    if not content_tags:
        content_tags = soup.find("div", class_="text").find_all("p") if soup.find("div", class_="text") else None
    content_text = "\n".join([p.get_text() for p in content_tags]) if content_tags else "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        #file.write(f"Title: {title}\n\n")
        file.write(f"\n{title}")
        #file.write(f"Content Text:\n{content_text}")
        file.write(f"\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")

# Test the function with a specific URL from alternet.org
#alternet("https://www.alternet.org/2020/05/eric-trump-slammed-for-calling-covid-19-crisis-a-democratic-hoax-that-will-magically-disappear/", "scraped_data.txt")


def breitbart(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title
    title_tag = soup.find("section", id="MainW").find("header").find("h1")
    title = title_tag.get_text() if title_tag else "Title not found"

    # Find the spotlight and content text
    entry_content_tag = soup.find("div", class_="entry-content")
    if entry_content_tag:
        spotlight_tag = entry_content_tag.find("p", class_="subheading")
        spotlight = spotlight_tag.get_text() if spotlight_tag else "Spotlight not found"
        content_tags = entry_content_tag.find_all("p")
        content_text = "\n".join([p.get_text() for p in content_tags if p.get('class') != ['subheading']]) if content_tags else "Content text not found"
    else:
        spotlight = "Spotlight not found"
        content_text = "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        file.write(f"Spotlight: {spotlight}\n\n")
        file.write(f"Content Text:\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")

# Test the function with a specific URL from breitbart.com
#breitbart("https://www.breitbart.com/national-security/2019/05/14/china-three-year-old-girl-dies-after-rabies-shot-raising-fears-another-vaccine-scandal/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+breitbart+%28Breitbart+News%29", "scraped_data.txt")



def thefederalist(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title
    title_tag = soup.select_one("header[class*='article-header']").find("h1")
    title = title_tag.get_text() if title_tag else "Title not found"

    # Find the spotlight
    spotlight_div = soup.select_one("div[class*='article-excerpt']")
    spotlight = spotlight_div.find("p").get_text() if spotlight_div and spotlight_div.find("p") else None

    # Find the content text
    content_tags = soup.select_one("div[class*='article-content'], div[class*='article-body']")
    content_text = "\n".join([p.get_text() for p in content_tags.find_all("p")]) if content_tags else "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        if spotlight:
            file.write(f"Spotlight: {spotlight}\n\n")
        file.write(f"Content Text:\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")


# Test the function with a specific URL from breitbart.com
#thefederalist("https://thefederalist.com/2019/06/25/aoc-wants-taxpayers-pay-off-1-6-billion-student-loans-imagine-treating-debts-like/", "scraped_data.txt")


def reuters(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print the entire HTML content in a nicely formatted way
    #print(soup.prettify())

    # Find the title
    title_section = soup.find("div", class_="default-article-header__heading__3cyKI")
    print(f"title_section: {title_section}")  # Print the result of finding the title section
    title_tag = title_section.find("h1", attrs={"data-testid": "Heading"}) if title_section else None
    title = title_tag.get_text() if title_tag else "Title not found"

    # Find the content text
    content_section = soup.find("div", class_="article-body__content__17Yit")
    print(f"content_section: {content_section}")  # Print the result of finding the content section
    content_tags = content_section.find_all("div", attrs={"data-testid": re.compile(r"paragraph-\d+")}) if content_section else None
    content_text = "\n".join([p.get_text() for p in content_tags]) if content_tags else "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        file.write(f"Content Text:\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")
    
# Test the function with a specific URL from reuters.com
#reuters("https://www.reuters.com/article/us-global-race-usa-los-angeles/l-a-sheriffs-deputies-fatally-shoot-black-man-after-suspected-bike-violation-idUSKBN25S606/", "scraped_data.txt")

def usatoday(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title
    title_div = soup.find("div", class_="story-topper lede column eleven-column")
    title = title_div.find("h1").get_text() if title_div else "Title not found"

    # Find the content text
    content_article = soup.find("article", class_="story primary-content text news row")
    if content_article:
        content_paragraphs = content_article.find_all("p")
        content_text = "\n".join([p.get_text() for p in content_paragraphs]) if content_paragraphs else "Content text not found"
    else:
        content_text = "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w",encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        file.write(f"Content Text:\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")

# Test the function with a specific URL from usatoday.com
#usatoday("https://eu.usatoday.com/story/news/nation/2020/02/14/gender-equality-millennial-men-still-dont-do-laundry-house-cleaning/4748860002/", "scraped_data.txt")

def huffpost(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title
    title_div = soup.find("div", class_="top-header js-cet-subunit")
    title = title_div.find("h1").get_text() if title_div else "Title not found"

    # Find the spotlight
    spotlight_div = soup.find("div", class_="dek")
    spotlight = spotlight_div.get_text() if spotlight_div else "Spotlight not found"

    # Find the content text
    content_article = soup.find("article", class_="entry__content js-page-content-top")
    if content_article:
        content_section = content_article.find("section", class_="entry__content-list js-entry-content js-cet-subunit")
        if content_section:
            content_divs = content_section.find_all("div", recursive=False)
            content_text = "\n".join([div.get_text() for div in content_divs]) if content_divs else "Content text not found"
        else:
            content_text = "Content text not found"
    else:
        content_text = "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        file.write(f"Spotlight: {spotlight}\n\n")
        file.write(f"Content Text:\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")

# Test the function with a specific URL from huffpost.com
#huffpost("https://www.huffpost.com/entry/ufc-conor-mcgregor-sexual-assault-investigation_n_5c9a7124e4b072a7f6008ff5", "scraped_data.txt")


def foxnews(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the title
    title_div = soup.find("div", class_="article-meta article-meta-upper")
    title = title_div.find("h1", class_="headline speakable").get_text() if title_div else "Title not found"

    # Find the spotlight
    spotlight_div = soup.find("div", class_="article-meta article-meta-upper")
    spotlight = spotlight_div.find("h2", class_="sub-headline speakable").get_text() if spotlight_div and spotlight_div.find("h2", class_="sub-headline speakable") else None

    # Find the content text
    content_article = soup.find("div", class_="article-body")
    if content_article:
        content_paragraphs = content_article.find_all("p")
        content_text = "\n".join([p.get_text() for p in content_paragraphs if not p.find('a')]) if content_paragraphs else "Content text not found"
    else:
        content_text = "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        if spotlight:
            file.write(f"Spotlight: {spotlight}\n\n")
        file.write(f"Content Text:\n{content_text}")

# Test the function with a specific URL from foxnews.com
#foxnews("https://www.foxnews.com/entertainment/australian-actress-yael-stone-giving-up-green-card-fight-climate-change", "scraped_data.txt")

def foxbusiness(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    #pretty_html = soup.prettify()
    #with open('output.html', 'w') as file:
        #Write the pretty HTML to the file
        #file.write(pretty_html)
        
    # Find the title
    title_tag = soup.find("div", class_="page-content").find("h1", class_="headline")
    title = title_tag.get_text() if title_tag else "Title not found"

    # Find the content text
    content_tags = soup.find("div", class_="article-body").find_all("p") if soup.find("div", class_="article-body") else None
    content_text = "\n".join([p.get_text() for p in content_tags]) if content_tags else "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        file.write(f"Content Text:\n{content_text}")

    # Print a success message
    print(f"The data was successfully scraped from {url} and saved to {file_name}")
    
# Test the function with a specific URL from foxnews.com
#foxbusiness("https://www.foxbusiness.com/money/middle-class-americans-worry-wealth-tax", "scraped_data.txt")

def thedailybeast(url, file_name):
    # Define headers for the GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title
    title_div = soup.find("div", class_="StandardHeader StandardHeader--single-author")
    title = title_div.find("h1", class_="StandardHeader__title").get_text() if title_div else "Title not found"

    # Find the spotlight
    spotlight_div = soup.find("div", class_="StandardHeader StandardHeader--single-author")
    spotlight = spotlight_div.find("p", class_="StoryDescription").get_text() if spotlight_div else None

    # Find the content text
    content_article = soup.find("div", class_="Body__content _2o_vt")
    if content_article:
        content_paragraphs = content_article.find("div", class_="Mobiledoc").find_all("p")
        content_text = "\n".join([p.get_text() for p in content_paragraphs]) if content_paragraphs else "Content text not found"
    else:
        content_text = "Content text not found"

    # Save the scraped data to a text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        if spotlight:
            file.write(f"Spotlight: {spotlight}\n\n")
        file.write(f"Content Text:\n{content_text}")

#thedailybeast('https://www.thedailybeast.com/its-not-just-trump-the-gop-is-getting-crueler-and-crazier?source=twitter&via=desktop', 'scraped_data.txt')  # replace with the URL of the article you want to scrape
