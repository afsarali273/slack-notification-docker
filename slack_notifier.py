import json
import requests


def get_test_result(test_results_path):
    with open(test_results_path) as f:
        data = json.load(f)

    # Get the list of test suites
    suites = data['suites']

    # Initialize the counters for passed, failed and skipped tests
    passed = 0
    failed = 0
    skipped = 0

    # Loop through the test suites
    for suite in suites:
        # Get the list of test cases
        specs = suite['specs']
        # Loop through the test cases
        for spec in specs:
            # Get the list of individual tests
            tests = spec['tests']
            # Loop through the individual tests
            for test in tests:
                # Get the status of the test and increment the corresponding counter
                results = test['results']
                for result in results:
                    status = result['status']

                if status == 'passed':
                    passed += 1
                elif status == 'failed':
                    failed += 1
                elif status == 'skipped':
                    skipped += 1

    # Print the results
    print('Passed:', passed)
    print('Failed:', failed)
    print('Skipped:', skipped)

    return passed, failed, skipped


def get_json_payload(build_number, test_results_path):
    with open('./slack_payload.json') as f:
        payload = json.load(f)

    blocks = payload['blocks']
    passed, failed, skipped = get_test_result(test_results_path)
    total_tests = passed+failed+skipped
    pass_percent = "{:.0%}".format((passed/total_tests))

    blocks[1]['elements'][0]['text'] = f"*Results*: {passed}/{total_tests} Passed ({pass_percent})"
    blocks[2]['elements'][0]['text'] = f":white_check_mark: *{passed}*   :x: *{failed}*   :warning:   *{skipped}*"

    # Set Report Url
    blocks[4]['elements'][0]['url'] = f"https://jenkins.propertyguru.com/job/Fintech-SF-Automation/{build_number}/HTML_20Report/"

    return payload


class SlackNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, build_number,test_results_path):

        response = requests.post(self.webhook_url, json=get_json_payload(build_number, test_results_path))
        if response.status_code != 200:
            print(f"Error sending message: {response.text}")
        else:
            print(f"Message sent")

    def send_build_results(self, build_number, test_results_path):
        self.send_message(build_number, test_results_path)
