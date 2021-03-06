# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get the ZenHub Board Data for a GitHub Repository"


class Input:
    REPO_ID = "repo_id"
    

class Output:
    DATA = "data"
    

class GetRepositoryBoardDataInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "repo_id": {
      "type": "integer",
      "title": "Repository ID",
      "description": "GitHub Repository ID e.g. 24237263",
      "order": 1
    }
  },
  "required": [
    "repo_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetRepositoryBoardDataOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/repository_data",
      "title": "Board Data",
      "description": "ZenHub Repository Board Data",
      "order": 1
    }
  },
  "definitions": {
    "issue_data": {
      "type": "object",
      "title": "issue_data",
      "properties": {
        "estimate_value": {
          "type": "integer",
          "title": "Estimated Value",
          "description": "Estimated value",
          "order": 6
        },
        "is_epic": {
          "type": "boolean",
          "title": "Is epic",
          "description": "Is epic",
          "order": 3
        },
        "issue_number": {
          "type": "integer",
          "title": "Issue number",
          "description": "Issue number",
          "order": 1
        },
        "pipeline_name": {
          "type": "string",
          "title": "Pipeline Name",
          "description": "Pipeline name",
          "order": 5
        },
        "plus_ones": {
          "type": "array",
          "title": "Plus One",
          "description": "Plus one",
          "items": {
            "$ref": "#/definitions/plus_one"
          },
          "order": 7
        },
        "position": {
          "type": "integer",
          "title": "Position",
          "description": "Position",
          "order": 4
        },
        "repo_id": {
          "type": "integer",
          "title": "Repo id",
          "description": "Repo id",
          "order": 2
        }
      },
      "definitions": {
        "plus_one": {
          "type": "object",
          "title": "plus_one",
          "properties": {
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "Created at",
              "format": "date-time",
              "order": 2
            },
            "user_id": {
              "type": "integer",
              "title": "User Id",
              "description": "User ID",
              "order": 1
            }
          }
        }
      }
    },
    "pipeline_data": {
      "type": "object",
      "title": "pipeline_data",
      "properties": {
        "issues": {
          "type": "array",
          "title": "Issues",
          "description": "Issues",
          "items": {
            "$ref": "#/definitions/issue_data"
          },
          "order": 3
        },
        "pipeline_id": {
          "type": "string",
          "title": "Pipeline ID",
          "description": "Pipeline id",
          "order": 1
        },
        "pipeline_name": {
          "type": "string",
          "title": "Pipeline Name",
          "description": "Pipeline name",
          "order": 2
        }
      },
      "definitions": {
        "issue_data": {
          "type": "object",
          "title": "issue_data",
          "properties": {
            "estimate_value": {
              "type": "integer",
              "title": "Estimated Value",
              "description": "Estimated value",
              "order": 6
            },
            "is_epic": {
              "type": "boolean",
              "title": "Is epic",
              "description": "Is epic",
              "order": 3
            },
            "issue_number": {
              "type": "integer",
              "title": "Issue number",
              "description": "Issue number",
              "order": 1
            },
            "pipeline_name": {
              "type": "string",
              "title": "Pipeline Name",
              "description": "Pipeline name",
              "order": 5
            },
            "plus_ones": {
              "type": "array",
              "title": "Plus One",
              "description": "Plus one",
              "items": {
                "$ref": "#/definitions/plus_one"
              },
              "order": 7
            },
            "position": {
              "type": "integer",
              "title": "Position",
              "description": "Position",
              "order": 4
            },
            "repo_id": {
              "type": "integer",
              "title": "Repo id",
              "description": "Repo id",
              "order": 2
            }
          },
          "definitions": {
            "plus_one": {
              "type": "object",
              "title": "plus_one",
              "properties": {
                "created_at": {
                  "type": "string",
                  "title": "Created At",
                  "displayType": "date",
                  "description": "Created at",
                  "format": "date-time",
                  "order": 2
                },
                "user_id": {
                  "type": "integer",
                  "title": "User Id",
                  "description": "User ID",
                  "order": 1
                }
              }
            }
          }
        },
        "plus_one": {
          "type": "object",
          "title": "plus_one",
          "properties": {
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "Created at",
              "format": "date-time",
              "order": 2
            },
            "user_id": {
              "type": "integer",
              "title": "User Id",
              "description": "User ID",
              "order": 1
            }
          }
        }
      }
    },
    "plus_one": {
      "type": "object",
      "title": "plus_one",
      "properties": {
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Created at",
          "format": "date-time",
          "order": 2
        },
        "user_id": {
          "type": "integer",
          "title": "User Id",
          "description": "User ID",
          "order": 1
        }
      }
    },
    "repository_data": {
      "type": "object",
      "title": "repository_data",
      "properties": {
        "pipelines": {
          "type": "array",
          "title": "Pipelines",
          "description": "Pipelines",
          "items": {
            "$ref": "#/definitions/pipeline_data"
          },
          "order": 1
        }
      },
      "definitions": {
        "issue_data": {
          "type": "object",
          "title": "issue_data",
          "properties": {
            "estimate_value": {
              "type": "integer",
              "title": "Estimated Value",
              "description": "Estimated value",
              "order": 6
            },
            "is_epic": {
              "type": "boolean",
              "title": "Is epic",
              "description": "Is epic",
              "order": 3
            },
            "issue_number": {
              "type": "integer",
              "title": "Issue number",
              "description": "Issue number",
              "order": 1
            },
            "pipeline_name": {
              "type": "string",
              "title": "Pipeline Name",
              "description": "Pipeline name",
              "order": 5
            },
            "plus_ones": {
              "type": "array",
              "title": "Plus One",
              "description": "Plus one",
              "items": {
                "$ref": "#/definitions/plus_one"
              },
              "order": 7
            },
            "position": {
              "type": "integer",
              "title": "Position",
              "description": "Position",
              "order": 4
            },
            "repo_id": {
              "type": "integer",
              "title": "Repo id",
              "description": "Repo id",
              "order": 2
            }
          },
          "definitions": {
            "plus_one": {
              "type": "object",
              "title": "plus_one",
              "properties": {
                "created_at": {
                  "type": "string",
                  "title": "Created At",
                  "displayType": "date",
                  "description": "Created at",
                  "format": "date-time",
                  "order": 2
                },
                "user_id": {
                  "type": "integer",
                  "title": "User Id",
                  "description": "User ID",
                  "order": 1
                }
              }
            }
          }
        },
        "pipeline_data": {
          "type": "object",
          "title": "pipeline_data",
          "properties": {
            "issues": {
              "type": "array",
              "title": "Issues",
              "description": "Issues",
              "items": {
                "$ref": "#/definitions/issue_data"
              },
              "order": 3
            },
            "pipeline_id": {
              "type": "string",
              "title": "Pipeline ID",
              "description": "Pipeline id",
              "order": 1
            },
            "pipeline_name": {
              "type": "string",
              "title": "Pipeline Name",
              "description": "Pipeline name",
              "order": 2
            }
          },
          "definitions": {
            "issue_data": {
              "type": "object",
              "title": "issue_data",
              "properties": {
                "estimate_value": {
                  "type": "integer",
                  "title": "Estimated Value",
                  "description": "Estimated value",
                  "order": 6
                },
                "is_epic": {
                  "type": "boolean",
                  "title": "Is epic",
                  "description": "Is epic",
                  "order": 3
                },
                "issue_number": {
                  "type": "integer",
                  "title": "Issue number",
                  "description": "Issue number",
                  "order": 1
                },
                "pipeline_name": {
                  "type": "string",
                  "title": "Pipeline Name",
                  "description": "Pipeline name",
                  "order": 5
                },
                "plus_ones": {
                  "type": "array",
                  "title": "Plus One",
                  "description": "Plus one",
                  "items": {
                    "$ref": "#/definitions/plus_one"
                  },
                  "order": 7
                },
                "position": {
                  "type": "integer",
                  "title": "Position",
                  "description": "Position",
                  "order": 4
                },
                "repo_id": {
                  "type": "integer",
                  "title": "Repo id",
                  "description": "Repo id",
                  "order": 2
                }
              },
              "definitions": {
                "plus_one": {
                  "type": "object",
                  "title": "plus_one",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "title": "Created At",
                      "displayType": "date",
                      "description": "Created at",
                      "format": "date-time",
                      "order": 2
                    },
                    "user_id": {
                      "type": "integer",
                      "title": "User Id",
                      "description": "User ID",
                      "order": 1
                    }
                  }
                }
              }
            },
            "plus_one": {
              "type": "object",
              "title": "plus_one",
              "properties": {
                "created_at": {
                  "type": "string",
                  "title": "Created At",
                  "displayType": "date",
                  "description": "Created at",
                  "format": "date-time",
                  "order": 2
                },
                "user_id": {
                  "type": "integer",
                  "title": "User Id",
                  "description": "User ID",
                  "order": 1
                }
              }
            }
          }
        },
        "plus_one": {
          "type": "object",
          "title": "plus_one",
          "properties": {
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "Created at",
              "format": "date-time",
              "order": 2
            },
            "user_id": {
              "type": "integer",
              "title": "User Id",
              "description": "User ID",
              "order": 1
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
