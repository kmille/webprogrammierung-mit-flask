#!/usr/bin/env python3

import zulip

c = zulip.Client()


# Get the 3 last messages sent by "iago@zulip.com" to the stream "Verona"
request = {
    'use_first_unread_anchor': True,
    'num_before': 100,
    'num_after': 10,
    'narrow': [{'operator': 'stream', 'operand': 'remote'},
               {'operator': 'topic',  'operand': 'Anti-Überwachungs-Router'}],
    'apply_markdown': False
}

messages = c.get_messages(request)['messages']
for message in messages:
    print("{}: {}".format(message['sender_full_name'], message['content']))

message = {
  "type": "stream",
  "to": 'remote',
  "subject": "Anti-Überwachungs-Router",
  "content": "api-test für morgen",
}
#x = c.send_message(message)

exit()

streams = c.get_streams()['streams']
for stream in streams:
    print(stream['name'], stream['stream_id'])

stream_id = 56


print("Lets get the topics\n\n\n")
topics = c.get_stream_topics(stream_id)['topics']
for topic in topics:
    print(topic['name'], topic['max_id'])









