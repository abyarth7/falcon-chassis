import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# # Upload a new file
# data = open('test.jpg', 'rb')
# s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)


def push_invoices_to_bucket():

    print("push to invoice hit")
    # # Upload a new file
    data = open(
        '/Users/abyarth/Desktop/cat.jpg', 'rb')
    s3.Bucket(
        'pe-neon-public').put_object(Key='diagnostics/staging/test/cat.jpg', Body=data)
    get_invoices_from_bucket()


def get_invoices_from_bucket():
    Key = 'diagnostics/staging/test/cat.jpg'
    try:
        download_file = s3.Bucket(
            'pe-neon-public').download_file(Key, 'cat.jpg')
        print("file downloaded : ", download_file)
        return download_file
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
        return False
