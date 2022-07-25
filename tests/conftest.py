# import asyncio
import pytest
from playwright.sync_api import sync_playwright

# from playwright.async_api import async_playwright
# from get_pwbrowser import get_pwbrowser_async as get_pwbrowser
from get_pwbrowser_sync import get_pwbrowser_sync


@pytest.fixture
def input_value():
    input = 39
    return input


_ = '''
@pytest.fixture
def page1():
    # with sync_playwright() as p:
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch()
    # context = browser.new_context()
    page_ = browser.new_page()

    # page.goto("http://playwright.dev")
    # print(page.title())

    # return page_
    yield page_

    browser.close()


@pytest.fixture
@pytest.mark.asyncio
async def page2():
    # with sync_playwright() as p:
    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch()
    # context = browser.new_context()
    page_ = await browser.new_page()

    # page.goto("http://playwright.dev")
    # print(page.title())

    # return page_
    yield page_

    await browser.close()


# @pytest.mark.asyncio
@pytest.fixture
async def browser1(scope="module"):  # session
    browser_ = get_pwbrowser_sync()

    yield browser_
    await browser_.close()


@pytest.fixture  # sync
def pwbrowser(scope="session"):
    """Prep a browser."""
    browser_ = get_pwbrowser_sync()

    yield browser_

    browser_.close()


@pytest.fixture  # hard way
def m_browser(scope="module"):
    """Prep a browser."""
    browser = get_pwbrowser_sync()
    yield browser

    print("closing up")
    # loop.run_until_complete(browser.close())
    browser.close()
# '''
