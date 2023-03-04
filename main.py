from slack_notifier import SlackNotifier

WEB_HOOK_URL = "YOUR_SLACK_WEBHOOK";
BUILD_NUMBER = "123"
RESULTS_JSON_PATH = "./results/results.json"
notifier = SlackNotifier(WEB_HOOK_URL)
notifier.send_build_results(BUILD_NUMBER, RESULTS_JSON_PATH)
