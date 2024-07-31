from flask import Flask, jsonify
from models.gato import Gato
from models.perro import Perro
from models.boa import Boa
from models.huron import Huron

app = Flask(__name__)

@app.route('/sonido/<animal>', methods=['GET'])
def home(animal):
    if animal == 'Gato':
        print(animal)
        return  jsonify({"animal": animal, "sonido": Gato.hacer_sonido()})
    elif animal == 'Perro':
        print(Perro.hacer_sonido())
        return jsonify({"animal": animal, "sonido": Perro.hacer_sonido()})
    elif animal == 'Boa':
        return jsonify({"animal": animal, "sonido": Boa.hacer_sonido()})
    elif animal == 'Huron':
        return jsonify({"animal": animal, "sonido": Huron.hacer_sonido()})
    else:
        return jsonify({"error": "Animal no encontrado"}), 404
    

if __name__ == '__main__':
    app.run(debug=True)