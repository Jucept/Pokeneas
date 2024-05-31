from flask import Blueprint, jsonify, render_template, current_app as app
from .pokeneas import POKENEAS
import random
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/json')
def get_pokenea_json():
    pokenea = random.choice(POKENEAS)
    container_id = os.uname().nodename
    return jsonify({
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'container_id': container_id
    })

@main_bp.route('/display')
def display_pokenea():
    pokenea = random.choice(POKENEAS)
    container_id = os.uname().nodename
    return render_template('display.html', pokenea=pokenea, container_id=container_id)
