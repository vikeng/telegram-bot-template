from log import log_info
from flask import Flask, request, abort
import telebot, time
from init_env import PROD, PORT, WEBHOOK_URL, WEBHOOK_SECRET
from handlers import bot

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!!"

# Process webhook calls
@app.route(f"/{WEBHOOK_SECRET}", methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)

webhook_info = bot.get_webhook_info()
if PROD:
    from waitress import serve

    log_info('Start webhook')
    if WEBHOOK_URL != webhook_info.url:
        bot.remove_webhook()
        time.sleep(0.1)
        bot.set_webhook(url=WEBHOOK_URL)
    serve(app, host="0.0.0.0", port=PORT)
else:
    log_info('Start polling')
    if webhook_info.url != '':
        bot.remove_webhook()
    bot.infinity_polling()
