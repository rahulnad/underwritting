from flask import Flask, render_template, url_for, flash, redirect,request,flash
from forms import registrationform

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/result/<age>/<vehicle_value>",methods=['GET', 'POST'])
def result(age,vehicle_value):
     print("age",age)
     print("vehiclevalue1",vehicle_value)
     input_vehicle_value = 0
     if int(age) == 30:
      input_vehicle_value = int(vehicle_value)*0.05
      print(input_vehicle_value)
     return render_template('result.html', title='result',result=input_vehicle_value)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registrationform()
    input_age = request.form.get('age')
    print("age",input_age)
    input_vehicle_value = request.form.get('VehicleValue')
    print("vehiclevalue",input_vehicle_value)
    #print(dir(form))
    if form.validate_on_submit():
        return redirect(url_for('result',age=input_age,vehicle_value=input_vehicle_value))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)