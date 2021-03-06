# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Decode a Mimecast encoded URL"


class Input:
    ENCODED_URL = "encoded_url"
    

class Output:
    DECODED_URL = "decoded_url"
    

class DecodeUrlInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "encoded_url": {
      "type": "string",
      "title": "Encoded URL",
      "description": "The Mimecast encoded URL (e.g. https://protect-xx.mimecast.com/...)",
      "order": 1
    }
  },
  "required": [
    "encoded_url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DecodeUrlOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "decoded_url": {
      "type": "string",
      "title": "Decoded URL",
      "description": "Original decoded URL",
      "order": 1
    }
  },
  "required": [
    "decoded_url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
