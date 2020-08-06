from flask import jsonify, make_response, request, abort, render_template
#from app_main import db
from flask import current_app as app


@app.route('/', methods=['GET'])
def get_all_cdrs():
    return render_template('index.html')
