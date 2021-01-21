from flask import Flask, render_template, jsonify, request, make_response
import json
import jsons

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pocztapolska')
@app.route('/pocztapolska/')
def poczta_polska():
    resp = make_response("PocztaPolska")
    resp.set_cookie("PHPSESSID", "EawU66qiWz2lNIRzF9qQ==", path="/pocztapolska")
    return resp

@app.route('/pocztapolska/wssClient.php', methods = ['POST'])
def wss_client():
    if request.form.get('n') == "003123123123123543231234" and request.form.get('s') == "EawU66qiWz2lNIRzF9qQ==":
        return render_template('poczta.html')
    else:
        return "Null"

@app.route('/inpost/<package_number>')
def inpost(package_number):
    if package_number == "612345678901234567890123":
        return jsonify(jsons.get_inpost_json())
    else:
        return jsonify(None)  