# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Lookup a file hash in Anomali"


class Input:
    HASH = "hash"
    

class Output:
    RESULTS = "results"
    

class LookupHashInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "Hash",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LookupHashOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Results returned",
      "items": {
        "$ref": "#/definitions/result"
      },
      "order": 1
    }
  },
  "definitions": {
    "result": {
      "type": "object",
      "title": "result",
      "properties": {
        "asn": {
          "type": "string",
          "title": "ASN",
          "description": "Autonomous system number",
          "order": 1
        },
        "classification": {
          "type": "string",
          "title": "Classification",
          "description": "Classification",
          "order": 2
        },
        "confidence": {
          "type": "string",
          "title": "Confidence",
          "description": "Confidence level",
          "order": 3
        },
        "country": {
          "type": "string",
          "title": "Country",
          "description": "Country",
          "order": 4
        },
        "date_first": {
          "type": "string",
          "title": "Date First",
          "description": "Date first",
          "order": 5
        },
        "date_last": {
          "type": "string",
          "title": "Date Last",
          "description": "Date last",
          "order": 6
        },
        "details2": {
          "type": "string",
          "title": "Details",
          "description": "Details",
          "order": 7
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "Domain",
          "order": 8
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 9
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 10
        },
        "itype": {
          "type": "string",
          "title": "Itype",
          "description": "Itype",
          "order": 11
        },
        "lat": {
          "type": "number",
          "title": "Latitude",
          "description": "Latitude",
          "order": 12
        },
        "lon": {
          "type": "number",
          "title": "Longitude",
          "description": "Longitude",
          "order": 13
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "MD5 Hash",
          "order": 14
        },
        "org": {
          "type": "string",
          "title": "Organization",
          "description": "Organization",
          "order": 15
        },
        "resource_uri": {
          "type": "string",
          "title": "Resource URI",
          "description": "Resource URI",
          "order": 16
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 17
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 18
        },
        "source_feed_id": {
          "type": "integer",
          "title": "Source Feed ID",
          "description": "Source Feed ID",
          "order": 19
        },
        "srcip": {
          "type": "string",
          "title": "Source IP",
          "description": "Source IP",
          "order": 20
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 21
        },
        "update_id": {
          "type": "string",
          "title": "Update ID",
          "description": "Update ID",
          "order": 22
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 23
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
