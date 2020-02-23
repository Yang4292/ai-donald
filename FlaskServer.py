from flask import Flask, request, render_template
import GenerateTweet

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/get-tweet', methods=['GET'])
def get_tweet():
    headline = request.args.get('headline')
    return GenerateTweet.get_tweet(headline)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)