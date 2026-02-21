from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Hello from AWS Elastic Beanstalk 🚀"

@application.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    application.run()
