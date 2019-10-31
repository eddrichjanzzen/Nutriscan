import json
import boto3
import re
import base64

def lambda_handler(event, context):
    
    client = boto3.client('rekognition')
    lambda_client = boto3.client('lambda')
    dynamo_client = boto3.client('dynamodb')
    
    image = json.loads(event['body'])['image']
    
    decoded = base64.decodestring(image.encode('utf-8'))
    
    response = client.detect_text(Image={'Bytes':decoded})
                        
    textDetections = response['TextDetections']
    
    array = []
    for text in textDetections:
        
        if (text['Type'] == "LINE"):
            if text['Confidence']>=90.0:
                #print ('Detected text:' + text['DetectedText'])
                #print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                #print ('Id: {}'.format(text['Id']))
                #if 'ParentId' in text:
                   # print ('Parent Id: {}'.format(text['ParentId']))
                #print ('Type:' + text['Type'])
                array.append(text['DetectedText']) 
                
    output = []
    for item in array:
        
        a1 = re.split(r'[:.,()]', item)
        
        for x in a1:
            if len(x)>0:
                output.append(x.strip())
                
    output.pop(0)
    output.pop()
    
    table = boto3.resource('dynamodb').Table('impact_rating')
    
    result = []
    
    for ingredient in output:
        #request if it exists in dynamodb
    
        response = table.get_item(
	        Key={
		        "ingredient": ingredient.lower()
            }
        )
	    
        aggregated = {}
        aggregated['ingredient'] = ingredient
	    
        try:
            item = response['Item']
            aggregated['state'] = "1"
            
            try:
                aggregated['rating']=item['rating']
            
            except:
                pass
            
            try:
                aggregated['history'] = item['history']
                aggregated['state']="2"
                
            except:
                pass
                
            try:
                aggregated['description'] = item['description']
                
            except:
                pass
            
        except KeyError:
            aggregated['state'] = "0"
            
        result.append(aggregated)
    print(result)    
            
    '''
    string = ",".join(output)
    
    request = {
        "ingredients":string
    }
    
    
    invoke_response = lambda_client.invoke(FunctionName="impact_wikipedia_search",
                                           InvocationType='RequestResponse',
                                           Payload=json.dumps(request))
                                           
    invoke_response = invoke_response["Payload"].read().decode('utf-8')
    parsed_response = json.loads(invoke_response)
    '''
    
    
    return {
        'statusCode': 200,
        'headers':{
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps(result)
    }

