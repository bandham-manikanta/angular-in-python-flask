from flask import jsonify, make_response, request, abort, render_template
#from app_main import db
from flask import current_app as app


@app.route('/', methods=['GET'])
def get_all_cdrs():
    return render_template('index.html')


def get_employees():
    employees = [{
        'id': 1,
        'fullName': 'mark jucker',
        'gender': 'MALE',
        'dob': '1-1-2021',
        'doj': '2-2-2022',
        'qualification': 'B.Tech',
        'pan': 'CDERED1233',
        'email': 'mark.zucker@facebook.com'
    }]
    return employees
