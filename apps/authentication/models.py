# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None


class Projections(db.Model):

    __tablename__ = 'projections'

    id = db.Column(db.Integer, primary_key=True)
    source_plant = db.Column(db.String)
    destination_plant = db.Column(db.String)
    destination_location = db.Column(db.String)
    forty_ft = db.Column(db.Integer)
    twenty_ft = db.Column(db.Integer)
    destination_port = db.Column(db.String)
    
    def __init__(self, **kwargs):
        super(Projections, self).__init__(**kwargs)


class VesselMaster(db.Model):

    __tablename__ = 'vessel_master'

    id = db.Column(db.Integer, primary_key=True)
    port = db.Column(db.String)
    terminal = db.Column(db.String)
    vessel = db.Column(db.String)
    max_capacity = db.Column(db.Integer)
    allocation_percentage = db.Column(db.Integer)
    br_or_sl = db.Column(db.String)

    def __init__(self, **kwargs):
        super(VesselMaster, self).__init__(**kwargs)


class ShippingLineAllocation(db.Model):

    __tablename__ = 'shipping_line_allocation'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String)
    destination = db.Column(db.String)
    destnation_location = db.Column(db.String)
    twenty_feet = db.Column(db.Boolean)
    forty_feet = db.Column(db.Boolean)
    l1_carrier = db.Column(db.String)
    valid_from = db.Column(db.Date)
    valid_to = db.Column(db.Date)

    def __init__(self, **kwargs):
        super(ShippingLineAllocation, self).__init__(**kwargs)


class ContainerStock(db.Model):

    __tablename__ = 'containerstock'

    id = db.Column(db.Integer, primary_key=True)
    port = db.Column(db.String)
    terminals = db.Column(db.String)
    brg_or_sl = db.Column(db.String)
    container_type = db.Column(db.String)
    empty_stock = db.Column(db.Integer)
    safety_stock = db.Column(db.Integer)
    rejected = db.Column(db.Integer)
    
    def __init__(self, **kwargs):
        super(ContainerStock, self).__init__(**kwargs)


class VesselSchedule(db.Model):

    __tablename__ = 'vesselschedule'

    id = db.Column(db.Integer, primary_key=True)
    port = db.Column(db.String)
    terminal = db.Column(db.String)
    vessel = db.Column(db.String)
    voyage = db.Column(db.String)
    sailing_date = db.Column(db.Date)

    def __init__(self, **kwargs):
        super(VesselSchedule, self).__init__(**kwargs)