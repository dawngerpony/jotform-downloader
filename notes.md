Notes
=====

* Notes go here!



    curl -vsX GET "https://eu-api.jotform.com/user?apiKey=$JOTFORM_API_KEY"
    curl -vsX GET "https://eu-api.jotform.com/user/submissions?apiKey=$JOTFORM_API_KEY" > all_submissions-`date +%s`.json

Sample Data
-----------

    {
        "submissions": [
          {
            "status": "ACTIVE",
            "form_id": "61005935839359",
            "ip": "213.205.252.243",
            "created_at": "2016-04-21 23:56:35",
            "updated_at": "2016-05-01 13:31:51",
            "answers": {
              "56": {
                "answer": "",
                "text": "Other Remuneration agreed",
                "type": "control_textarea"
              },
              "42": {
                "answer": "none",
                "text": "What other technical needs do you have?\u00a0",
                "type": "control_textarea"
              },
              "43": {
                "answer": "none",
                "text": "Do you need any furniture, such as chairs, stools or tables on stage?",
                "type": "control_textarea"
              },
              "60": {
                "answer": "https://www.facebook.com/noisyboysie/",
                "text": "A link to your Facebook profile",
                "type": "control_textbox"
              },
              "61": {
                "answer": "Noisy Boysie",
                "text": "Stage Name",
                "type": "control_textbox"
              },
              "53": {
                "answer": "\u00a340",
                "text": "Remuneration",
                "type": "control_textbox"
              },
              "52": {
                "answer": "DJ Performance",
                "text": "Description of Performance",
                "type": "control_radio"
              },
              "26": {
                "answer": "I&#039;ll bring my Traktor and Laptop",
                "text": "Media to be used during performance (Equipment requirements)",
                "type": "control_textarea"
              },
              "27": {
                "answer": "none",
                "text": "Other requirements",
                "type": "control_textarea"
              },
              "20": {
                "answer": "07817715292",
                "text": "Phone number (pre-event)",
                "type": "control_textbox"
              },
              "21": {
                "answer": {
                  "hourSelect": "23",
                  "minuteSelect": "00"
                },
                "text": "Start time of performance",
                "type": "control_time",
                "prettyFormat": "23:00"
              },
              "22": {
                "answer": {
                  "year": "2016",
                  "day": "29",
                  "month": "07"
                },
                "text": "Date of performance",
                "type": "control_datetime",
                "prettyFormat": "29-07-2016"
              },
              "23": {
                "answer": {
                  "hourSelect": "0",
                  "minuteSelect": "00"
                },
                "text": "End time of performance",
                "type": "control_time",
                "prettyFormat": "0:00"
              },
              "47": {
                "answer": "Lets make some Noise",
                "text": "Please provide up to 75 words describing your act for us to use for marketing purposes.",
                "type": "control_textarea"
              },
              "45": {
                "text": "<h1>Marketing Information</h1>\n<p>The more you give us, the more marketing love we can give you and your performance.</p>",
                "type": "control_text"
              },
              "28": {
                "text": "<h2>Clause 3: Remuneration</h2>\n<p>The Performer shall receive the following remuneration from the Hirer per live performance:</p>",
                "type": "control_text"
              },
              "29": {
                "answer": "Pip Boys = Guest\r\n1/2 = Alex Boys\r\nAs I have paid and the 2 above can they be refunded pls?\r\nI also have pre paid for car pass can this be refunded also please?\r\n",
                "text": "Full Name(s) of Half Price +1 Guest(s)",
                "type": "control_textarea"
              },
              "41": {
                "answer": "2 13a plugs",
                "text": "if applicable, what kind of power will you need (How many plugs)?",
                "type": "control_textarea"
              },
              "3": {
                "text": "<p>This contract defines the terms for hiring a DJ or performer for his or her participation in a live performance. It specifies the obligations of the hirer of the live performance as well as the obligations of the DJ or performer.</p>",
                "type": "control_text"
              },
              "4": {
                "text": "<h3>We ask that you promote your performance at Chilled in a Field Festival to your networks at least 1 month beforehand.</h3>\n<p>Please ensure that you tag Chilled in a Field Festival in any Facebook or Twitter (<a href=\"https://twitter.com/ChilledInAField\">@ChilledInAField</a>) activity. Thanks.</p>",
                "type": "control_text"
              },
              "7": {
                "text": "<h2>Clause 1: \u00a0Event Information</h2>\n<p>Chilled in a Field Festival 2016<br />Open : midday 29 July 2016<br />Close : midnight 31 July 2016<br /><span style=\"font-size:12pt;\"><strong>The Hop Farm, Maidstone Rd, Paddock Wood, Kent TN12 6PY</strong></span></p>",
                "type": "control_text"
              },
              "6": {
                "text": "<p>Parties:</p>\n<p>1) \u00a0The DJ or Performer, herein after referred to as THE PERFORMER:</p>\n<p><strong>Noisy Boysie</strong></p>\n<p>2) The LIVE PERFORMANCE HIRER:</p>\n<p><strong>Chilled in a Field Festival of 52 Knollys Road, London, SW16 2JX (hereinafter referred to as the HIRER)</strong></p>\n<p>\u00a0</p>",
                "type": "control_text"
              },
              "8": {
                "text": "<h2>Clause 2: \u00a0Performer Information</h2>\n<p>The Performer is hired to participate in the following live performance/s:</p>",
                "type": "control_text"
              },
              "77": {
                "text": "<p>NB. Please arrive at least 15 minutes before the start of your set, or longer (e.g. 30min)\u00a0if you have complex equipment (e.g. a controller) to plug in.</p>",
                "type": "control_text"
              },
              "76": {
                "answer": [],
                "text": "Please upload a biog.",
                "type": "control_fileupload"
              },
              "75": {
                "answer": "",
                "text": "Phone number on the day, if different",
                "type": "control_textbox"
              },
              "74": {
                "text": "<p>Please provide us with a couple of photos that we can use for marketing purposes.</p>",
                "type": "control_text"
              },
              "73": {
                "answer": [],
                "text": "Marketing photo #2",
                "type": "control_fileupload"
              },
              "72": {
                "answer": [
                  "http://www.jotform.com/uploads/dafyddciaff/61005935839359/337106593342614273/1.jpg"
                ],
                "text": "Marketing photo #1",
                "type": "control_fileupload"
              },
              "58": {
                "answer": "https://twitter.com/NoisyBoysieDJ",
                "text": "A link to your Twitter profile",
                "type": "control_textbox"
              },
              "10": {
                "answer": "Boysie",
                "text": "Members of act",
                "type": "control_textarea"
              },
              "12": {
                "answer": "",
                "text": "Details of Public Liability Insurance (if applicable)",
                "type": "control_textbox"
              },
              "59": {
                "answer": "https://www.mixcloud.com/noisyboysie/",
                "text": "A link to your SoundCloud/YouTube profile",
                "type": "control_textbox"
              },
              "14": {
                "text": "<h3>Chilled in a Field Contact (name, number and email)</h3>\n<p>Rob Baggs \u00a007595 526743 \u00a0robabaggs@gmail.com</p>\n<p>\u00a0</p>",
                "type": "control_text"
              },
              "17": {
                "answer": "markboys@hotmail.co.uk",
                "text": "E-mail",
                "type": "control_email"
              },
              "16": {
                "answer": [
                  "Woodland Stage"
                ],
                "text": "Location of Performance",
                "type": "control_checkbox",
                "prettyFormat": "Woodland Stage"
              },
              "19": {
                "text": "<h3>Main Contact</h3>",
                "type": "control_text"
              },
              "18": {
                "answer": {
                  "last": "Boys",
                  "first": "Mark"
                },
                "text": "Full Name",
                "type": "control_fullname",
                "prettyFormat": "Mark Boys"
              },
              "31": {
                "answer": "2",
                "text": "Number of Drinks Tokens agreed",
                "type": "control_textbox"
              },
              "30": {
                "answer": "1",
                "text": "Number of Car Park Tickets agreed",
                "type": "control_textbox"
              },
              "36": {
                "text": "<h3>Thank you for performing at Chilled in a Field Festival.</h3>\n<p>Chilled in a Field Festival is a company limited by guarantee, registered in England Co. # 7584675<br />Registered office 52 Knollys Road, London, SW16 2JX.</p>",
                "type": "control_text"
              },
              "35": {
                "answer": "Mark Boys",
                "text": "Signed as a Deed by The Performer (type name)",
                "type": "control_textbox"
              },
              "34": {
                "text": "<p>Signed as Deed on behalf of The Hirer</p>\n<p>Rob Baggs</p>",
                "type": "control_text"
              },
              "33": {
                "text": "<h2>Conditions</h2>\n<ul><li>Artists deemed not to be in a fit state to perform may have their performance cancelled by the Hirer. The decision to cancel a performance rests with the Hirer in their absolute discretion. Where the Hirer has cancelled a performance remuneration defined in Clause 3 will not be paid. Where a performance is cancelled by the Hirer due to fitness to perform being in question, the determination of which is at the Hirer's absolute discretion, then compensation will be sought to recompense the Hirer for the substitution of an alternative Artist deemed fit to perform.</li>\n<li>Where the performance is cancelled by the Artist or Hirer the Hirer will be entitled to seek compensation from the Artist for any expenses incurred as a result of the cancellation.</li>\n<li>The Artist will familiarise themselves with the health and safety guidance set out by the event organisers and adhere to the guidelines applicable to their performance.</li>\n<li>The Artist agrees not to breach copyright or broadcasting laws.</li>\n<li>The Artist(s) agrees to adhere to the laws of the country in which the contract is enacted.</li>\n<li>The Artist agrees not to disclose the terms of this contractual agreement to any other third party, specifically but not limited to other Artists booked by the Hirer and performing at the event.</li>\n<li>The Artist consents to the Hirer making any recording or video or taking any photographs of the performance in order for the - Hirer to use such images or recordings for promotional purposes.</li>\n<li>The parties shall inform each other of any change of address or contact details.</li>\n</ul><p>\u00a0</p>",
                "type": "control_text"
              },
              "54": {
                "answer": "1",
                "text": "Number of Meal Tokens agreed",
                "type": "control_textbox"
              },
              "57": {
                "answer": "http://noisyboysie.co.uk",
                "text": "A link to your website",
                "type": "control_textbox"
              }
            },
            "flag": "0",
            "new": "0",
            "id": "337106593342614273"
          }
        ],
        "form": {
          "username": "dafyddciaff",
          "status": "ENABLED",
          "title": "DJ - Noisy Boysie - Chilled in a Field Festival 2016 Contract for Hire and Booking Confirmation",
          "url": "https://form.jotformeu.com/form/61005935839359",
          "created_at": "2016-04-10 14:13:37",
          "updated_at": "2016-04-14 12:29:29",
          "height": "5673",
          "last_submission": "2016-04-21 23:56:35",
          "new": "0",
          "id": "61005935839359",
          "count": "1"
        }
    }
