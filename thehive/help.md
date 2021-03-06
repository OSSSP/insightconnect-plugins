# Description

[TheHive](https://thehive-project.org/) TheHive is a scalable, open source security incident response solution
designed for SOCs & CERTs to collaborate, elaborate, analyze and get their job done.
Handle your case management needs with TheHive plugin for Rapid7 InsightConnect.

# Key Features

* Retrieve a list of cases or a specific case by ID
* Create a new case and close an existing case
* Create new tasks within a case
* Create new observables within a case
* Get user information

# Requirements

* TheHive instance hostname
* TheHive username and password

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Username and password|None|
|host|string|None|True|TheHive host e.g. thehive.company.com or 10.3.4.50|None|
|port|string|9000|True|TheHive API port e.g. 9000|None|
|protocol|string|None|True|HTTP Protocol|['http', 'https']|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTP or HTTPS as the key, and the proxy URL as the value|None|
|verify|boolean|True|True|Verify the certificate|None|

## Technical Details

### Actions

#### Create Task

This action is used to create a new case task.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|None|
|task|itask|None|True|Task name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|case|task|False|Create case task output|

Example output:

```

{
  "case": {
    "_type": "case_task",
    "user": "jschipp",
    "startDate": 1511303757000,
    "id": "AV_guT21YMfcbXhqb9vj",
    "description": "Blah",
    "status": "Waiting",
    "createdAt": 1511303757236,
    "createdBy": "jschipp",
    "order": 0,
    "title": "Blah Blah",
    "flag": false,
    "owner": "jschipp"
  }
}

```

#### Create Observable

This action is used to create a new case observable.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|None|
|observable|iobservable|None|True|Observable|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|case|observable|False|Create case observable output|

Example output:

```

{
  "case": {
    "status": "Ok",
    "id": "6dc39e0049512aea098de1793b942ff7",
    "user": "jschipp",
    "startDate": 1511303756229,
    "tlp": 2,
    "reports": {},
    "_id": "6dc39e0049512aea098de1793b942ff7",
    "dataType": "domain",
    "_type": "case_artifact",
    "data": "example4.com",
    "createdAt": 1511303756228,
    "message": "Blah",
    "createdBy": "jschipp",
    "ioc": false,
    "tags": [
      "blah"
    ]
  }
}

```
#### Get Cases

This action is used to retrieve a list of cases.

##### Input

_This action does not contain any inputs._

##### Output


|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]case|False|List of cases|

Example output:

```

{
  "list": [
    {
      "status": "Deleted",
      "createdBy": "jschipp",
      "owner": "jschipp",
      "_type": "case",
      "user": "jschipp",
      "updatedBy": "jschipp",
      "flag": false,
      "severity": 2,
      "description": "This is a case generated by Komand",
      "caseId": 21,
      "tlp": 2,
      "startDate": 1511314797000,
      "updatedAt": 1511314809671,
      "title": "Komand",
      "tags": [
        "test",
        "komand"
      ],
      "createdAt": 1511314797360,
      "metrics": {},
      "id": "AV_hYbT4YMfcbXhqb9v4",
      "customFields": {}
    },
    {
      "status": "Open",
      "createdBy": "jschipp",
      "owner": "jschipp",
      "_type": "case",
      "user": "jschipp",
      "flag": false,
      "severity": 2,
      "description": "This is a case generated by Komand",
      "caseId": 20,
      "tlp": 2,
      "startDate": 1511314704000,
      "title": "Komand",
      "tags": [
        "test",
        "komand"
      ],
      "createdAt": 1511314704388,
      "metrics": {},
      "id": "AV_hYElcYMfcbXhqb9v0",
      "customFields": {}
    },
    ...
  ]
}

```

#### Get User

This action is used to get user information.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|False|User ID. If empty, the current user is used|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_id|string|False|User _ID|
|_type|string|False|User type|
|createdAt|integer|False|Time the user was created at in milliseconds or epoch, e.g. 1496561862924|
|createdBy|string|False|Created by|
|hasKey|boolean|False|User has a key|
|id|string|False|ID|
|name|string|False|Name|
|preferences|object|False|User preferences|
|roles|[]string|False|Roles|
|status|string|False|Get user status|
|updatedAt|integer|False|Time the user was updated in milliseconds or epoch, e.g. 1496561862924|
|updatedBy|string|False|Updated by|
|user|string|False|User|

Example output:

```

{
  "id": "jschipp",
  "user": "user",
  "_id": "jschipp",
  "_type": "user",
  "createdAt": 1510027623902,
  "status": "Ok",
  "roles": [
    "read",
    "write",
    "admin",
    "alert"
  ],
  "updatedAt": 1511200144667,
  "updatedBy": "user",
  "hasKey": true,
  "createdBy": "user",
  "name": "Jon Schipp"
}

```

#### Get Case

This action is used to retrieve a case by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|case|case|True|Get case output|

Example output:

```

{
  "case": {
    "owner": "jschipp",
    "flag": true,
    "severity": 2,
    "tlp": 3,
    "createdBy": "jschipp",
    "customFields": {},
    "_type": "case",
    "user": "jschipp",
    "startDate": 1511199461000,
    "createdAt": 1511200164686,
    "title": "From TheHive4Py",
    "metrics": {},
    "tags": [
      "TheHive4Py",
      "sample"
    ],
    "description": "N/A",
    "id": "AV_ajI_oYMfcbXhqb9tS",
    "status": "Open",
    "caseId": 1
  }
}

```

#### Create Case

This action is used to create a new case.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|customFields|object|None|False|Case custom fields|None|
|description|string|None|False|Description of the case|None|
|flag|boolean|False|False|Flag, default is false|None|
|tags|[]string|None|False|List of tags|None|
|task|itask|None|False|Case task|None|
|title|string|None|True|Name of the case|None|
|tlp|integer|2|False|Traffic Light Protocol level, default is 2|None|

##### customFields

To assign `customFields` to a new case, pass in custom JSON to the input. The `object` contains the name of the customField that was created as its key, yielding a new `object`
that has the datatype of the field and a value you want assigned to the new custom field e.g.:

|Supported Data Types|Examples|
|--------------------|--------|
|string|{"testCustomField":{"string":"My custom field"}}|
|numbers|{"testCustomField":{"number":100}}|
|booleans|{"testCustomField":{"boolean":true}}|
|dates|{"testCustomField":{"date":1529696160000}}|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|case|case|False|Create case output|

Example output:

```

{
  "case": {
     "tags": [
       "test"
     ],
     "status": "Open",
     "_type": "case",
     "startDate": 1511303753000,
     "flag": false,
     "id": "AV_guTIIYMfcbXhqb9vg",
     "owner": "jschipp",
     "createdAt": 1511303754105,
     "user": "jschipp",
     "metrics": {},
     "title": "My Test Case",
     "caseId": 18,
     "customFields": {},
     "severity": 2,
     "description": "This is a test case",
     "tlp": 2,
     "createdBy": "jschipp"
  }
}

```

#### Close Case

This action is used to close a case by ID. It returns `Found` or `NotFound` in the `type` key and `Closed` or `NotClosed` in the `message` key if there's no errors.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|None|
|impact_status|string|None|False|Case impact status|['low', 'medium', 'high']|
|resolution_status|string|None|False|Case resolution status|['low', 'medium', 'high']|
|summary|string|None|False|Case Summary|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Closed case message|
|type|string|True|Closed case type|

Example output:

```

{
  "type": "Found",
  "message": "Closed"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.5 - New spec and help.md format for the Hub. Update help key features and fix description capitalisation
* 2.0.4 - Update to use the `komand/python-2-27-slim-plugin` Docker image to reduce plugin size and to support SSL Verify
* 2.0.3 - Fix issue where SSL Verify was not used in actions that utilize requests | Updated test method and moved it to connection
* 2.0.2 - Fix issue where SSL Verify was not used in the connection
* 2.0.1 - Update descriptions
* 2.0.0 - Update to new credential types
* 1.0.0 - Custom Field support added to Create Case action | Support web server mode
* 0.2.0 - Bug fix, add more input variables for Close Case action
* 0.1.2 - Bug fix for constant "waiting" in Status field | Updated to v2 architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [TheHive](https://thehive-project.org/)
* [thehive4py](https://github.com/CERT-BDF/TheHive4py)
* [TheHive API](https://github.com/CERT-BDF/TheHiveDocs/tree/master/api)

