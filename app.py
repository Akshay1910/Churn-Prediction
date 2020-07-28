from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('bank.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
       
        CreditScore = int(request.form['CreditScore'])
        Age = int(request.form['Age'])
        
        Tenure = int(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = int(request.form['NumOfProducts'])
        
        IsActiveMember = request.form['IsActiveMember']
        if(IsActiveMember == 'Yes'):
            IsActiveMember = 1
        else:
            IsActiveMember = 0

        HasCrCard = request.form['HasCrCard']
        if(HasCrCard == 'Yes'):
            HasCrCard = 1
        else:
            HasCrCard = 0

        EstimatedSalary = float(request.form['EstimatedSalary'])
        Geography = request.form['Geography']
        if(Geography == 'France'):
            Geography_France = 1
            Geography_Germany = 0
            Geography_Spain = 0
        elif(Geography == 'Germany'):
            Geography_France = 0
            Geography_Germany = 1
            Geography_Spain = 0
        else:
            Geography_France = 0
            Geography_Germany = 0
            Geography_Spain = 1

        Gender = request.form['Gender']
        if(Gender == 'Male'):
            Gender_Female = 0
            Gender_Male = 1
        else:
            Gender_Female = 1
            Gender_Male = 0

       
        

        prediction = model.predict([[CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember,
                                    EstimatedSalary, Geography_France, Geography_Germany, Geography_Spain, Gender_Female, Gender_Male]])
        output = int(prediction[0])
        if output == 0:
            return render_template('index.html', prediction_text='Customer wont quit')
        else:
            return render_template('index.html', prediction_text='Work on customer..He might quit in future')


    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
