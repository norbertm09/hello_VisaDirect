import requests
import json
import sys, os
import datetime
cert_content = os.getenv("VISA_CERT_PEM")
cert_content = os.getenv("VISA_KEY_PEM")
# print(datetime.datetime.now())
date=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
# print(date)

url='https://sandbox.api.visa.com/visaaliasdirectory/v1/manage/createalias'

# cert='/home/avibomb/Desktop/Hello/cert.perm'
cert=os.path.abspath("visa_cert.pem")
# key='key_test.pem'
key=os.path.abspath("Visa_key.pem")

headers={"Accept": "application/json"}

user_id='M86X7RZ20QN7GKO7D2XZ21TuC1aCB63azYVa9tY8ehpDs96Eg'
password='fgoHAN3L959zDw5q2hGA7'

body={}

timeout=10

payload=json.loads('''
{
"guid": "574f4b6a4c2b70472f306f300099515a789092348832455975343637a4d3170",
"recipientFirstName": "Jamie",
"recipientMiddleName": "M",
"recipientLastName": "Bakari",
"address1": "Street 1",
"address2": "Region 1",
"city": "Nairobi",
"country": "KE",
"postalCode": "00111",
"consentDateTime": "2018-03-01 01:02:03",
"recipientPrimaryAccountNumber": "4895140000066666",
"issuerName": "Test Bank 1",
"cardType": "Visa Classic",
"alias": "254711333888",
"aliasType": "01"
}
''')

r = requests.post(url,
                #   verify = ('put the CA certificate pem file path here'),
				  cert = (cert,key),
				  headers = headers,
				  auth = (user_id, password),
				#   data = body
                  json=payload,
                  timeout=timeout
                )

print(r.text)


url='https://sandbox.api.visa.com/visaaliasdirectory/v1/resolve'

payload=json.loads('''
{
"alias": "254711001987",
"businessApplicationId": "PP"
}
''')

r = requests.post(url,
                #   verify = ('put the CA certificate pem file path here'),
				  cert = (cert,key),
				  headers = headers,
				  auth = (user_id, password),
				#   data = body
                  json=payload,
                  timeout=timeout
                )

print(r.text)

url='https://sandbox.api.visa.com/visaaliasdirectory/v1/managemerchant/createalias'

payload=json.loads('''
{
"aliasId": "888000",
"merchantId": "4761100090708271",
"merchantCategoryCode": "6012",
"payloadFormatIndicator": "01",
"pointOfInitiationMethod": "11",
"transactionCurrencyCode": "404",
"recipientName": "Bob's Ice Cream",
"city": "Nairobi",
"country": "KE"
}
''')

r = requests.post(url,
                #   verify = ('put the CA certificate pem file path here'),
				  cert = (cert,key),
				  headers = headers,
				  auth = (user_id, password),
				#   data = body
                  json=payload,
                  timeout=timeout
                )

print(r.text)
