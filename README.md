# theastrologer-api

API to view and send horoscope as SMS from [theastrologer.com](http://theastrologer.com) using [theastrologer](https://pypi.python.org/pypi/theastrologer/) lilbrary, Flask framework and Twilio API

## Installation
```sh
$ git clone https://github.com/sandipbgt/theastrologer-api.git
$ cd theastrologer-api
$ pip install -r requirements.txt
$ gunicorn app:app
```

## Configuration
* Copy the below commands at the end of your `~/.bashrc` profile and type `source ~/.bashrc` in your terminal

```sh
### theastrologer-api environment variables for Twilio SMS
export TWILIO_ACCOUNT_SID="your twilio account sid"
export TWILIO_AUTH_TOKEN="your twilio auth token"
export TWILIO_TO_PHONE="verified number for which to send sms"
export TWILIO_FROM_PHONE="your twilio phone number"
```

# API Usage

**Base URL:** `http://theastrologer-api.herokuapp.com`

**Description:** Base url of app

**Response:**
```json
{
    "api": "http://theastrologer-api.herokuapp.com/api",
    "author": "Sandip Bhagat",
    "author_url": "http://sandipbgt.github.io",
    "base_url": "https://theastrologer-api.herokuapp.com",
    "project_name": "theastrologer-api",
    "project_url": "https://github.com/sandipbgt/theastrologer-api"
}
```

**API Base URL:** `http://theastrologer-api.herokuapp.com/api`

**Description:** Base url of api

**Response:**
```json
{
    "today": "http://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/today",
    "tomorrow": "http://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/tomorrow",
    "yesterday": "http://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/yesterday"
}
```

**GET:** `http://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/today`

**Description:** Returns today's horoscope

**Example:** `http://theastrologer-api.herokuapp.com/api/horoscope/aquarius/today`

**Response:**
```json
{
    "date": "2015-10-20",
    "sunsign": "Aquarius"
    "horoscope": "You're a thinker by nature, but focus today on staying grounded in your body. Go for a long walk or do some yoga on your living room floor. Eat foods that are densely nutritious. Then focus on your future. It's time to take some solid steps toward a more secure life, whether that means adjusting your budget, looking for a new, better job, enrolling in classes or anything else that will improve your standing.",
    "meta": {
        "intensity": "55%",
        "keywords": "factual, permanence",
        "mood": "cultured"
    },
}
```

**POST:** `http://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/today`

**Description:** Sends today's horoscope as SMS via Twilio API. Note: You must configure environment variables to send SMS.

**Example:** `http://theastrologer-api.herokuapp.com/api/horoscope/aquarius/today`

**Response:**
```json
{
  "code": 201,
  "message": "success"
}
```

**GET:** `http://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/yesterday`

**Description:** Returns yesterday's horoscope

**Example:** `http://theastrologer-api.herokuapp.com/api/horoscope/aquarius/yesterday`

**Response:**
```json
{
    "date": "2015-10-19",
    "sunsign": "Aquarius"
    "horoscope": "You're squirming today against some external attempt to confine your movements or your creativity. Of course, you're ultra-sensitive to any type of restriction, so this certainly doesn't sit well with you. Whether it's something as straightforward as a traffic jam or as complicated as a relationship doesn't matter. It's not the exact situation that matters as much as your reaction to it. Go for the mature, civilized approach today.",
    "meta": {
        "intensity": "55%",
        "keywords": "quiet, simple",
        "mood": "boring"
    },
}
```

**GET:** `http://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/tomorrow`

**Description:** Returns tomorrow's horoscope

**Example:** `http://theastrologer-api.herokuapp.com/api/horoscope/aquarius/tomorrow`

**Response:**
```json
{
    "date": "2015-10-21",
    "sunsign": "Aquarius"
    "horoscope": "Today you're infused with the excitement of discovery. The world is full of possibility. It's a great time to research or develop a project, whether a personal or professional one. The important thing is to be creative: The more innovative your ideas, the better. A pioneering approach will not only lead to big things, it will impress your employer and other VIPs who are looking for something just a little bit different now.",
    "meta": {
        "intensity": "85%",
        "keywords": "loyal, carrier",
        "mood": "revolutionary"
    },
}
```

# Contributing
Feel free to submit a pull request or an issue!