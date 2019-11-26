# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Populate a JSON object with the specified fields of the given Incident"


class Input:
    FILTERING_FIELDS = "filtering_fields"
    SYSTEM_ID = "system_id"
    

class Output:
    FILTERED_INCIDENT = "filtered_incident"
    

class ReadIncidentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filtering_fields": {
      "type": "string",
      "title": "Filtering Fields",
      "description": "Comma-separated list of fields desired in output object (e.g. opened_by,number)",
      "order": 2
    },
    "system_id": {
      "type": "string",
      "title": "System ID",
      "description": "System ID of the Incident record from which to read",
      "order": 1
    }
  },
  "required": [
    "filtering_fields",
    "system_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReadIncidentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filtered_incident": {
      "type": "object",
      "title": "Filtered Incident",
      "description": "JSON object representing the incident containing the given fields",
      "order": 1
    }
  },
  "required": [
    "filtered_incident"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)