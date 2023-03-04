# slack-notification-docker
Send Slack notification for various test framework like selenium, playwright cypress, webdriverio etc from Jenkins or any CI tools

<h4> To use this run below snippet</h4>

```shell

docker pull afsarali273/slack-notification-test:latest

docker run -v /Users/mohammedafsar/Repository/slack-notificatin/results:/app/results/ \
 -e BUILD_NUMBER="20" -e RESULTS_JSON_PATH="./results/results.json" \
 -e SLACK_WEB_HOOK_URL=https://hooks.slack.com/services/<REPLACE_THIS>/<REPLACE_THIS>/<REPLACE_THIS> \
 --name slack-notification \
 afsarali273/slack-notification-test:latest
```
```text
docker run 
-v <FULL_PATH_OF_RESULT_FILE>:/app/results/ 
-e BUILD_NUMBER=<YOUR_JENKINS_BUILD_NUMBER>
-e RESULTS_JSON_PATH="./results/results.json" 
-e SLACK_WEB_HOOK_URL= <YOUR_SLACK_WEBHOOK_URL>
--name slack-notification 
afsarali273/slack-notification-test:latest
```

You can run above docker command after your Playwright Test run completed . Make sure you have enabled `json` report 

<h2> Supports : </h2>

<li> Playwright </li> 
<li> Cucumber (In Progress)</li>

