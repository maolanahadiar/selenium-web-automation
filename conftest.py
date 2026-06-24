from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure
import os
import subprocess
import webbrowser

#setup browser fixture for tests
@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

#setup allure screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("browser")

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="FAILED_SCREENSHOT",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"\n❌ Screenshot failed: {e}")

#setup toggle allure report to make it auto open after running test
#change mode "serve" for auto or "generate" for manual
MODE = "generate"

def pytest_sessionfinish(session, exitstatus):

    results_dir = "reports/allure-results"
    report_dir = "reports/allure-report"

    if not os.path.exists(results_dir):
        return

    if MODE == "serve":
        subprocess.run(["allure", "serve", results_dir])

    else:
        subprocess.run(
            ["allure", "generate", results_dir, "-o", report_dir, "--clean"]
        )

        webbrowser.open(f"file://{os.path.abspath(report_dir)}/index.html")