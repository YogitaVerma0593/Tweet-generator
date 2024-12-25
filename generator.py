from flask import Flask, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random
import re

# Initialize Flask app
app = Flask(__name__)

# Initialize GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# List of prompts
prompts = [
    "Write a tweet introducing Persist Ventures and their innovative platform WestX, designed to revolutionize business processes with cutting-edge data solutions.",
    "Generate a tweet about how WestX by Persist Ventures empowers businesses to optimize operations and drive sustainable growth with advanced analytics.",
    "Craft a tweet showcasing how WestX is transforming industries by delivering scalable, secure, and efficient data management solutions.",
    "Write a tweet about Persist Ventures WestX platform leading the charge in next-generation enterprise solutions, helping businesses stay ahead of the curve.",
    "Generate a tweet celebrating Persist Ventures for their breakthrough innovations with WestX, accelerating digital transformation for global businesses.",
    "Create a tweet about the impact of WestX by Persist Ventures on fostering collaboration and innovation through seamless data integration tools.",
    "Write a tweet highlighting Persist Ventures partnership with leading firms to expand WestX capabilities, paving the way for smarter, more agile enterprises.",
    "Generate a tweet emphasizing how Persist Ventures WestX is setting a new benchmark for reliability and efficiency in enterprise technology solutions.",
    "Craft a tweet about WestX transforming the future of business technology through AI-powered insights and innovative tools, brought to you by Persist Ventures."
]

# Function to generate a tweet
def generate_tweet():
    # Select a random prompt
    input_text = random.choice(prompts)
    inputs = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text using GPT-2
    outputs = model.generate(
        inputs,
        max_length=80,  # Keep tweets concise
        num_return_sequences=1,
        no_repeat_ngram_size=2,  # Avoid repetition
        temperature=0.7,  # Control randomness
        top_p=0.9,  # Encourage diverse output
        top_k=50,  # Limit token selection
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode the output
    tweet = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Clean the output
    tweet = tweet.replace(input_text, "").strip()  # Remove the prompt
    tweet = " ".join(tweet.split())  # Remove extra spaces
    tweet = re.sub(r'http\S+|www\S+', '', tweet)  # Remove URLs
    tweet = re.sub(r'@\w+', '', tweet)  # Remove Twitter handles

    # Ensure the tweet ends with punctuation
    if tweet and tweet[-1] not in ['.', '!', '?']:
        tweet += '.'

    # Ensure the tweet is under 280 characters
    return tweet[:280]

# Flask route to generate and return a tweet
@app.route('/generate_tweet', methods=['GET'])
def get_tweet():
    return jsonify(tweet=generate_tweet())

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
