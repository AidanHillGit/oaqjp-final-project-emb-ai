"""
Emotion Detection Server File

The server takes in the users input text, processes the text, and returns a list of
emotions and rating for each. Then what emotion has the highest level between 0.0-1.0,
1.0 being the highest possible value.
"""

from flask import Flask, render_template, request, jsonify

# import in the functions that are needed
from EmotionDetection.emotion_detection import emotion_detector

# create the app variable for server
app = Flask(__name__)

def run_emotion_detection():
    """
    The main function for running Emotion Detection application
    """
    app.run(host="0.0.0.0", port=5000)

# /emotionDetector decorator
@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the text from the user for the emotions and return the results from analysis
    """
    text_to_detect = request.args.get('textToAnalyze')

    if not text_to_detect or text_to_detect.strip() == "":
        return "Invalid text! Please try again.", 400

    formatted_response = emotion_detector(text_to_detect)

    return (
        "For the given statement, the system response is "
        f"'anger': {formatted_response['anger']}, "
        f"'disgust': {formatted_response['disgust']}, "
        f"'fear': {formatted_response['fear']}, "
        f"'joy': {formatted_response['joy']} and "
        f"'sadness': {formatted_response['sadness']}. "
        f"The dominant emotion is {formatted_response['dominant_emotion']}."
    )

# main route for web app
@app.route("/")
def render_index_page():
    """
    This function creates rendering of the main application for over the Flask channel
    """
    return render_template('index.html')

@app.errorhandler(500)
def internal_server_error(_):
    """Handles internal server errors"""
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == "__main__":
    run_emotion_detection()
