import tweepy
from flask import Flask,render_template,request
app=Flask(__name__)

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

@app.route('/test')
def test():
    return render_template('index.html')
@app.route('/twitter',methods=['POST'])
def main():
  # Fill in the values that you get from the twitter api
  cfg = {
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : ""
    }

  api = get_api(cfg)
  tweet = request.form['message']
  status = api.update_status(status=tweet)
  return "the message has been sent"
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
    app.run(debug=True)