import boto3

# Connect to S3 service
s3 = boto3.client('s3')

# Upload a document to S3
s3.upload_file('invoice.pdf', 'your-bucket-name', 'invoices/invoice1.pdf')

# Generate a pre-signed URL for accessing the file
url = s3.generate_presigned_url('get_object',
                                Params={'Bucket': 'your-bucket-name', 'Key': 'invoices/invoice1.pdf'},
                                ExpiresIn=3600)

print("Access URL:", url)
