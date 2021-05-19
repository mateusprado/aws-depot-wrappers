
# resources-by-tag

### Variables

Tags that will be exported from resources to csv file
```python
tags_to_export = ['Name']
```

Tags that will be used as filter and services and resources that will be used to generate csv file

```python
TagFilters=[
        {"Key": "Env"}
    ],
    ResourceTypeFilters=[
        "ec2:instance"
    ]
```

[List of complete Resource Types with name convention](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html)

### Output file format
```bash
resource,Tag: Name
arn:aws:ec2:us-east-1:AWSACCOUNT:instance/i-0e15fe4145c50e677,devlopment-instance
arn:aws:ec2:us-east-1:AWSACCOUNT:instance/i-0ee8c3c33f5c4ebb6,aws-cloud9-mprado-workspace-2e43625b2b2c4fb3bb4263387269e293
```