from flask import Flask, jsonify, render_template, request
from project_app.utils import SalesPrice

# Creating instance here
# 'app' is standard variable
app = Flask(__name__)

# @app.route("/") --> USED TO GET HOME API
# @app.route("/furniture") --> You will get 'Furniture' Page here

@app.route("/")
def hello_flask():
    print("Welcome to Cars price Prediction")
    return render_template("index.html")


@app.route("/predict_charges",methods=["POST","GET"])
def get_insurance_charges():
    if request.method =="GET":
        print("We are in a GET Method")
                
    
        symboling = float(request.args.get("symboling"))
        normalized_losses = float(request.args.get("normalized_losses"))
        fuel_type = request.args.get("fuel_type")
        aspiration = request.args.get("aspiration")
        num_of_doors = request.args.get("num_of_doors")
        drive_wheels = request.args.get("drive_wheels")
        engine_location = request.args.get("engine_location")
        wheel_base = float(request.args.get("wheel_base"))
        length = float(request.args.get("length"))
        width = float(request.args.get("width"))
        height = float(request.args.get("height"))
        curb_weight = float(request.args.get("curb_weight"))
        num_of_cylinders = request.args.get("num_of_cylinders")
        engine_size = float(request.args.get("engine_size"))
        bore = float(request.args.get("bore"))
        stroke = float(request.args.get("stroke"))
        compression_ratio = float(request.args.get("compression_ratio"))
        horsepower = float(request.args.get("horsepower"))
        peak_rpm = float(request.args.get("peak_rpm"))
        city_mpg = float(request.args.get("city_mpg"))
        highway_mpg = float(request.args.get("highway_mpg"))
        engine_type = request.args.get("engine_type")
        body_style = request.args.get("body_style")
        fuel_system = request.args.get("fuel_system")


    
    else:
        print("error in if block")
        


    sal_pri=SalesPrice(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,engine_type,body_style,fuel_system)
    charges=sal_pri.get_predicted_charges()
    return render_template("index.html",prediction=charges)


print("__name__-->",__name__)
if __name__=="__main__":
    #app.run(host="0.0.0.0",post=5000,debug=false)
    app.run()
