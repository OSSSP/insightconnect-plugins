# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Update a ServiceNow Incident with the given data"


class Input:
    SYSTEM_ID = "system_id"
    UPDATE_DATA = "update_data"
    

class Output:
    SUCCESS = "success"
    

class UpdateIncidentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "system_id": {
      "type": "string",
      "title": "System ID",
      "description": "System ID of the Incident record to update",
      "order": 1
    },
    "update_data": {
      "type": "object",
      "title": "Update Data",
      "description": "JSON object containing the fields and values to update",
      "order": 2
    }
  },
  "required": [
    "system_id",
    "update_data"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateIncidentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "True if the update was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
