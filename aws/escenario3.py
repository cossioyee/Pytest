import boto3

def imprimirtabla(tabla):
   for item in tabla['Item']:
      value = tabla['Item'][item]
      print(f"{item}:{value}")

def consultar(tabla, correo):
   dynamodb = boto3.resource('dynamodb')
   table = dynamodb.Table(tabla)
   response = table.get_item(
      Key={'email':correo}
   )
   imprimirtabla(response)

def actualizar_por_correo(tabla, correo, newval):
   dynamodb = boto3.resource('dynamodb')
   table = dynamodb.Table(tabla)
   response = table.update_item(
       Key={'email':correo},
       UpdateExpression='SET surname = :valor',
       ExpressionAttributeValues={':valor': newval}
   )
   print(response)

def main():
   tabla="user"
   correo = "correo@dominio.com"
   newval="Lopez Perez"
   consultar(tabla, correo)
   actualizar_por_correo(tabla, correo, newval)
   consultar(tabla, correo)


if __name__ == '__main__':
   main()