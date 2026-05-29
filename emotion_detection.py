import requests

def emotion_detector(text_to_analyze):
    '''
    Analyze the emotion of the given text using the Watson NLP API and return text attribute.
    '''
    # URL, headers and input kson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyze } }

	# Make a POST request to the API with the payload and headers
    response = requests.post(url, json=json, headers=header, timeout = 5)

    return response.text
