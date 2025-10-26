import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response text into a Python dictionary
        response_dict = json.loads(response.text)
        emotion_scores = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
        return emotion_scores
    else:
        # Return None or an error message if the request failed
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

if __name__ == '__main__':
    print(emotion_detector("I love this new technology."))