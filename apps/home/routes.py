# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
import pandas as pd
from apps.authentication.models import Projections, VesselMaster, VesselSchedule, ShippingLineAllocation, ContainerStock
from apps import db
import numpy


@blueprint.route('/index')
@login_required
def index():
    return render_template('pages/map.html', segment='index')

@blueprint.route('/data')
@login_required
def data():
    return render_template('pages/index.html', segment='index')

@blueprint.route('/typography')
@login_required
def typography():
    return render_template('pages/typography.html')

@blueprint.route('/color')
@login_required
def color():
    return render_template('pages/color.html')


@blueprint.route('/port')
@login_required
def port():
    return render_template('pages/output.html')


@blueprint.route('/container')
@login_required
def container():
    return render_template('pages/container.html')


@blueprint.route('/upload')
def upload_data():
    df = pd.read_excel('data.xlsx', sheet_name=None)
    # print(df)
    for key, value in df.items():
        print(key)
        if key == "projection":
            # print(value)
            columns = list(value.columns)
            print(columns)
            for ind in value.index:
                tmp = {}
                for item in columns:
                    if item == 'source_plant' or item == 'destination_plant':
                        tmp[item] = str(value[item][ind])
                    elif item == 'forty_ft' or item == 'twenty_ft':
                        tmp[item] = int(value[item][ind])
                    else:
                        tmp[item] = value[item][ind]
                db.session.add((Projections(**tmp)))
            db.session.commit()
        if key == "vessel_master":
            # print(value)
            new_value  = value.fillna(0)
            print(new_value)
            columns = list(value.columns)
            print(columns)
            for ind in new_value.index:
                tmp = {}
                for item in columns:
                    if item == 'max_capacity' or item == 'allocation_percentage':
                        tmp[item] = int(new_value[item][ind])
                    else:
                        tmp[item] = new_value[item][ind]
                db.session.add((VesselMaster(**tmp)))
            db.session.commit()
        if key == "vessel_schedule":
        # print(value)
            # new_value  = value.fillna(0)
            columns = list(value.columns)
            print(columns)
            for ind in value.index:
                tmp = {}
                for item in columns:
                #     if item == 'max_capacity' or item == 'allocation_percentage':
                #         tmp[item] = int(new_value[item][ind])
                #     else:
                    tmp[item] = value[item][ind]
                db.session.add((VesselSchedule(**tmp)))
            db.session.commit()

        if key == "shipping_line_allocation":
        # print(value)
            new_value  = value.fillna(0)
            columns = list(value.columns)
            print(columns)
            for ind in new_value.index:
                tmp = {}
                for item in columns:
                    if item == 'source' or item == 'destination':
                        tmp[item] = str(new_value[item][ind])
                    elif item == 'twenty_feet' or item == 'forty_feet':
                        if new_value[item][ind] == 'X':
                            tmp[item] = True
                        else:
                            tmp[item] = False
                    else:
                        tmp[item] = new_value[item][ind]
                db.session.add((ShippingLineAllocation(**tmp)))
            db.session.commit()
        if key == "containerstock":
        # print(value)
            # new_value  = value.fillna(0)
            columns = list(value.columns)
            print(columns)
            for ind in value.index:
                tmp = {}
                for item in columns:
                    if item == 'empty_stock' or item == 'safety_stock' or item == 'rejected':
                        tmp[item] = int(value[item][ind])
                    else:
                        tmp[item] = value[item][ind]
                db.session.add((ContainerStock(**tmp)))
            db.session.commit()
    return jsonify({'result': True})


@blueprint.route('/icon-tabler')
@login_required
def icon_tabler():
    return render_template('pages/icon-tabler.html')


@blueprint.route('/vesselmaster')
@login_required
def vesselmaster():
    projection_data = VesselMaster.query.all()
    final_projection = []
    for data in projection_data:
        tmp = {}
        tmp['port'] = data.port
        tmp['terminal'] = data.terminal
        tmp['vessel'] = data.vessel
        tmp['max_capacity'] = data.max_capacity
        tmp['allocation_percentage'] = data.allocation_percentage
        tmp['br_or_sl'] = data.br_or_sl
        final_projection.append(tmp)
    header = [
    { 'field': "port" },
    { 'field': "terminal" },
    { 'field': "vessel" },
    { 'field': "max_capacity" },
    { 'field': "allocation_percentage" },
    { 'field': "br_or_sl" }
  ]
    
    print(final_projection)
    return render_template('pages/sample-page.html', projection=final_projection, header=header) 


@blueprint.route('/containerstock')
@login_required
def containerstock():
    projection_data = ContainerStock.query.all()
    final_projection = []
    for data in projection_data:
        tmp = {}
        tmp['port'] = data.port
        tmp['terminals'] = data.terminals
        tmp['brg_or_sl'] = data.brg_or_sl
        tmp['container_type'] = data.container_type
        tmp['empty_stock'] = data.empty_stock
        tmp['safety_stock'] = data.safety_stock
        tmp['rejected'] = data.rejected
        final_projection.append(tmp)
    header = [
    { 'field': "port" },
    { 'field': "terminals" },
    { 'field': "brg_or_sl" },
    { 'field': "container_type" },
    { 'field': "empty_stock" },
    { 'field': "safety_stock" },
    { 'field': "rejected" }
  ]
    
    print(final_projection)
    return render_template('pages/sample-page.html', projection=final_projection, header=header) 
    
@blueprint.route('/shippingline')
@login_required
def shippingline():
    projection_data = ShippingLineAllocation.query.all()
    final_projection = []
    for data in projection_data:
        tmp = {}
        tmp['source'] = data.source
        tmp['destination'] = data.destination
        tmp['destnation_location'] = data.destnation_location
        tmp['twenty_feet'] = data.twenty_feet
        tmp['forty_feet'] = data.forty_feet
        tmp['l1_carrier'] = data.l1_carrier
        tmp['valid_from'] = data.valid_from
        tmp['valid_to'] = data.valid_to
        final_projection.append(tmp)
    header = [
    { 'field': "source" },
    { 'field': "destination" },
    { 'field': "destnation_location" },
    { 'field': "twenty_feet" },
    { 'field': "forty_feet" },
    { 'field': "l1_carrier" },
    { 'field': "valid_from" },
    { 'field': "valid_to" }
  ]
    
    print(final_projection)
    return render_template('pages/sample-page.html', projection=final_projection, header=header) 
    

@blueprint.route('/schedule')
@login_required
def schedule():
    projection_data = VesselSchedule.query.all()
    final_projection = []
    for data in projection_data:
        tmp = {}
        tmp['port'] = data.port
        tmp['terminal'] = data.terminal
        tmp['vessel'] = data.vessel
        tmp['voyage'] = data.voyage
        tmp['sailing_date'] = data.sailing_date
        final_projection.append(tmp)
    header = [
    { 'field': "port" },
    { 'field': "terminal" },
    { 'field': "vessel" },
    { 'field': "voyage" },
    { 'field': "sailing_date" }
  ]
    
    print(final_projection)
    return render_template('pages/sample-page.html', projection=final_projection, header=header)


@blueprint.route('/sample-page')
@login_required
def sample_page():
    projection_data = Projections.query.all()
    final_projection = []
    for data in projection_data:
        tmp = {}
        tmp['source_plant'] = data.source_plant
        tmp['destination_plant'] = data.destination_plant
        tmp['destination_location'] = data.destination_location
        tmp['40_Feet'] = data.forty_ft
        tmp['20_Feet'] = data.twenty_ft
        tmp['destination_port'] = data.destination_port
        final_projection.append(tmp)

    print(final_projection)
    header = [
    { 'field': "source_plant" },
    { 'field': "destination_plant" },
    { 'field': "destination_location" },
    { 'field': "40_Feet" },
    { 'field': "20_Feet" },
    { 'field': "destination_port" }
  ]
    
    return render_template('pages/sample-page.html', projection=final_projection, header=header)  

@blueprint.route('/accounts/password-reset/')
def password_reset():
    return render_template('accounts/password_reset.html')

@blueprint.route('/accounts/password-reset-done/')
def password_reset_done():
    return render_template('accounts/password_reset_done.html')

@blueprint.route('/accounts/password-reset-confirm/')
def password_reset_confirm():
    return render_template('accounts/password_reset_confirm.html')

@blueprint.route('/accounts/password-reset-complete/')
def password_reset_complete():
    return render_template('accounts/password_reset_complete.html')

@blueprint.route('/accounts/password-change/')
def password_change():
    return render_template('accounts/password_change.html')

@blueprint.route('/accounts/password-change-done/')
def password_change_done():
    return render_template('accounts/password_change_done.html')

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
