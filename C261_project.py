import requests
equation=input("Enter the equation")
result= 'https://newton.now.sh/api/v2//simplify/'+equation
data=requests.get(result).json()
print("operation for the given operation",data['operation'])
print("expression for the given operation",data['expression'])
print("result for the given operation",data['result'])