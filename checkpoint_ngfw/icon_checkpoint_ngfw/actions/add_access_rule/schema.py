# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a rule to block traffic"


class Input:
    ACTION = "action"
    DESTINATION = "destination"
    DISCARD_OTHER_SESSIONS = "discard_other_sessions"
    LAYER = "layer"
    LIST_OF_SERVICES = "list_of_services"
    NAME = "name"
    POSITION = "position"
    SOURCE = "source"
    

class Output:
    ACCESS_RULE = "access_rule"
    

class AddAccessRuleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Action to take",
      "default": "Drop",
      "enum": [
        "Accept",
        "Drop",
        "Ask",
        "Inform",
        "Reject",
        "User Auth",
        "Client Auth",
        "Apply Layer"
      ],
      "order": 6
    },
    "destination": {
      "type": "string",
      "title": "Destination",
      "description": "Destination network object name",
      "order": 5
    },
    "discard_other_sessions": {
      "type": "boolean",
      "title": "Discard Other Sessions",
      "description": "Discard all other user sessions. This can fix errors when objects are locked by other sessions",
      "default": true,
      "order": 8
    },
    "layer": {
      "type": "string",
      "title": "Layer",
      "description": "Layer to add this rule to",
      "default": "Network",
      "order": 3
    },
    "list_of_services": {
      "type": "array",
      "title": "List of Services",
      "description": "List of services to block e.g. [\\"AOL\\", \\"SMTP\\"]",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Rule name",
      "order": 1
    },
    "position": {
      "type": "string",
      "title": "Position",
      "description": "Position in the list of rules. e.g. top, bottom, 15",
      "default": "top",
      "order": 7
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Source network object name",
      "order": 4
    }
  },
  "required": [
    "action",
    "discard_other_sessions",
    "layer",
    "name",
    "position"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddAccessRuleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "access_rule": {
      "$ref": "#/definitions/access_rule",
      "title": "Block Rule",
      "description": "The rule that was created",
      "order": 1
    }
  },
  "required": [
    "access_rule"
  ],
  "definitions": {
    "access_rule": {
      "type": "object",
      "title": "access_rule",
      "properties": {
        "action": {
          "$ref": "#/definitions/action_type",
          "title": "Action",
          "description": "Action",
          "order": 24
        },
        "action-settings": {
          "type": "object",
          "title": "Action-Settings",
          "description": "Action-settings",
          "order": 23
        },
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Comments",
          "order": 11
        },
        "content": {
          "type": "array",
          "title": "Content",
          "description": "Content",
          "items": {
            "$ref": "#/definitions/action_type"
          },
          "order": 12
        },
        "content-direction": {
          "type": "string",
          "title": "Content-Direction",
          "description": "Content-direction",
          "order": 5
        },
        "content-negate": {
          "type": "boolean",
          "title": "Content-Negate",
          "description": "Content-negate",
          "order": 6
        },
        "custom-fields": {
          "type": "object",
          "title": "Custom-Fields",
          "description": "Custom-fields",
          "order": 3
        },
        "destination": {
          "type": "array",
          "title": "Destination",
          "description": "Destination",
          "items": {
            "$ref": "#/definitions/action_type"
          },
          "order": 10
        },
        "destination-negate": {
          "type": "boolean",
          "title": "Destination-Negate",
          "description": "Destination-negate",
          "order": 14
        },
        "domain": {
          "$ref": "#/definitions/domain",
          "title": "Domain",
          "description": "Domain",
          "order": 1
        },
        "enabled": {
          "type": "boolean",
          "title": "Enabled",
          "description": "Enabled",
          "order": 21
        },
        "install-on": {
          "type": "array",
          "title": "Install-On",
          "description": "Install-on",
          "items": {
            "$ref": "#/definitions/action_type"
          },
          "order": 18
        },
        "layer": {
          "type": "string",
          "title": "Layer",
          "description": "Layer",
          "order": 4
        },
        "meta-info": {
          "$ref": "#/definitions/meta_info_type",
          "title": "Meta-Info",
          "description": "Meta-info",
          "order": 22
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 19
        },
        "service": {
          "type": "array",
          "title": "Service",
          "description": "Service",
          "items": {
            "$ref": "#/definitions/objects_dictionary_type"
          },
          "order": 9
        },
        "service-negate": {
          "type": "boolean",
          "title": "Service-Negate",
          "description": "Service-negate",
          "order": 20
        },
        "source": {
          "type": "array",
          "title": "Source",
          "description": "Source",
          "items": {
            "$ref": "#/definitions/action_type"
          },
          "order": 13
        },
        "source-negate": {
          "type": "boolean",
          "title": "Source-Negate",
          "description": "Source-negate",
          "order": 7
        },
        "time": {
          "type": "array",
          "title": "Time",
          "description": "Time",
          "items": {
            "$ref": "#/definitions/action_type"
          },
          "order": 17
        },
        "track": {
          "$ref": "#/definitions/track",
          "title": "Track",
          "description": "Track",
          "order": 16
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 15
        },
        "uid": {
          "type": "string",
          "title": "UID",
          "description": "UID",
          "order": 2
        },
        "vpn": {
          "type": "array",
          "title": "VPN",
          "description": "VPN",
          "items": {
            "$ref": "#/definitions/action_type"
          },
          "order": 8
        }
      },
      "definitions": {
        "action_type": {
          "type": "object",
          "title": "action_type",
          "properties": {
            "domain": {
              "$ref": "#/definitions/domain",
              "title": "Domain",
              "description": "Domain",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 2
            },
            "uid": {
              "type": "string",
              "title": "UID",
              "description": "UID",
              "order": 4
            }
          },
          "definitions": {
            "domain": {
              "type": "object",
              "title": "domain",
              "properties": {
                "domain-type": {
                  "type": "string",
                  "title": "Domain",
                  "description": "Domain",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 2
                },
                "uid": {
                  "type": "string",
                  "title": "UID",
                  "description": "UID",
                  "order": 3
                }
              }
            }
          }
        },
        "creation_time_type": {
          "type": "object",
          "title": "creation_time_type",
          "properties": {
            "iso-8601": {
              "type": "string",
              "title": "ISO-8601",
              "description": "ISO-8601",
              "order": 2
            },
            "posix": {
              "type": "integer",
              "title": "POSIX",
              "description": "POSIX",
              "order": 1
            }
          }
        },
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "domain-type": {
              "type": "string",
              "title": "Domain",
              "description": "Domain",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "uid": {
              "type": "string",
              "title": "UID",
              "description": "UID",
              "order": 3
            }
          }
        },
        "meta_info_type": {
          "type": "object",
          "title": "meta_info_type",
          "properties": {
            "creation-time": {
              "$ref": "#/definitions/creation_time_type",
              "title": "Creation-Time",
              "description": "Creation-time",
              "order": 2
            },
            "creator": {
              "type": "string",
              "title": "Creator",
              "description": "Creator",
              "order": 6
            },
            "last-modifier": {
              "type": "string",
              "title": "Last-Modifier",
              "description": "Last-modifier",
              "order": 3
            },
            "last-modify-time": {
              "$ref": "#/definitions/creation_time_type",
              "title": "Last-Modify-Time",
              "description": "Last-modify-time",
              "order": 4
            },
            "lock": {
              "type": "string",
              "title": "Lock",
              "description": "Lock",
              "order": 5
            },
            "validation-state": {
              "type": "string",
              "title": "Validation-State",
              "description": "Validation-state",
              "order": 1
            }
          },
          "definitions": {
            "creation_time_type": {
              "type": "object",
              "title": "creation_time_type",
              "properties": {
                "iso-8601": {
                  "type": "string",
                  "title": "ISO-8601",
                  "description": "ISO-8601",
                  "order": 2
                },
                "posix": {
                  "type": "integer",
                  "title": "POSIX",
                  "description": "POSIX",
                  "order": 1
                }
              }
            }
          }
        },
        "objects_dictionary_type": {
          "type": "object",
          "title": "objects_dictionary_type",
          "properties": {
            "color": {
              "type": "string",
              "title": "Color",
              "description": "Color",
              "order": 4
            },
            "comments": {
              "type": "string",
              "title": "Comments",
              "description": "Comments",
              "order": 5
            },
            "customFields": {
              "type": "object",
              "title": "Custom Fields",
              "description": "Custom fields",
              "order": 9
            },
            "display-name": {
              "type": "string",
              "title": "Display-Name",
              "description": "Display-name",
              "order": 11
            },
            "domain": {
              "$ref": "#/definitions/domain",
              "title": "Domain",
              "description": "Domain",
              "order": 1
            },
            "icon": {
              "type": "string",
              "title": "Icon",
              "description": "Icon",
              "order": 12
            },
            "meta-info": {
              "$ref": "#/definitions/meta_info_type",
              "title": "Meta-Info",
              "description": "Meta-info",
              "order": 6
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "port": {
              "type": "string",
              "title": "Port",
              "description": "Port",
              "order": 7
            },
            "tags": {
              "type": "array",
              "title": "Tags",
              "description": "Tags",
              "items": {
                "type": "object"
              },
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 10
            },
            "uid": {
              "type": "string",
              "title": "UID",
              "description": "UID",
              "order": 8
            }
          },
          "definitions": {
            "creation_time_type": {
              "type": "object",
              "title": "creation_time_type",
              "properties": {
                "iso-8601": {
                  "type": "string",
                  "title": "ISO-8601",
                  "description": "ISO-8601",
                  "order": 2
                },
                "posix": {
                  "type": "integer",
                  "title": "POSIX",
                  "description": "POSIX",
                  "order": 1
                }
              }
            },
            "domain": {
              "type": "object",
              "title": "domain",
              "properties": {
                "domain-type": {
                  "type": "string",
                  "title": "Domain",
                  "description": "Domain",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 2
                },
                "uid": {
                  "type": "string",
                  "title": "UID",
                  "description": "UID",
                  "order": 3
                }
              }
            },
            "meta_info_type": {
              "type": "object",
              "title": "meta_info_type",
              "properties": {
                "creation-time": {
                  "$ref": "#/definitions/creation_time_type",
                  "title": "Creation-Time",
                  "description": "Creation-time",
                  "order": 2
                },
                "creator": {
                  "type": "string",
                  "title": "Creator",
                  "description": "Creator",
                  "order": 6
                },
                "last-modifier": {
                  "type": "string",
                  "title": "Last-Modifier",
                  "description": "Last-modifier",
                  "order": 3
                },
                "last-modify-time": {
                  "$ref": "#/definitions/creation_time_type",
                  "title": "Last-Modify-Time",
                  "description": "Last-modify-time",
                  "order": 4
                },
                "lock": {
                  "type": "string",
                  "title": "Lock",
                  "description": "Lock",
                  "order": 5
                },
                "validation-state": {
                  "type": "string",
                  "title": "Validation-State",
                  "description": "Validation-state",
                  "order": 1
                }
              },
              "definitions": {
                "creation_time_type": {
                  "type": "object",
                  "title": "creation_time_type",
                  "properties": {
                    "iso-8601": {
                      "type": "string",
                      "title": "ISO-8601",
                      "description": "ISO-8601",
                      "order": 2
                    },
                    "posix": {
                      "type": "integer",
                      "title": "POSIX",
                      "description": "POSIX",
                      "order": 1
                    }
                  }
                }
              }
            }
          }
        },
        "track": {
          "type": "object",
          "title": "track",
          "properties": {
            "accounting": {
              "type": "boolean",
              "title": "Accounting",
              "description": "Accounting",
              "order": 2
            },
            "alert": {
              "type": "string",
              "title": "Alert",
              "description": "Alert",
              "order": 5
            },
            "per-connection": {
              "type": "boolean",
              "title": "Per-Connection",
              "description": "Per-connection",
              "order": 1
            },
            "per-session": {
              "type": "boolean",
              "title": "Per-Session",
              "description": "Per-session",
              "order": 4
            },
            "type": {
              "$ref": "#/definitions/action_type",
              "title": "Type",
              "description": "Type",
              "order": 3
            }
          },
          "definitions": {
            "action_type": {
              "type": "object",
              "title": "action_type",
              "properties": {
                "domain": {
                  "$ref": "#/definitions/domain",
                  "title": "Domain",
                  "description": "Domain",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 3
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Type",
                  "order": 2
                },
                "uid": {
                  "type": "string",
                  "title": "UID",
                  "description": "UID",
                  "order": 4
                }
              },
              "definitions": {
                "domain": {
                  "type": "object",
                  "title": "domain",
                  "properties": {
                    "domain-type": {
                      "type": "string",
                      "title": "Domain",
                      "description": "Domain",
                      "order": 1
                    },
                    "name": {
                      "type": "string",
                      "title": "Name",
                      "description": "Name",
                      "order": 2
                    },
                    "uid": {
                      "type": "string",
                      "title": "UID",
                      "description": "UID",
                      "order": 3
                    }
                  }
                }
              }
            },
            "domain": {
              "type": "object",
              "title": "domain",
              "properties": {
                "domain-type": {
                  "type": "string",
                  "title": "Domain",
                  "description": "Domain",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 2
                },
                "uid": {
                  "type": "string",
                  "title": "UID",
                  "description": "UID",
                  "order": 3
                }
              }
            }
          }
        }
      }
    },
    "action_type": {
      "type": "object",
      "title": "action_type",
      "properties": {
        "domain": {
          "$ref": "#/definitions/domain",
          "title": "Domain",
          "description": "Domain",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 2
        },
        "uid": {
          "type": "string",
          "title": "UID",
          "description": "UID",
          "order": 4
        }
      },
      "definitions": {
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "domain-type": {
              "type": "string",
              "title": "Domain",
              "description": "Domain",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "uid": {
              "type": "string",
              "title": "UID",
              "description": "UID",
              "order": 3
            }
          }
        }
      }
    },
    "creation_time_type": {
      "type": "object",
      "title": "creation_time_type",
      "properties": {
        "iso-8601": {
          "type": "string",
          "title": "ISO-8601",
          "description": "ISO-8601",
          "order": 2
        },
        "posix": {
          "type": "integer",
          "title": "POSIX",
          "description": "POSIX",
          "order": 1
        }
      }
    },
    "domain": {
      "type": "object",
      "title": "domain",
      "properties": {
        "domain-type": {
          "type": "string",
          "title": "Domain",
          "description": "Domain",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "uid": {
          "type": "string",
          "title": "UID",
          "description": "UID",
          "order": 3
        }
      }
    },
    "meta_info_type": {
      "type": "object",
      "title": "meta_info_type",
      "properties": {
        "creation-time": {
          "$ref": "#/definitions/creation_time_type",
          "title": "Creation-Time",
          "description": "Creation-time",
          "order": 2
        },
        "creator": {
          "type": "string",
          "title": "Creator",
          "description": "Creator",
          "order": 6
        },
        "last-modifier": {
          "type": "string",
          "title": "Last-Modifier",
          "description": "Last-modifier",
          "order": 3
        },
        "last-modify-time": {
          "$ref": "#/definitions/creation_time_type",
          "title": "Last-Modify-Time",
          "description": "Last-modify-time",
          "order": 4
        },
        "lock": {
          "type": "string",
          "title": "Lock",
          "description": "Lock",
          "order": 5
        },
        "validation-state": {
          "type": "string",
          "title": "Validation-State",
          "description": "Validation-state",
          "order": 1
        }
      },
      "definitions": {
        "creation_time_type": {
          "type": "object",
          "title": "creation_time_type",
          "properties": {
            "iso-8601": {
              "type": "string",
              "title": "ISO-8601",
              "description": "ISO-8601",
              "order": 2
            },
            "posix": {
              "type": "integer",
              "title": "POSIX",
              "description": "POSIX",
              "order": 1
            }
          }
        }
      }
    },
    "objects_dictionary_type": {
      "type": "object",
      "title": "objects_dictionary_type",
      "properties": {
        "color": {
          "type": "string",
          "title": "Color",
          "description": "Color",
          "order": 4
        },
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Comments",
          "order": 5
        },
        "customFields": {
          "type": "object",
          "title": "Custom Fields",
          "description": "Custom fields",
          "order": 9
        },
        "display-name": {
          "type": "string",
          "title": "Display-Name",
          "description": "Display-name",
          "order": 11
        },
        "domain": {
          "$ref": "#/definitions/domain",
          "title": "Domain",
          "description": "Domain",
          "order": 1
        },
        "icon": {
          "type": "string",
          "title": "Icon",
          "description": "Icon",
          "order": 12
        },
        "meta-info": {
          "$ref": "#/definitions/meta_info_type",
          "title": "Meta-Info",
          "description": "Meta-info",
          "order": 6
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "port": {
          "type": "string",
          "title": "Port",
          "description": "Port",
          "order": 7
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "object"
          },
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 10
        },
        "uid": {
          "type": "string",
          "title": "UID",
          "description": "UID",
          "order": 8
        }
      },
      "definitions": {
        "creation_time_type": {
          "type": "object",
          "title": "creation_time_type",
          "properties": {
            "iso-8601": {
              "type": "string",
              "title": "ISO-8601",
              "description": "ISO-8601",
              "order": 2
            },
            "posix": {
              "type": "integer",
              "title": "POSIX",
              "description": "POSIX",
              "order": 1
            }
          }
        },
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "domain-type": {
              "type": "string",
              "title": "Domain",
              "description": "Domain",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "uid": {
              "type": "string",
              "title": "UID",
              "description": "UID",
              "order": 3
            }
          }
        },
        "meta_info_type": {
          "type": "object",
          "title": "meta_info_type",
          "properties": {
            "creation-time": {
              "$ref": "#/definitions/creation_time_type",
              "title": "Creation-Time",
              "description": "Creation-time",
              "order": 2
            },
            "creator": {
              "type": "string",
              "title": "Creator",
              "description": "Creator",
              "order": 6
            },
            "last-modifier": {
              "type": "string",
              "title": "Last-Modifier",
              "description": "Last-modifier",
              "order": 3
            },
            "last-modify-time": {
              "$ref": "#/definitions/creation_time_type",
              "title": "Last-Modify-Time",
              "description": "Last-modify-time",
              "order": 4
            },
            "lock": {
              "type": "string",
              "title": "Lock",
              "description": "Lock",
              "order": 5
            },
            "validation-state": {
              "type": "string",
              "title": "Validation-State",
              "description": "Validation-state",
              "order": 1
            }
          },
          "definitions": {
            "creation_time_type": {
              "type": "object",
              "title": "creation_time_type",
              "properties": {
                "iso-8601": {
                  "type": "string",
                  "title": "ISO-8601",
                  "description": "ISO-8601",
                  "order": 2
                },
                "posix": {
                  "type": "integer",
                  "title": "POSIX",
                  "description": "POSIX",
                  "order": 1
                }
              }
            }
          }
        }
      }
    },
    "track": {
      "type": "object",
      "title": "track",
      "properties": {
        "accounting": {
          "type": "boolean",
          "title": "Accounting",
          "description": "Accounting",
          "order": 2
        },
        "alert": {
          "type": "string",
          "title": "Alert",
          "description": "Alert",
          "order": 5
        },
        "per-connection": {
          "type": "boolean",
          "title": "Per-Connection",
          "description": "Per-connection",
          "order": 1
        },
        "per-session": {
          "type": "boolean",
          "title": "Per-Session",
          "description": "Per-session",
          "order": 4
        },
        "type": {
          "$ref": "#/definitions/action_type",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      },
      "definitions": {
        "action_type": {
          "type": "object",
          "title": "action_type",
          "properties": {
            "domain": {
              "$ref": "#/definitions/domain",
              "title": "Domain",
              "description": "Domain",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 2
            },
            "uid": {
              "type": "string",
              "title": "UID",
              "description": "UID",
              "order": 4
            }
          },
          "definitions": {
            "domain": {
              "type": "object",
              "title": "domain",
              "properties": {
                "domain-type": {
                  "type": "string",
                  "title": "Domain",
                  "description": "Domain",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 2
                },
                "uid": {
                  "type": "string",
                  "title": "UID",
                  "description": "UID",
                  "order": 3
                }
              }
            }
          }
        },
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "domain-type": {
              "type": "string",
              "title": "Domain",
              "description": "Domain",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "uid": {
              "type": "string",
              "title": "UID",
              "description": "UID",
              "order": 3
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
