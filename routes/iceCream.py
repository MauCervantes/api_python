from flask import Blueprint, request
from models.Helado import Helado
from controllers.controller import new, view

icecream = Blueprint('icecream', __name__)


@icecream.route("/new", methods=['POST'])
def add_iceCream():
    name = request.form['name']
    flavor = request.form['flavor']

    new_helado = Helado(name, flavor)

    new(new_helado)
    return 'Se ha insertado un nuevo registro: { "name": "' + new_helado.name + '", "flavor": "' + new_helado.flavor + '"}'



@icecream.route("/view", methods=['GET'])
def view_iceCream():
    result = view()
    iceC = ""

    for row in result:
        print(row)
        iceC = iceC + str(row) + "\n"
    return iceC
