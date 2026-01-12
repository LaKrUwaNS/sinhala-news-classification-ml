from playwright.sync_api import sync_playwright
import pandas as pd
import time

BASE_URL = "https://hirunews.lk/news_listing.php?category=General"
OUTPUT_FILE = "hiru_news_raw.csv"

def scrape_hiru_news():
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL, timeout=60000)

        last_count = 0

        # Scroll until all news is loaded
        while True:
            page.mouse.wheel(0, 6000)
            time.sleep(2)

            cards = page.query_selector_all("#news-cards a.card-v4.listed")
            current_count = len(cards)

            print(f"Loaded articles: {current_count}")

            no_more = page.query_selector("#no-more-news")
            if no_more and no_more.is_visible():
                print("No more news to load.")
                break

            if current_count == last_count:
                break

            last_count = current_count

        # Extract data
        for card in cards:
            title = card.query_selector("h4.title").inner_text()
            description = card.query_selector(".text-content-wrp .description").inner_text()
            date = card.query_selector(".content-top > .description").inner_text()
            image_url = card.query_selector("img").get_attribute("src")
            relative_link = card.get_attribute("href")

            data.append({
                "title": title.strip(),
                "description": description.strip(),
                "date": date.strip(),
                "image_url": image_url,
                "news_url": f"https://hirunews.lk/{relative_link}"
            })

        browser.close()

    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"\nScraping completed successfully.")
    print(f"Data saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    scrape_hiru_news()
