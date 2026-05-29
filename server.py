'''Flask server for the Emotion Detector application.'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def run_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion_detector() function. 
    '''
    # Store the text to analyze from the html interface
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function over the text_to_analyze
    analyzed_text = emotion_detector(text_to_analyze)

    # Format the output as The given text has been identified as 'label' with a score of 'score'.
    anger =  analyzed_text['anger']
    disgust = analyzed_text['disgust']
    fear = analyzed_text['fear']
    joy = analyzed_text['joy']
    sadness = analyzed_text['sadness']

    dominant_emotion = analyzed_text['dominant_emotion']

    if dominant_emotion is None:
        return "Invaid text! Please try again!."

    response_formatted = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is <strong>{dominant_emotion}</strong>."
        )

    return response_formatted

@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000

    app.run(host="0.0.0.0", port=5000)
