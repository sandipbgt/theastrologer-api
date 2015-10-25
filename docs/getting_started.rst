Getting Started
===============

This document will show you how to get up and running with theastrologer-api.

Installation
------------

Clone the repository and install the libaries using pip::

    $ git clone https://github.com/sandipbgt/theastrologer-api.git
    $ cd theastrologer-api
    $ pip install -r requirements.txt
    $ gunicorn app:app

Configuration
-------------

To use the Twilio SMS API, you need to have some environment variables
configured.
Copy the below commands and paste it at the end of your ``~/.bashrc`` profile
and type ``source ~/.bashrc`` in your terminal to add these environment variables.::

    ### theastrologer-api environment variables for Twilio SMS
    export TWILIO_ACCOUNT_SID="your twilio account sid"
    export TWILIO_AUTH_TOKEN="your twilio auth token"
    export TWILIO_TO_PHONE="verified number for which to send sms"
    export TWILIO_FROM_PHONE="your twilio phone number"

.. note:: You must have ``Twilio API`` environment variables configured to use ``SMS`` features.