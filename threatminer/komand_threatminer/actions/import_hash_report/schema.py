# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Fetches information related to a hash"


class Input:
    QUERY = "query"
    

class Output:
    RESPONSE = "response"
    

class ImportHashReportInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "SHA1 hash to search e.g. 1f4f257947c1b713ca7f9bc25f914039",
      "order": 1
    }
  },
  "required": [
    "query"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ImportHashReportOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "response": {
      "type": "object",
      "title": "response",
      "properties": {
        "results": {
          "type": "array",
          "title": "Results",
          "description": "Results",
          "items": {
            "type": "object"
          },
          "order": 3
        },
        "status_code": {
          "type": "integer",
          "title": "Status Code",
          "description": "Status Code",
          "order": 1
        },
        "status_message": {
          "type": "string",
          "title": "Status Message",
          "description": "Status message",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
