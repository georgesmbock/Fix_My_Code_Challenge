#!/usr/bin/python

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/statut', methods=['GET'])

def statut():
    return jsonify({'statut': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True)
