# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Send a message to a room"


class Input:
    MESSAGE = "message"
    ROOM_ID_OR_NAME = "room_id_or_name"
    

class Output:
    ID = "id"
    TIMESTAMP = "timestamp"
    

class PostInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "The message post to room. Valid length range: 1 - 1000",
      "order": 2
    },
    "room_id_or_name": {
      "type": "string",
      "title": "Room ID or Name",
      "description": "The ID or URL encoded name of the room",
      "order": 1
    }
  },
  "required": [
    "message",
    "room_id_or_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PostOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "Message ID",
      "description": "The unique identifier of the sent message",
      "order": 1
    },
    "timestamp": {
      "type": "string",
      "title": "Timestamp",
      "description": "The UTC timestamp representing when the message was processed",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)