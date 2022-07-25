"""Test example.

https://playwright.dev/python/docs/test-runners#usage
"""
from get_pwbrowser_sync import get_pwbrowser_sync


# def test_example(page1):
def test_example():
    """Test example."""
    browser = get_pwbrowser_sync()
    page1 = browser.new_page()
    page1.goto("https://httpbin.org/")
    content = page1.text_content("h2")
    if isinstance(content, str):
        assert "httpbin" in content

    # assert "httpbin" in page.innerText('h2')
    # page1.click("text=More information")
