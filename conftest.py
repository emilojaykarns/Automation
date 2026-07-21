import pytest
import requests
import os
from utils.driver_factory import build_driver

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPOSITORY")  # "emilojaykarns/Automation"
ASSIGNEE_EMAIL = os.getenv("JIRA_ASSIGNEE_EMAIL", "emilojaykarns@emilo.in")


def create_github_issue(title, body):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "title": title,
        "body": body
    }
    response = requests.post(url, json=payload, headers=headers)
    print(f"GitHub Issue created: {response.json().get('html_url')}")


@pytest.fixture
def driver():
    drv = build_driver()
    yield drv
    drv.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Sirf FAIL pe aur sirf call phase mein
    if report.when == "call" and report.failed:
        test_name = item.name
        error_msg = str(report.longrepr)

        issue_title = f"🐛 Test Failed: {test_name}"
        issue_body = f"""## Automated Bug Report

**Test Name:** `{test_name}`

## Error Details