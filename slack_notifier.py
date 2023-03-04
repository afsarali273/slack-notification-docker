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


def get_json_payload():
    with open('./slack_payload.json') as f:
        payload = json.load(f)

    return payload


class SlackNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, message):

        response = requests.post(self.webhook_url, json=get_json_payload())
        if response.status_code != 200:
            print(f"Error sending message: {response.text}")
        else:
            print(f"Message sent")

    def send_build_results(self, build_number, test_results_path):
        passed, failed, skipped = get_test_result(test_results_path)
        message = f"Build {build_number} completed with {passed} test results"
        self.send_message(message)
