import requests
import json
import sys, os
import datetime

# print(datetime.datetime.now())
date=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
# print(date)

url='https://sandbox.api.visa.com/visadirect/fundstransfer/v1/pullfundstransactions'

# cert='/home/avibomb/Desktop/Hello/cert.perm'



cert=os.path.abspath("Visa_cert.pem")
# key='key_test.pem'


key=os.path.abspath("Visa_key.pem")

headers={"Accept": "application/json"}

user_id='M86X7RZ20QN7GKO7D2XZ21TuC1aCB63azYVa9tY8ehpDs96Eg'
password='fgoHAN3L959zDw5q2hGA7'

body={}

timeout=10

payload=json.loads(''' 
{
"acquirerCountryCode": "840",
"acquiringBin": "408999",
"amount": "124.02",
"businessApplicationId": "AA",
"cardAcceptor": {
"address": {
"country": "USA",
"county": "081",
"state": "CA",
"zipCode": "94404"
},
"idCode": "ABCD1234ABCD123",
"name": "Visa Inc. USA-Foster City",
"terminalId": "ABCD1234"
},
"cavv": "0700100038238906000013405823891061668252",
"foreignExchangeFeeTransaction": "11.99",
"localTransactionDateTime": "'''+date+'''",
"retrievalReferenceNumber": "330000550000",
"senderCardExpiryDate": "2015-10",
"senderCurrencyCode": "USD",
"senderPrimaryAccountNumber": "4895142232120006",
"surcharge": "11.99",
"systemsTraceAuditNumber": "451001",
"nationalReimbursementFee": "11.22",
"cpsAuthorizationCharacteristicsIndicator": "Y",
"addressVerificationData": {
"street": "XYZ St",
"postalCode": "12345"
},
"settlementServiceIndicator": "9",
"colombiaNationalServiceData": {
"countryCodeNationalService": "170",
"nationalReimbursementFee": "20.00",
"nationalNetMiscAmountType": "A",
"nationalNetReimbursementFeeBaseAmount": "20.00",
"nationalNetMiscAmount": "10.00",
"addValueTaxReturn": "10.00",
"taxAmountConsumption": "10.00",
"addValueTaxAmount": "10.00",
"costTransactionIndicator": "0",
"emvTransactionIndicator": "1",
"nationalChargebackReason": "11"
},
"riskAssessmentData": {
"delegatedAuthenticationIndicator": true,
"lowValueExemptionIndicator": true,
"traExemptionIndicator": true,
"trustedMerchantExemptionIndicator": true,
"scpExemptionIndicator": true
},
"visaMerchantIdentifier": "73625198"
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


url='https://sandbox.api.visa.com/visadirect/fundstransfer/v1/pushfundstransactions'

payload=json.loads('''
{
"acquirerCountryCode": "840",
"acquiringBin": "408999",
"amount": "124.05",
"businessApplicationId": "AA",
"cardAcceptor": {
"address": {
"country": "USA",
"county": "San Mateo",
"state": "CA",
"zipCode": "94404"
},
"idCode": "CA-IDCode-77765",
"name": "Visa Inc. USA-Foster City",
"terminalId": "TID-9999"
},
"localTransactionDateTime": "'''+date+'''",
"merchantCategoryCode": "6012",
"pointOfServiceData": {
"motoECIIndicator": "0",
"panEntryMode": "90",
"posConditionCode": "00"
},
"recipientName": "rohan",
"recipientPrimaryAccountNumber": "4957030420210496",
"retrievalReferenceNumber": "412770451018",
"senderAccountNumber": "4653459515756154",
"senderAddress": "901 Metro Center Blvd",
"senderCity": "Foster City",
"senderCountryCode": "124",
"senderName": "Mohammed Qasim",
"senderReference": "",
"senderStateCode": "CA",
"sourceOfFundsCode": "05",
"systemsTraceAuditNumber": "451018",
"transactionCurrencyCode": "USD",
"transactionIdentifier": "381228649430015",
"settlementServiceIndicator": "9",
"colombiaNationalServiceData": {
"countryCodeNationalService": "170",
"nationalReimbursementFee": "20.00",
"nationalNetMiscAmountType": "A",
"nationalNetReimbursementFeeBaseAmount": "20.00",
"nationalNetMiscAmount": "10.00",
"addValueTaxReturn": "10.00",
"taxAmountConsumption": "10.00",
"addValueTaxAmount": "10.00",
"costTransactionIndicator": "0",
"emvTransactionIndicator": "1",
"nationalChargebackReason": "11"
}
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


url='https://sandbox.api.visa.com/visadirect/fundstransfer/v1/reversefundstransactions'

payload=json.loads('''
 
{
"acquirerCountryCode": "608",
"acquiringBin": "408999",
"businessApplicationId": "AA",
"amount": "24.01",
"cardAcceptor": {
"address": {
"country": "USA",
"county": "San Mateo",
"state": "CA",
"zipCode": "94404"
},
"idCode": "VMT200911026070",
"name": "Visa Inc. USA-Foster City",
"terminalId": "365539"
},
"localTransactionDateTime": "'''+date+'''",
"originalDataElements": {
"acquiringBin": "408999",
"approvalCode": "20304B",
"systemsTraceAuditNumber": "897825",
"transmissionDateTime": "2020-07-01T13:00:35"
},
"pointOfServiceCapability": {
"posTerminalEntryCapability": "2",
"posTerminalType": "4"
},
"pointOfServiceData": {
"motoECIIndicator": "0",
"panEntryMode": "90",
"posConditionCode": "00"
},
"retrievalReferenceNumber": "330000550000",
"senderCardExpiryDate": "2015-10",
"senderCurrencyCode": "USD",
"senderPrimaryAccountNumber": "4895100000055127",
"systemsTraceAuditNumber": "451050",
"transactionIdentifier": "381228649430011",
"settlementServiceIndicator": "9",
"colombiaNationalServiceData": {
"countryCodeNationalService": "170",
"nationalReimbursementFee": "20.00",
"nationalNetMiscAmountType": "A",
"nationalNetReimbursementFeeBaseAmount": "20.00",
"nationalNetMiscAmount": "10.00",
"addValueTaxReturn": "10.00",
"taxAmountConsumption": "10.00",
"addValueTaxAmount": "10.00",
"costTransactionIndicator": "0",
"emvTransactionIndicator": "1",
"nationalChargebackReason": "11"
}
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
