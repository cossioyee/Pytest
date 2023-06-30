import boto3

def invalidar_distribucion(id, referencia):
    cloudfront = boto3.client('cloudfront')    
    response = cloudfront.create_invalidation(
        DistributionId=id,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': ['/*']
            },
            'CallerReference': referencia
        }
    )

def main():
   id = 'E4UPIDHQUWNLX'
   referencia = 'invalidacion1'
   invalidar_distribucion(id,referencia)

if __name__ == '__main__':
   main()