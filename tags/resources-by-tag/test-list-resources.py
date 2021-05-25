import boto3
import json
client = boto3.client('resource-groups')

query = {
    "ResourceTypeFilters":
    [
        "AWS::AllSupported"
    ],
    "TagFilters":
    [
        {
            "Key": "Env"
        }
    ]
}

response = client.search_resources(
    ResourceQuery={
        'Type': 'TAG_FILTERS_1_0',
        'Query': json.dumps(query)
    }
)
print(len(response['ResourceIdentifiers']))
print(response['ResourceIdentifiers'])