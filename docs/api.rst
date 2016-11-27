API Endpoints
=============

The readonly ``API`` are documented here.

Feel free to use cURL and python to look at formatted json response. You can
also look at them in your browser, if it handles returned json.

::

    curl http://sandipbgt.com/theastrologer | python -m json.tool

Base
----
.. http:get:: /

   Retrieve author and project info

   **Example response**:

   .. sourcecode:: js

        {
            "author": "Sandip Bhagat",
            "author_url": "http://sandipbgt.com",
            "project_name": "theastrologer-api",
            "github": "https://github.com/sandipbgt/theastrologer-api",
            "api": "http://sandipbgt.com/theastrologer/api"
        }

Root
----

.. http:get:: /api

   Retrieve list of api resources.

   **Example response**:

   .. sourcecode:: js

    {
        "sunsign_list": "http://sandipbgt.com/theastrologer/api/sunsigns",
        "today": "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/today",
        "yesterday": "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/yesterday",
        "tomorrow": "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/tomorrow"
    }
    
Horoscope
---------

.. http:get:: /api/horoscope/{sunsign}/today

   Retrieve today's horoscope

   :param sunsign: horoscope's sunsign
   :type sunsign: string

   **Example response**:

   .. sourcecode:: js

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

.. http:post:: /api/horoscope/{sunsign}/today

   Sends today's horoscope as SMS via Twilio API.

   .. note:: You must have ``Twilio API`` environment variables configured to use ``SMS`` features.

   :param sunsign: horoscope's sunsign
   :type sunsign: string

   **Example response**:

   .. sourcecode:: js

      {
        "code": 201,
        "message": "success"
      }

.. http:get:: /api/horoscope/{sunsign}/tomorrow

   Retrieve tomorrow's horoscope

   :param sunsign: horoscope's sunsign
   :type sunsign: string

   **Example response**:

   .. sourcecode:: js

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

.. http:get:: /api/horoscope/{sunsign}/yesterday

   Retrieve yesterday's horoscope

   :param sunsign: horoscope's sunsign
   :type sunsign: string

   **Example response**:

   .. sourcecode:: js

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
