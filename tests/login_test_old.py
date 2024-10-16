from playwright.sync_api import Page, expect


def test_login_error(page: Page):
    base_url1 = "https://www.gmx.net/"
    expected_error_msg = "Login leider nicht erfolgreich."
    page.goto(base_url1)
    page.wait_for_timeout(timeout=6_000)
    frames_counter = page.frames
    for frame in frames_counter:
        frame_button = frame.locator("//button[@id='save-all-pur']")
        if frame_button.is_visible():
            frame_button.click()
    '''CONSENT_IFRAME = page.locator("iframe[contains(@src, 'https://plus.gmx.net')]")
    accept_button = CONSENT_IFRAME.locator("//button[@id='save-all-pur']")
    accept_button.click()'''
    email_address = page.locator("//input[@name='username']")
    email_address.fill('')
    password = page.locator("//input[@name='password']")
    password.fill('')
    login_button = page.locator("//button[text()='Login']")
    login_button.click()
    actual_error_msg = page.locator("//div[@data-component='notification']/div/strong")
    print("Actual error message is : ", actual_error_msg)
    expect(actual_error_msg).to_have_text(expected_error_msg)


def test_login_with_invalid_credentials(page: Page):
    base_url1 = "https://www.gmx.net/"
    expected_error_msg = "Login leider nicht erfolgreich."
    page.goto(base_url1)
    page.wait_for_timeout(timeout=6_000)
    frames_counter = page.frames
    for frame in frames_counter:
        frame_button = frame.locator("//button[@id='save-all-pur']")
        if frame_button.is_visible():
            frame_button.click()
    email_address = page.locator("//input[@name='username']")
    email_address.fill('abcdefghijklmnopqwerty')
    password = page.locator("//input[@name='password']")
    password.fill('asdfghjqwertyuasd')
    login_button = page.locator("//button[text()='Login']")
    login_button.click()
    actual_error_msg = page.locator("//div[@data-component='notification']/div/strong")
    print("Actual error message is : ", actual_error_msg)
    expect(actual_error_msg).to_have_text(expected_error_msg)


def test_login_with_valid_credentials(page: Page):
    base_url1 = "https://www.gmx.net/"
    expected_error_msg = "Login leider nicht erfolgreich."
    page.goto(base_url1)
    page.wait_for_timeout(timeout=6_000)
    frames_counter = page.frames
    for frame in frames_counter:
        frame_button = frame.locator("//button[@id='save-all-pur']")
        if frame_button.is_visible():
            frame_button.click()
    email_address = page.locator("//input[@name='username']")
    email_address.fill('')
    password = page.locator("//input[@name='password']")
    password.fill('')
    login_button = page.locator("//button[text()='Login']")
    login_button.click()


def test_back_to_login_on_invalid_login(page: Page):
    base_url1 = "https://www.gmx.net/"
    expected_error_msg = "Login leider nicht erfolgreich."
    page.goto(base_url1)
    page.wait_for_timeout(timeout=6_000)
    frames_counter = page.frames
    for frame in frames_counter:
        frame_button = frame.locator("//button[@id='save-all-pur']")
        if frame_button.is_visible():
            frame_button.click()
    email_address = page.locator("//input[@name='username']")
    email_address.fill('')
    password = page.locator("//input[@name='password']")
    password.fill('')
    login_button = page.locator("//button[text()='Login']")
    login_button.click()
    back_button = page.locator("//a[text()= ' Zurück zum Login ']")
    expect(back_button).to_be_visible()
    back_button.click()
    expect(login_button).to_be_visible()
