import boto3
from diccionario import jenkins

def imprimir_tabla(tabla):
   for item in tabla['Item']:
      value = tabla['Item'][item]
      print(f"{item}:{value}")

def consultar(tabla, correo):
   dynamodb = boto3.resource('dynamodb')
   table = dynamodb.Table(tabla)
   response = table.get_item(
      Key={
         'email':correo
      }
   )
   imprimir_tabla(response)

def actualizar_por_correo(tabla, correo, key, newval):
   dynamodb = boto3.resource('dynamodb')
   new_var = tabla
   table = dynamodb.Table(new_var)   
   response = table.update_item(
      Key={
          'email':correo
      },
      ExpressionAttributeValues={
         ':valor': newval
      },
      ExpressionAttributeNames={
        '#llave': key
      },
      UpdateExpression='SET #llave = :valor'   
   )

def main():
   for tabla, correos in jenkins.items():
      for correo, cambios in correos.items():
         for llave, valor in cambios.items():
            print(f"{tabla} {correo} {llave} {valor}")
            actualizar_por_correo(tabla, correo, llave, valor)
            consultar(tabla, correo)

if __name__ == '__main__':
   main()