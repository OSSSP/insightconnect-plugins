# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Looks for updates to a project"


class Input:
    
    FREQUENCY = "frequency"
    PROJECT_NAME = "project_name"
    

class Output:
    
    UPDATED_LIST = "updated_list"
    

class ProjectUpdatedInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "frequency": {
      "type": "integer",
      "title": "Frequency",
      "description": "The time between updates in seconds",
      "default": 300,
      "order": 2
    },
    "project_name": {
      "type": "string",
      "title": "Project Name",
      "description": "The name of the project to retrieve artifacts from",
      "order": 1
    }
  },
  "required": [
    "project_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ProjectUpdatedOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "updated_list": {
      "type": "array",
      "title": "Updated List",
      "description": "Results as list of JSON",
      "items": {
        "$ref": "#/definitions/artifact"
      },
      "order": 1
    }
  },
  "definitions": {
    "artifact": {
      "type": "object",
      "title": "artifact",
      "properties": {
        "created": {
          "type": "string",
          "title": "Created",
          "description": "Creation date",
          "order": 5
        },
        "creator": {
          "type": "string",
          "title": "Creator",
          "description": "Person or organization who added this artifact",
          "order": 3
        },
        "guid": {
          "type": "string",
          "title": "GUID",
          "description": "Artifact GUID",
          "order": 13
        },
        "links": {
          "$ref": "#/definitions/links",
          "title": "Links",
          "description": "Web links to project and artifact",
          "order": 6
        },
        "monitor": {
          "type": "boolean",
          "title": "Monitor",
          "description": "Monitor",
          "order": 1
        },
        "monitorable": {
          "type": "boolean",
          "title": "Monitorable",
          "description": "Artifact can be monitored",
          "order": 9
        },
        "organization": {
          "type": "string",
          "title": "Organization",
          "description": "Organization",
          "order": 10
        },
        "owner": {
          "type": "string",
          "title": "Owner",
          "description": "Artifact owner",
          "order": 8
        },
        "project": {
          "type": "string",
          "title": "Project",
          "description": "Project GUID",
          "order": 7
        },
        "query": {
          "type": "string",
          "title": "Query",
          "description": "Query",
          "order": 12
        },
        "system_tags": {
          "type": "array",
          "title": "System Tags",
          "description": "System assigned tag",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "tag_meta": {
          "type": "object",
          "title": "Tag Meta",
          "description": "Tag Meta",
          "order": 11
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of artifact eg. domain",
          "order": 14
        },
        "user_tags": {
          "type": "array",
          "title": "User Tags",
          "description": "User assigned tag",
          "items": {
            "type": "string"
          },
          "order": 2
        }
      },
      "definitions": {
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "project": {
              "type": "string",
              "title": "Project",
              "description": "Link to project",
              "order": 1
            },
            "self": {
              "type": "string",
              "title": "Self",
              "description": "Link to artifact",
              "order": 2
            },
            "tag": {
              "type": "string",
              "title": "Tag",
              "description": "Tag",
              "order": 3
            }
          }
        }
      }
    },
    "links": {
      "type": "object",
      "title": "links",
      "properties": {
        "project": {
          "type": "string",
          "title": "Project",
          "description": "Link to project",
          "order": 1
        },
        "self": {
          "type": "string",
          "title": "Self",
          "description": "Link to artifact",
          "order": 2
        },
        "tag": {
          "type": "string",
          "title": "Tag",
          "description": "Tag",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
