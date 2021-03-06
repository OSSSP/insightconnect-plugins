# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Decodes a Microsoft Safe Link"


class Input:
    URL = "url"
    

class Output:
    RESULT = "result"
    

class DecodeInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Safe Link to be decoded",
      "order": 1
    }
  },
  "required": [
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DecodeOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "string",
      "title": "Result",
      "description": "Result of the decoded Safe Link",
      "order": 1
    }
  },
  "required": [
    "result"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
