import os
from slack_bolt import App as SlackApp


from dotenv import load_dotenv
load_dotenv()

slackapp = SlackApp(token=os.environ.get("SLACK_BOT_TOKEN"))


def report_top_thumbsup_messages(channel_id):
    bot_token = os.environ["SLACK_BOT_TOKEN"]
    thumbs_up_reaction = "notebook_with_decorative_cover"

    client = slackapp.client

    # app_token = os.environ["SLACK_APP_TOKEN"]
    # channel_name = "hanhwa"
    # response = client.conversations_list(token=bot_token)
    # channels = response["channels"]

    # for channel in channels:
    #     if channel["name"] == channel_name:
    #         channel_id = channel["id"]
    #         break
    
    
    response = client.conversations_history(token=bot_token, channel=channel_id)
    messages = response["messages"]

    thumbs_up_messages = []

    for message in messages:
        if "reactions" in message:
            for reaction in message["reactions"]:
                if reaction["name"] == thumbs_up_reaction:
                    print(message)
                    thumbs_up_messages.append(message)

    report_formatted = "Thumbs Up Messages:\n"
    for message in thumbs_up_messages:
        ts = message["ts"]
        msg_url = f"https://upstageai.slack.com/archives/{channel_id}/p{ts.replace('.', '')}"
        report_formatted += f"User <@{message['user']}>: {message['text']}, <{msg_url}|메시지 링크>]\n"
    return report_formatted

from flask import Flask, jsonify, make_response
app = Flask(__name__)

@app.route('/note', methods=['POST'])
def handle_command():
    return jsonify(
        response_type="in_channel",
        text=report_top_thumbsup_messages("C044NMVKK5L")
    )

if __name__ == '__main__':
    app.run(port=3000)

