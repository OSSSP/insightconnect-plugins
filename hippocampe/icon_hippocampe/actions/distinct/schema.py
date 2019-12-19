# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Return all distinct values that match the given intelligence types"


class Input:
    INTELLIGENCE_TYPES = "intelligence_types"
    

class Output:
    VALUES = "values"
    

class DistinctInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "intelligence_types": {
      "type": "array",
      "title": "Intelligence Types",
      "description": "Intelligence types, e.g. 'ip' or 'url'",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "intelligence_types"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DistinctOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "values": {
      "type": "object",
      "title": "Values",
      "description": "Matching distinct values, one key per intelligence type",
      "order": 1
    }
  },
  "required": [
    "values"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)