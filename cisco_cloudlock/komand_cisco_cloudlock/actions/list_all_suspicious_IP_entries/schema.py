# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Lists all suspicious IP entries"


class Input:
    LIMIT = "limit"
    NAME = "name"
    OFFSET = "offset"
    Q = "q"
    

class Output:
    ENTRIES = "entries"
    

class ListAllSuspiciousIPEntriesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "limit": {
      "type": "number",
      "title": "Limit",
      "description": "Number of paginated results to return. Max: 100",
      "default": 20,
      "order": 4
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Match a substring within entry name",
      "order": 2
    },
    "offset": {
      "type": "number",
      "title": "Offset",
      "description": "Pagination offset",
      "default": 0,
      "order": 3
    },
    "q": {
      "type": "string",
      "title": "Q",
      "description": "Match string",
      "enum": [
        "Name",
        "Location",
        "IP Address",
        "Categories"
      ],
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAllSuspiciousIPEntriesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "entries": {
      "type": "array",
      "title": "Suspicious IP Entries",
      "description": "Suspicious IP entries",
      "items": {
        "$ref": "#/definitions/suspicious_ip_entry"
      },
      "order": 1
    }
  },
  "definitions": {
    "suspicious_ip_entry": {
      "type": "object",
      "title": "suspicious_ip_entry",
      "properties": {
        "categories": {
          "type": "array",
          "title": "Categories",
          "description": "Item categories",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "created_on": {
          "type": "string",
          "title": "Created On",
          "displayType": "date",
          "description": "Creation date",
          "format": "date-time",
          "order": 8
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Library item description",
          "order": 2
        },
        "expires_on": {
          "type": "string",
          "title": "Expires On",
          "displayType": "date",
          "description": "Time to expire item from library",
          "format": "date-time",
          "order": 9
        },
        "ip_address": {
          "type": "string",
          "title": "Ip Address",
          "description": "IP address in library",
          "order": 3
        },
        "location": {
          "type": "string",
          "title": "Location",
          "description": "Item location",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Library item name",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Item type",
          "order": 5
        },
        "updated_on": {
          "type": "string",
          "title": "Updated On",
          "displayType": "date",
          "description": "Last update",
          "format": "date-time",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
