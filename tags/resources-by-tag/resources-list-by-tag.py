import boto3
import csv

client = boto3.client('resourcegroupstaggingapi')

tags_to_export = ['Env']
resource_filter = []

print('Starting request to TaggingAPI...')
response = client.get_resources(
    ResourceTypeFilters=resource_filter
)

resources_export = []
resources = response['ResourceTagMappingList']
header = ['resource']
tags_discovered = []
has_token = True

if response['PaginationToken']:
    while has_token:
        response = client.get_resources(
            PaginationToken=response['PaginationToken'],
            ResourceTypeFilters=resource_filter
        )

        for r in response['ResourceTagMappingList']:
            resources.append(r)

        if not response['PaginationToken']:
            has_token = False


for r in resources:
    resource = {}
    
    resource['resource'] = r['ResourceARN']

    resources_export.append(resource)
    for t in r['Tags']:
        if t['Key'] not in tags_discovered:
            tags_discovered.append(t['Key'])
        for te in tags_to_export:
            if te == t['Key']:
                resource[f"Tag: {t['Key']}"] = t['Value']
                if f"Tag: {t['Key']}" not in header:
                    header.append(f"Tag: {t['Key']}")
        
print(f"Other tags that have been discovered: {tags_discovered}")
print(f"Exporting resources found to csv file with Tags: {tags_to_export}")
for r in resources_export:
    with open('output.csv', 'w') as f:
        w = csv.DictWriter(f,header)
        w.writeheader()
        w.writerows(resources_export)
        f.close()

print('File output generated successfully.')
