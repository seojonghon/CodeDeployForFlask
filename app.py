from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'seo - hello flask & code deploy V2  good test !!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
