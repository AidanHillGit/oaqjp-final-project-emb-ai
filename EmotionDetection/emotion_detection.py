import requests
import json

# get user text, send to the emotion API then return the response
def emotion_detector(text_to_analyze):
    URL =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json = input_json, headers=header)
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }

    return formatted_response

def emotion_predictor(text_to_analyze):

    # if we do not have a value do not stop here and return text
    if all(value is None for value in detected_text.values()):
        return detected_text


    if detected_text['emotionPredictions'] is not None:
        emotions = detected_text['emotionPredictions'][0]['emotion']

        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']

        dominant_emotion = max(emotions, key=emotions.get)

        test_result = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

        return test_result