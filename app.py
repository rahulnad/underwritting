from flask import Flask, render_template, url_for, flash, redirect,request,flash
from forms import registrationform
from datetime import datetime,date

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/result/<first_name>/<last_name>/<email>/<dob>/<zipcode>/<make>/<brand>/<yearofcar>/<mileage>/<commute>/<storage>/<drivinghistory>/<accidenthistory>/<cac>",methods=['GET', 'POST'])
def result(first_name,last_name,email,dob,zipcode,make,brand,yearofcar,mileage,commute,storage,drivinghistory,accidenthistory,cac):
    base_premium = 450
    is_accident =0.70
    is_amod = 0.10
    is_oneyear = 0.40
    is_twoyear = 0.30
    is_threeyear = 0.20
    is_fouryear = 0.10
    current_date = datetime.now()
    dh = datetime.strptime(drivinghistory,'%Y-%m-%d')
    delta = current_date - dh
    delta_years = int((delta).days/365)
    print(delta_years)

    msg = ""
    if commute == 'yes' or storage == 'no' or brand not in ('Buick','Dodge','Ford','Honda','Mitsubishi','Nissan','Pontiac','Saturn','Volkswagen') \
       or make not in ('Regatta','Ram SRT10','Lightning','S2000','3000GT','350Z','G8','Sky','Cabriolet'):
        msg = "Your application is not approved"
    elif accidenthistory == 'no' or cac in ['American Modern','american modern','AMOD''amod','AMERICAN MODERN','amig']:
        calculated_base_premium = base_premium - base_premium*is_amod
        msg = "Your application is approved and your quote is :"+str(drivinghistorycaluclation(delta_years, calculated_base_premium))
    elif  accidenthistory == 'yes' or cac in ['American Modern','american modern','AMOD''amod','AMERICAN MODERN','amig']:
        calculated_base_premium = base_premium + (base_premium)*is_accident - (base_premium)*is_amod
        msg = "Your application is approved and your quote is :"+str(drivinghistorycaluclation(delta_years, calculated_base_premium))
    elif  cac in ['American Modern','american modern','AMOD''amod','AMERICAN MODERN','amig']:
        calculated_base_premium = base_premium - (base_premium)*is_amod
        msg = "Your application is approved and your quote is :"+str(drivinghistorycaluclation(delta_years, calculated_base_premium))
    elif  accidenthistory == 'yes' or cac in ['American Modern','american modern','AMOD''amod','AMERICAN MODERN','amig']:
        calculated_base_premium = base_premium + (base_premium)*is_accident - (base_premium)*is_amod
        msg = "Your application is approved and your quote is :"+str(drivinghistorycaluclation(delta_years, calculated_base_premium))
    else:
        msg = "We are unable to process your application. Please contact your local agent"

    
    return render_template('result.html', title='result',result=msg)

def drivinghistorycaluclation(delta_years,calculated_bp):
    if delta_years < 2:
        return calculated_bp + (calculated_bp*0.40)
    elif delta_years == 2:
        return calculated_bp + (calculated_bp*0.30)
    elif delta_years == 3:
        return calculated_bp + (calculated_bp*0.20)
    elif delta_years == 4:
        return calculated_bp + (calculated_bp*0.10)
    else:
        return calculated_bp 


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registrationform()
    if form.validate_on_submit():
  
        input_first_name = request.form.get('firstname')
    
        input_last_name = request.form.get('lastname')
    
        input_email = request.form.get('email')
  
        input_dob = request.form.get('dob')
    
        input_zip_code = request.form.get('zipcode')
      
        input_make = request.form.get('make')

        input_brand = request.form.get('brand')

        input_yearofcar = request.form.get('yearofcar')

        input_mileage = request.form.get('mileage')
     
        input_commute = request.form.get('commute')
    
        input_storage = request.form.get('storage')

        input_dh = request.form.get('drivinghistory')
    
        input_ah = request.form.get('accidenthistory')

        input_ac = request.form.get('currentautocarrier')
   
        return redirect(url_for('result',first_name=input_first_name,last_name=input_last_name,email=input_email,dob=input_dob,zipcode=input_zip_code,make=input_make,brand=input_brand,yearofcar = input_yearofcar,mileage=input_mileage,commute=input_commute,storage=input_storage,drivinghistory=input_dh,accidenthistory=input_ah,cac=input_ac))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)