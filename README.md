# surepass-python-task
---
## Documentation
> Created an API, using Flask Restex, around the function get pan data in file pan.py.
---
> Date of birth("dob" field) is serialized in JSON output in the format YYYY-MM-DD
---
> Used Flask-JWT to generate Tokens
## INPUT
```
{
  PAN Number : 'NXXXXXFK9'
}
```
## OUTPUT
```
{
  PAN Number: 'NXXXXXFK9',
  Name: "Dinesh Kumar",
  dob: "1990-10-25",
  father_name: "Hari Kumar",
  "client_id": "4feb601e-2316-4dda-8d91-28c89cdb2335-2316-4dda-8d91-28c89cdb2335-2316-4dda-8d91-28c89cdb2335-4dda-8d91-4dda-8d91-4feb601e-2316-4dda"
}
```
## How to use:
```
> python pan.py
> curl -i http://127.0.0.1:5000/NXXXXXFK9
```
