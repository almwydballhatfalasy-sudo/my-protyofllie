from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Test index.html
        page.goto("http://localhost:8000/index.html")

        # Capture English version
        page.screenshot(path="verification/screenshots/index_en.png")
        print("Captured index_en.png")

        # Click language toggle (it should be AR initially or toggle to AR)
        # The button text is "AR" when in English mode
        page.click("#lang-toggle")

        # Verify dir is rtl
        dir_attr = page.get_attribute("html", "dir")
        print(f"Index HTML dir: {dir_attr}")

        # Capture Arabic version
        page.screenshot(path="verification/screenshots/index_ar.png")
        print("Captured index_ar.png")

        # Test code.html
        page.goto("http://localhost:8000/code.html")

        # It should remember the language (Arabic) from localStorage?
        # Playwright sessions might not persist unless using a context.
        # Let's check.
        dir_attr_code = page.get_attribute("html", "dir")
        print(f"Code HTML dir initially: {dir_attr_code}")

        if dir_attr_code != "rtl":
            page.click("#lang-toggle")

        page.screenshot(path="verification/screenshots/code_ar.png")
        print("Captured code_ar.png")

        # Toggle back to EN
        page.click("#lang-toggle")
        page.screenshot(path="verification/screenshots/code_en.png")
        print("Captured code_en.png")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification/screenshots"):
        os.makedirs("verification/screenshots")
    run()
