import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page_context():
    # Setup Playwright with headless mode
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)  # Headless mode
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_inflation_calculator(page_context):
    page = page_context

    # Step 0: Create a directory for screenshots if it doesn't exist
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Step 1: Visit the website
    url = "https://www.csas.cz/cs/osobni-finance/investovani#kalkulacka-inflace"
    page.goto(url, timeout=60000, wait_until="domcontentloaded")
    page.screenshot(path=f"{screenshots_dir}/step1_visit_website.png")

    # Step 2: Accept cookies
    cookie_button_selector = "#popin_tc_privacy_button"
    page.wait_for_selector(cookie_button_selector, timeout=10000)
    page.click(cookie_button_selector)
    page.screenshot(path=f"{screenshots_dir}/step2_accept_cookies.png")

    # Step 3: Change value from (4) to (0)
    duration_selector = "#duration"
    page.wait_for_selector(duration_selector, timeout=10000)
    page.fill(duration_selector, "0")
    page.screenshot(path=f"{screenshots_dir}/step3_change_value_to_0.png")
    updated_value = page.input_value(duration_selector)
    assert updated_value == "0", "Duration value was not updated to 0"

    # Step 4: Click on the "minus" button
    minus_button_selector = "#button-minus"
    page.wait_for_selector(minus_button_selector)
    page.click(minus_button_selector)
    page.screenshot(path=f"{screenshots_dir}/step4_click_minus_button.png")
    updated_value_after_minus = page.input_value(duration_selector)
    assert updated_value_after_minus == "4", "Duration value did not reset to 4"

    # Step 5: Change value from 4 to 1000 using "+"
    plus_button_selector = "#button-plus"
    page.wait_for_selector(plus_button_selector)
    page.click(plus_button_selector)
    page.fill(duration_selector, "1000")
    page.screenshot(path=f"{screenshots_dir}/step5_change_value_to_1000.png")
    updated_value_after_plus = page.input_value(duration_selector)
    assert updated_value_after_plus == "1000", "Duration value was not updated to 1000"

    # Step 6: Click "+" again to verify value equals 101
    page.click(plus_button_selector)
    page.screenshot(path=f"{screenshots_dir}/step6_click_plus_to_101.png")
    updated_value_after_next_plus = page.input_value(duration_selector)
    assert updated_value_after_next_plus == "101", "Value was not updated to 101"

    # Step 7: Select "Odvážná" in the custom dropdown
    dropdown_input_selector = "#investorTypeId"
    dropdown_option_selector = "#items-list > ul > li:nth-child(4)"
    expected_value_selector = "div:text('2,93 %')"
    page.wait_for_selector(dropdown_input_selector, timeout=10000)
    page.click(dropdown_input_selector)
    page.screenshot(path=f"{screenshots_dir}/step7_open_dropdown.png")
    page.wait_for_selector(dropdown_option_selector, timeout=10000)
    page.click(dropdown_option_selector)
    page.screenshot(path=f"{screenshots_dir}/step7_select_odvazna.png")

    # Step 8: Verify the displayed value changes to "2,93 %"
    page.wait_for_selector(expected_value_selector, timeout=10000)
    page.screenshot(path=f"{screenshots_dir}/step8_verify_2.93_percent.png")
    assert page.is_visible(expected_value_selector), "Value '2,93 %' was not displayed"
