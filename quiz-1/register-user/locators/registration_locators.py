class RegistrationLocators:
    LOGIN_SIGNUP_BTN = "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a"
    SIGNUP_FORM = ".signup-form"
    NAME_INPUT = '//*[@id="form"]/div/div/div[3]/div/form/input[2]'
    EMAIL_INPUT = '//*[@id="form"]/div/div/div[3]/div/form/input[3]'
    SIGNUP_BTN = "[data-qa='signup-button']"

    ENTER_ACCOUNT_INFO_SELECTOR = '.login-form'

    DETAILS_SELECTORS = {
        "GENDER": '[for="id_gender1"]',
        "PASSWORD": '[data-qa="password"]',
        "DAYS": '[data-qa="days"]',
        "MONTH": '[data-qa="months"]',
        "YEAR": '[data-qa="years"]',

        "NEWSLETTER": '[for="newsletter"]',
        "OFFERS": '[for="optin"]',

        "FIRST_NAME": '[data-qa="first_name"]',
        "LAST_NAME": '[data-qa="last_name"]',
        "COMPANY": '[data-qa="company"]',
        'ADDRESS': '[data-qa="address"]',
        'COUNTRY': '[data-qa="country"]',

        'STATE': '[data-qa="state"]',
        'CITY': '[data-qa="city"]',
        'ZIP': '[data-qa="zipcode"]',
        'PHONE': '[data-qa="mobile_number"]',

        'SUBMIT_BTN': '[data-qa="create-account"]'
    }

    CREATED = '[data-qa="account-created"]'
    CONTINUE = '[data-qa="continue-button"]'
    LOGGED_IN_AS = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a'
    DELETE_ACCOUNT = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a'
