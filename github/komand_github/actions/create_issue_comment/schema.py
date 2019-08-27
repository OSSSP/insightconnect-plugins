# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create an issue comment"


class Input:
    BODY = "body"
    ISSUE_NUMBER = "issue_number"
    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    

class Output:
    URL = "url"
    

class CreateIssueCommentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "body": {
      "type": "string",
      "title": "Body",
      "description": "Body text of issue",
      "order": 1
    },
    "issue_number": {
      "type": "number",
      "title": "Issue Number",
      "description": "Issue number",
      "order": 2
    },
    "organization": {
      "type": "string",
      "title": "Organization",
      "description": "Organizational owner of repository",
      "order": 4
    },
    "repository": {
      "type": "string",
      "title": "Repository",
      "description": "Repository to post issue",
      "order": 3
    }
  },
  "required": [
    "body",
    "issue_number",
    "repository"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateIssueCommentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)