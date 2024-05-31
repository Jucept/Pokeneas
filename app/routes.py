from flask import Blueprint, jsonify, render_template
from .pokeneas import POKENEAS
import random
import os

main_bp = Blueprint('main', __name__)

def get_container_id():
    try:
        with open('/etc/hostname') as f:
            container_id = f.read().strip()
    except FileNotFoundError:
        container_id = 'localhost'
    return container_id

@main_bp.route('/json')
def get_pokenea_json():
    pokenea = random.choice(POKENEAS)
    container_id = get_container_id()
    return jsonify({
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'container_id': container_id,
        'frase_filosofica': pokenea['frase_filosofica'],
    })

@main_bp.route('/index')
def display_pokenea():
    pokenea = random.choice(POKENEAS)
    container_id = get_container_id()
    return render_template('index.html', pokenea=pokenea, container_id=container_id)
