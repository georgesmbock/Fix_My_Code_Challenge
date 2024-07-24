#!/usr/bin/python

from flask import Flask, jsonify

app_views = Blueprint('app_views', __name__)

@app_views.route('/statut', methods=['GET'])

def statut():
    return jsonify({'statut': 'ok'}), 200
