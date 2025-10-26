''' Executing this function initiates the application of Emotion Detector
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the text provided by the user via URL query parameter,
    formats the response, and handles invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    dominant_emotion = response.pop('dominant_emotion')
    output_string = ", ".join([f"'{key}': {value}" for key, value in response.items()])

    return (
        f"For the given statement, the system response is {output_string}. "
        f"The dominant emotion is **{dominant_emotion}**."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main HTML page for the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    