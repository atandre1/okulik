from playwright.sync_api import sync_playwright

def run_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Your Playwright script here

        page.goto('https://google.com')
        page.screenshot(path='example.png')

        browser.close()

if __name__ == "__main__":
    run_playwright()
