#  import slack
#  client = slack.WebClient(token=slack_token)
# slack_token = 'xoxb-1184311835603-1212991939168-IwgRAdK4lZ026LAcb9ELJYgz'
#  client.chat_postMessage(channel="#general", text="Hello world!")
import json
from flask import Flask, request, make_response
from slacker import Slacker
slack_token = 'xoxb-1184311835603-1212991939168-IwgRAdK4lZ026LAcb9ELJYgz'
slack = Slacker(slack_token)


app= Flask(__name__)

def get_answer():
    return "안녕하세요"

def event_handler(event_type, slack_event):
    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        print(channel)
        text = get_answer()
        slack.chat.post_message(channel, text)
        return make_response("앱 멘션 메시지가 보내졌습니다",200,)
    message = "[%s] 이벤트 핸들러를 찾을 수 없습니다."% event_type
    return make_response(message, 200, {"X-Slack-No-Retry":1})

@app.route("/slack", methods=["GET","POST"])
def hears():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"],200,
                                {"content_type":"application/json"})
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("슬랙 요청에 이벤트가 없습니다",404,
            {"X-Slack-No-Retry":1})


@app.route("/", methods = ["GET","POST"])
def index():
    return "Hello world"

if __name__ =='__main__':
    app.run('0.0.0.0',port=5000)
