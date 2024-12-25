# we are creating an automatic tweet generation tool that generates
#  and post it to the web page(index.html) where on each refresh , a new tweet is generated
# and posted
import os
from flask import Flask, render_template, jsonify
from model.generator import generate_tweet  

# Create the Flask app
app = Flask(__name__)

# Store generated tweets in a list
generated_tweets = []

@app.route('/')
def index():
    tweet = generate_tweet()  # Generate a new tweet
    generated_tweets.append(tweet)  # Add the tweet to the list
    return render_template('index.html', tweets=generated_tweets)

@app.route('/generate_tweet')
def generate():
    tweet = generate_tweet()  # Generate a tweet without appending it to the list
    return jsonify(tweet=tweet)

if __name__ == "__main__":
    app.run(debug=True)
