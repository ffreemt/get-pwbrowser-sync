"""Test sync pwbrowser."""
from get_pwbrowser_sync import get_pwbrowser_sync


# def test_sync_browser(pwbrowser):
def test_pwbrowser():
    """Test sync pwbrowser."""
    pwbrowser = get_pwbrowser_sync()
    page = pwbrowser.new_page()
    page.goto("http://www.baidu.com")
    assert "百度" in page.title()
    # print(page.title())
    # '百度一下，你就知道'
