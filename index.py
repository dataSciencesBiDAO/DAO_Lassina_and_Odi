from flask import Flask, request, render_template
import numpy as np
import pickle
app = Flask(__name__)

model= pickle.load(open('model.pk','rb'))


@app.route('/', methods=['POST', 'GET'])
def form_data():
    if request.method=='GET':
        return render_template('form.html')
    else:
        for datas in request.form.values():
            if not datas :
                return render_template('form.html', error="Veuillez saisir correctement les données.")
        data = [int(x) for x in request.form.values()]
        d = np.array(data)
        reshaped=d.reshape(1,-1) 
        predict = model.predict(reshaped)
        if predict == 0:
            prediction = "Vous avez au moins une maladie cardiaque"
        else:
            prediction = "Vous n'avez aucune maladie cardiaque"

    return render_template('form.html', prediction=prediction, data=request.form)



