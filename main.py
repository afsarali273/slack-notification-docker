# main.py

import os
from slack_notifier import SlackNotifier

SLACK_WEB_HOOK_URL = os.environ["SLACK_WEB_HOOK_URL"]
BUILD_NUMBER = os.environ["BUILD_NUMBER"]
RESULTS_JSON_PATH = os.environ["RESULTS_JSON_PATH"]

notifier = SlackNotifier(SLACK_WEB_HOOK_URL)
notifier.send_build_results(BUILD_NUMBER, RESULTS_JSON_PATH)
