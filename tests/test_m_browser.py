"""Test with loop fixture.

https://playwright.dev/python/docs/test-runners#usage
# async def test_example2(page2):
    ’‘’Async example.

    playwright = await async_playwright().start()
    if 1:
    await playwright.stop()
    ‘’‘
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
"""
from get_pwbrowser_sync import get_pwbrowser_sync


# def test_hardway(m_browser):
def test_hardway():
    """Test https://httpbin.org."""
    # loop, browser = loop_browser
    m_browser = get_pwbrowser_sync()
    page = m_browser.new_page()

    page.goto("https://httpbin.org/", timeout=60 * 1000)
    content = page.text_content("h2")
    if isinstance(content, str):
        assert "httpbin" in content
