import requests
import json

# get user text, send to the emotion API then return the response
def emotion_detector(text_to_analyze):
    """
    Sends user text to the Watson Emotion Detection API and returns
    emotion scores plus the dominant emotion.
    """

    # Watson NLP API endpoint
    URL =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Header tells the Watson which emotion detection model to use
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # JSON payload sent to the API, the API expects the users text inside raw_document
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Send POST request to Watson API
    response = requests.post(URL, json = input_json, headers=header)

    # Converts the JSON response into a Python dictionary
    formatted_response = json.loads(response.text)
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    dominant_emotion = max(emotions, key=emotions.get)

    # if the API returns a bad request, return empty values
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    # Send to the emotion_predictor, extract emotion values and dominant emotion
    return emotion_predictor(formatted_response)

def emotion_predictor(detected_text):

    # if we do not have a value do not stop here and return text
    if all(value is None for value in detected_text.values()):
        return detected_text

    # emotionPredictions contains the emotion analysis results
    if detected_text['emotionPredictions'] is not None:
        # access the emotion score dictionary
        emotions = detected_text['emotionPredictions'][0]['emotion']

        # Store the scores for each emotion
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']

        # Find the emotion with the highest score
        dominant_emotion = max(emotions, key=emotions.get)

        # create a dictionary with the final results
        test_result = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

        # return the processed results
        return test_result
