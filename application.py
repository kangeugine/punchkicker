'''
Flaks application for punchkicker
'''

import json
from datetime import datetime

from flask import Flask, render_template, request
from flask import jsonify, session, redirect, url_for
from sqlalchemy import func

from application import db
from application.models import Fighter, Fight, Frame, Annotation
from application.forms import EnterDBInfo, RetrieveDBInfo
from application.util import get_time
from application.constant import OBJECTS_TO_FIND, LABELS

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug = True
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'

# Global Variables
TEST = True
CONFIG = "A1"
USER_ID = "admin"

@application.route('/', methods=['GET'])
@application.route('/index', methods=['GET'])
def index():
    ip        = request.environ.get('HTTP_X_REAL_IP', 
                                    request.remote_addr)
    frame     = Frame.query.order_by(func.rand()).limit(1)
    image_url = frame[0].source_url
    frame_id  = frame[0].frame_id
    fight_id  = frame[0].fight_id
    session['fight_id']   = fight_id
    session['frame_id']   = frame_id
    session['ip']         = ip
    session['start_time'] = get_time()
    print image_url
    return render_template('box-annotation.html',
                           image_url=image_url,
                           objects_to_find=OBJECTS_TO_FIND,
                           labels=LABELS)

@application.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        jsonData   = request.get_json()
        annotation = jsonData['annotation']
        user_id    = jsonData['user_id']
        offset     = jsonData['offset']
        anno_str   = json.dumps(annotation)
        ip         = session.get('ip', None)
        frame_id   = session.get('frame_id', None)
        fight_id   = session.get('fight_id', None)
        start_time = session.get('start_time', None)
        end_time   = get_time()
        if TEST:
            print user_id
            print "annotation is '{}'".format(annotation)
            print "timezone offset is '{}'".format(offset)
        data_entered = Annotation(ip=ip,
                                  user_id=user_id,
                                  fight_id=fight_id,
                                  frame_id=frame_id,
                                  annotation=anno_str,
                                  is_test=TEST,
                                  start_time=start_time,
                                  end_time=end_time,
                                  timezone_offset=offset,
                                  config=CONFIG)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return json.dumps(({'success': True}, 200, 
               {'ContentType': 'application/json'}))

if __name__ == '__main__':
    application.run(host='0.0.0.0')
