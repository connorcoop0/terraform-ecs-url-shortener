from flask import Flask, render_template, request, jsonify, redirect
import hashlib, boto3
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Change this to send to dynamo DB
urlPair = ["", ""]

# Genereates shortened url keys
def gen_key(url): return hashlib.md5(url.encode()).hexdigest()[:6]

@app.route("/shorten", methods=["POST"])
def shorten():
    # Get longURL from webpage request
    long_url = request.get_json().get("url")

    # This should be prevented by the js but just in case
    if not long_url:
        return jsonify({"error": "Missing URL"}), 400
    
    # Generate a key
    key = gen_key(long_url)

    # Assign the key
    urlPair[0], urlPair[1] = key, long_url
    
    # return success code 200
    return jsonify({"short_url": f"{request.host_url}{key}"}), 200

@app.route("/<key>")
def go(key):
    if key == urlPair[0]:
        item = urlPair
        return redirect(item[1], 302)
    else: 
        return (jsonify({"error":"Not found"}),404)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
