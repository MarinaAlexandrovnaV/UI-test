from playwright.sync_api import Page
import config
import qase


class IndexPage:
    _LINK_ENG_LANG = "xpath=//*[@id='SIvCob']/a"
    _BUTTON_GOOGLE_SEARCH = "xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"

    @qase.step(
        action='Open the Index page',
        data=config.url.DOMAIN,
        expected_result='The page opened'
    )

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    @qase.step(
        action='Pressthe English Language link',
        expected_result='The page language changed to English'
    )

    def press_link_eng_lang(self, page: Page):
        page.locator(self._LINK_ENG_LANG).click()

    @qase.step(
        action='Check the text in the Google Search button',
        expected_result='The test is equal Google Search'
    )

    def get_text_from_google_search_button(self, page: Page):
        return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')
