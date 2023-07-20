import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from slack_bolt import App as SlackApp

load_dotenv()

app = Flask(__name__)
slackapp = SlackApp(token=os.environ.get("SLACK_BOT_TOKEN"))

WORKSPACE = os.environ["SLACK_WORKSPACE"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]


def filter_messages_with_emoji(messages, emoji):
    filtered_messages = []
    for msg in messages:
        reactions = [r["name"] for r in msg.get("reactions", [])]
        if emoji in reactions:
            filtered_messages.append(msg)
    return filtered_messages


def report_emoji_messages(channel_id: str, emoji: str = "notebook_with_decorative_cover"):
    response = slackapp.client.conversations_history(token=SLACK_BOT_TOKEN, channel=channel_id)
    messages = response["messages"]
    messages = filter_messages_with_emoji(messages, emoji)

    report_formatted = ""
    for message in messages:
        ts = message["ts"]
        msg_url = f"https://{WORKSPACE}.slack.com/archives/{channel_id}/p{ts.replace('.', '')}"
        report_formatted += f"<@{message['user']}>가 :{emoji}:하시길\n{message['text'][:300]} <{msg_url}|링크>\n\n"
    if report_formatted == "":
        report_formatted = f":{emoji}:가 포함된 메시지가 없습니다."
    return report_formatted


@app.route("/note", methods=["POST"])
def handle_command():
    req = request.form
    if (emoji := req.get("text")) is None:
        text = "Please specify an emoji"
    else:
        emoji = emoji.strip(":")
        text = report_emoji_messages(req["channel_id"], emoji=emoji)

    return jsonify(response_type="in_channel", text=text)


if __name__ == "__main__":
    app.run(port=3000)
