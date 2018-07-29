from application import db
from sqlalchemy import func

class Fighter(db.Model):
    __tablename__ = 'fighter'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), index=True, unique=False)
    last_name = db.Column(db.String(128), index=True, unique=False)
    nickname = db.Column(db.String(128), index=True, unique=False)
    time_created = db.Column(db.DateTime(timezone=True),
                             server_default=func.now(),
                             onupdate=func.current_timestamp())

    def __init__(self, first_name, last_name, nickname):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname

    def __repr__(self):
        line = '<Fighter(first_name=%r, last_name=%r, nickname=%r)>'
        return line % (self.first_name,
                       self.last_name,
                       self.nickname)

class Fight(db.Model):
    __tablename__ = 'fight'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(128), index=True, unique=False)
    red_fighter_id = db.Column(db.Integer, index=True, unique=False)
    blue_fighter_id = db.Column(db.Integer, index=True, unique=False)
    finish_round = db.Column(db.Integer, index=True, unique=False)
    finish_time = db.Column(db.String(128), index=True, unique=False)
    allowed_round = db.Column(db.Integer, index=True, unique=False)
    time_created = db.Column(db.DateTime(timezone=True),
                             server_default=func.now(),
                             onupdate=func.current_timestamp())

    def __init__(self, date, red_fighter_id, blue_fighter_id, finish_round, finish_time, allowed_round):
        self.date = date
        self.red_fighter_id = red_fighter_id
        self.blue_fighter_id = blue_fighter_id
        self.finish_round = finish_round
        self.finish_time = finish_time
        self.allowed_round = allowed_round

    def __repr__(self):
        line = ('<Fight(date=%r, red_fighter_id=%r, blue_fighter_id=%r,' 
                'finish_round=%r, finish_time=%r, allowed_round=%r)>')
        return line % (self.date,
                       self.red_fighter_id,
                       self.blue_fighter_id,
                       self.finish_round,
                       self.finish_time,
                       self.allowed_round)

class Frame(db.Model):
    __tablename__ = "frame"
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, index=True, unique=False)
    round = db.Column(db.Integer, index=True, unique=False)
    order = db.Column(db.Integer, index=True, unique=False)
    frame_id = db.Column(db.String(128), index=True, unique=True)
    source_url = db.Column(db.String(256), index=True, unique=False)
    time_created = db.Column(db.DateTime(timezone=True),
                             server_default=func.now(),
                             onupdate=func.current_timestamp())

    def __init__(self, fight_id, round, order, source_url):
        self.fight_id = fight_id
        self.round = round
        self.order = order
        frame_id = "-".join([str(fight_id), str(round), str(order)])
        self.frame_id = frame_id
        self.source_url = source_url

    def __repr__(self):
        line = '<Frame(fight_id=%r, round=%r, order=%r, frame_id=%r, source_url=%r)>'
        return line % (self.fight_id,
                       self.round,
                       self.order,
                       self.frame_id,
                       self.source_url)

class Gif(db.Model):
    __tablename__ = "gif"
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, index=True, unique=False)
    round = db.Column(db.Integer, index=True, unique=False)
    start_second = db.Column(db.Integer, index=True, unique=False)
    gif_id = db.Column(db.String(128), index=True, unique=True)
    source_url = db.Column(db.String(256), index=True, unique=False)
    time_created = db.Column(db.DateTime(timezone=True),
                             server_default=func.now(),
                             onupdate=func.current_timestamp())

    def __init__(self, fight_id, round, start_second, source_url):
        self.fight_id = fight_id
        self.round = round
        self.start_second = start_second
        gif_id = "-".join([str(fight_id), str(round), str(start_second)])
        self.gif_id = gif_id
        self.source_url = source_url

    def __repr__(self):
        line = '<Gif(fight_id=%r, round=%r, start_second=%r, gif_id=%r, source_url=%r)>'
        return line % (self.fight_id,
                       self.round,
                       self.start_second,
                       self.gif_id,
                       self.source_url)

class Annotation(db.Model):
    __tablename__ = "annotation"
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(128), index=True, unique=False)
    user_id = db.Column(db.String(128), index=True, unique=False)
    fight_id = db.Column(db.Integer, index=True, unique=False)
    frame_id = db.Column(db.String(128), index=True, unique=False)
    annotation = db.Column(db.String(2048), index=True, unique=False)
    is_test = db.Column(db.Boolean, index=True, unique=False)
    start_time = db.Column(db.String(128), index=True, unique=False)
    end_time = db.Column(db.String(128), index=True, unique=False)
    timezone_offset = db.Column(db.Integer, index=True, unique=False)
    config = db.Column(db.String(128), index=True, unique=False)
    time_created = db.Column(db.DateTime(timezone=True),
                             server_default=func.now(),
                             onupdate=func.current_timestamp())

    def __init__(self, ip, user_id, fight_id, 
                 frame_id, annotation, is_test,
                 start_time, end_time, timezone_offset,
                 config):
        self.ip = ip
        self.user_id = user_id
        self.fight_id = fight_id
        self.frame_id = frame_id
        self.annotation = annotation
        self.is_test = is_test
        self.start_time = start_time
        self.end_time = end_time
        self.timezone_offset = timezone_offset
        self.config = config

    def __repr__(self):
        line = ('<Annotation(ip=%r, user_id=%r,'
               + ' fight_id=%r, frame_id=%r,'
               + ' annotation=%r, is_test=%r,'
               + ' start_time=%r, end_time=%r,'
               + ' timezone_offset=%r, config=%r)>')
        return line % (self.ip, self.user_id,
                       self.fight_id, self.frame_id,
                       self.annotation, self.is_test,
                       self.start_time, self.end_time,
                       self.timezone_offset, self.config)
