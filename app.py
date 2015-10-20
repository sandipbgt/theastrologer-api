from flask import Flask, jsonify, url_for
from theastrologer import Horoscope, is_valid_sunsign

app = Flask(__name__)

# Main Index
@app.route('/', methods=['GET'])
def get_home():
    return jsonify({
            'author': 'Sandip Bhagat',
            'author_url': 'http://sandipbgt.github.io',
            'base_url': 'https://theastrologer-api.herokuapp.com',
            'project_name': 'theastrologer-api',
            'project_url': 'https://github.com/sandipbgt/theastrologer-api',
            'api': 'https://theastrologer-api.herokuapp.com/api'
        })

# API Index
@app.route('/api', methods=['GET'])
def get_api_home():
    return jsonify({
            'yesterday': 'https://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/yesterday',
            'today': 'https://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/today',
            'tomorrow': 'https://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/tomorrow'
        })

# Yesterday's Horoscope
@app.route('/api/horoscope/<sunsign>/yesterday', methods=['GET'])
def get_yesterday_horoscope(sunsign):
    if not is_valid_sunsign(sunsign):
        return jsonify({'status': 400, 'error': 'bad request',
                        'message': 'Invalid sunsign'}), 400
    horoscope = Horoscope(sunsign)
    return jsonify(horoscope.yesterday())

# Todays's Horoscope
@app.route('/api/horoscope/<sunsign>/today', methods=['GET'])
def get_today_horoscope(sunsign):
    if not is_valid_sunsign(sunsign):
        return jsonify({'status': 400, 'error': 'bad request',
                        'message': 'Invalid sunsign'}), 400
    horoscope = Horoscope(sunsign)
    return jsonify(horoscope.today())

# Tomorrow's Horoscope
@app.route('/api/horoscope/<sunsign>/tomorrow', methods=['GET'])
def get_tomorrow_horoscope(sunsign):
    if not is_valid_sunsign(sunsign):
        return jsonify({'status': 400, 'error': 'bad request',
                        'message': 'Invalid sunsign'}), 400
    horoscope = Horoscope(sunsign)
    return jsonify(horoscope.tomorrow())

# Send sms message of todays's horoscope via Twilio API
@app.route('/api/horoscope/<sunsign>/today', methods=['POST'])
def send_todays_horoscope(sunsign):
    if not is_valid_sunsign(sunsign):
        return jsonify({'status': 400, 'error': 'bad request',
                        'message': 'Invalid sunsign'}), 400
    horoscope = Horoscope(sunsign)
    today = horoscope.today()
    message = "%s [%s]: %s INTENSITY: %s , MOOD: %s , KEYWORDS: %s" % (sunsign.upper(), today['date'], today['horoscope'], today['meta']['intensity'], today['meta']['mood'], today['meta']['keywords'])
    if not send_message(message):
        return jsonify({'status': 400, 'error': 'bad request',
                        'message': 'Twilio API environment variables not configured'}), 400

    return jsonify({'message': 'success', 'code': 201}), 201

# Utility function to send message via Twilio API
def send_message(message):
    import os
    from twilio import TwilioRestException
    from twilio.rest import TwilioRestClient

    account_sid = os.environ.get('TWILIO_ACCOUNT_SID', None)
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN', None)
    to_phone = os.environ.get('TWILIO_TO_PHONE', None)
    from_phone = os.environ.get('TWILIO_FROM_PHONE', None)
    body = message

    if not account_sid or not auth_token or not to_phone or not from_phone:
        return False

    try:
        client = TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(body=body, to=to_phone, from_=from_phone)
        return {
            'message_id': message.sid
        }
    except TwilioRestException as e:
        return {
                'error_message': str(e.msg)
            }, 400

# Fire our Flask app
if __name__ == '__main__':
    app.run()