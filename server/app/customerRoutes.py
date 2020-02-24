from flask import render_template, request
from app import app
from pymongo import MongoClient

mongoClient = MongoClient('127.0.0.1', 27017)
db = mongoClient.customerData

# Customer Home Page
@app.route('/customerHome')
def customerHomePage():
    return render_template('CustomerHomePage.html')

# Form for new customer details and measurements
@app.route('/customer/new', methods=['GET'])
def NewCustomerPage():
    return render_template('newCustomerDetailsForm.html')

# Add customer details to database
@app.route('/customer/addCustomerDetails', methods=['GET'])
def addNewCustomer():
    customerData = {}
    customerData["name"] = request.args.get('name')  
    customerData["address"] = request.args.get('address')  
    customerData["phone"] = request.args.get('phone')  
    customerData["email"] = request.args.get('email')  
    customerData["napeToAboveBustVertical"] = request.args.get('napeToAboveBustVertical')  
    customerData["napeToAboveBustCircular"] = request.args.get('napeToAboveBustCircular')  
    customerData["napeToApexVertical"] = request.args.get('napeToApexVertical')  
    customerData["napeToApexCircular"] = request.args.get('napeToApexCircular')  
    customerData["napeToWaistVertical"] = request.args.get('napeToWaistVertical')  
    customerData["napeToWaistCircular"] = request.args.get('napeToWaistCircular')  
    customerData["napeToUpperHipVertical"] = request.args.get('napeToUpperHipVertical')  
    customerData["napeToUpperHipCircular"] = request.args.get('napeToUpperHipCircular')  
    customerData["napeToHipVertical"] = request.args.get('napeToHipVertical')  
    customerData["napeToHipCircular"] = request.args.get('napeToHipCircular')  
    customerData["napeToTopLengthVertical"] = request.args.get('napeToTopLengthVertical')  
    customerData["napeToTopLengthCircular"] = request.args.get('napeToTopLengthCircular')  
    customerData["napeToShortKurtiVertical"] = request.args.get('napeToShortKurtiVertical')  
    customerData["napeToShortKurtiCircular"] = request.args.get('napeToShortKurtiCircular')  
    customerData["waistToThighVertical"] = request.args.get('waistToThighVertical')  
    customerData["waistToThighCircular"] = request.args.get('waistToThighCircular')  
    customerData["waistToMidThighVertical"] = request.args.get('waistToMidThighVertical')  
    customerData["waistToMidThighCircular"] = request.args.get('waistToMidThighCircular')  
    customerData["waistToKneeVertical"] = request.args.get('waistToKneeVertical')  
    customerData["waistToKneeCircular"] = request.args.get('waistToKneeCircular')  
    customerData["waistCalfVertical"] = request.args.get('waistCalfVertical')  
    customerData["waistCalfCircular"] = request.args.get('waistCalfCircular')  
    customerData["waistToAnkleVertical"] = request.args.get('waistToAnkleVertical')  
    customerData["waistToAnkleCircular"] = request.args.get('waistToAnkleCircular')  
    customerData["waistToFloorVertical"] = request.args.get('waistToFloorVertical')  
    customerData["waistToFloorCircular"] = request.args.get('waistToFloorCircular')  
    customerData["capsLengthwise"] = request.args.get('capsLengthwise')  
    customerData["capsRound"] = request.args.get('capsRound')  
    customerData["shortSleeveLengthwise"] = request.args.get('shortSleeveLengthwise')  
    customerData["shortSleeveRound"] = request.args.get('shortSleeveRound')  
    customerData["elbowLengthwise"] = request.args.get('elbowLengthwise')  
    customerData["elbowRound"] = request.args.get('elbowRound')  
    customerData["threeQuatersLengthwise"] = request.args.get('threeQuatersLengthwise')  
    customerData["threeQuatersRound"] = request.args.get('threeQuatersRound')  
    customerData["fullLengthwise"] = request.args.get('fullLengthwise')  
    customerData["fullRound"] = request.args.get('fullRound')  
    customerData["armHoleLengthwise"] = request.args.get('armHoleLengthwise')  
    customerData["armHoleRound"] = request.args.get('armHoleRound')  
    customerData["shoulder"] = request.args.get('shoulder')  
    customerData["acrossFront"] = request.args.get('acrossFront')  
    customerData["acrossBack"] = request.args.get('acrossBack')  
    customerData["shoulderWidth"] = request.args.get('shoulderWidth')  
    customerData["acrossFrontForSleeveless"] = request.args.get('acrossFrontForSleeveless')  
    customerData["neckDepthForBlouseFront"] = request.args.get('neckDepthForBlouseFront')  
    customerData["neckDepthForBlouseBack"] = request.args.get('neckDepthForBlouseBack')  
    customerData["neckDepthForDressFront"] = request.args.get('neckDepthForDressFront')  
    customerData["neckDepthForDressBack"] = request.args.get('neckDepthForDressBack')

    print(customerData)

    if (db.customerData.find({"name": customerData["name"]}).count()>0):
        return render_template('newCustomerAdded.html', text = "Customer with given name already exists")

    db.customerData.update({"name": customerData["name"], "phone": customerData["phone"]}, {"$set":customerData}, upsert=True)

    return render_template('newCustomerAdded.html')

@app.route('/customer/getCustomerDetails')
def getchCustomerDetails():
    customerName = request.args.get("name")
    customerPhone = request.args.get("phone")

    customerData = db.customerData.find({"name": customerName, "phone": customerPhone})



    return render_template('CustomerDetailsPage.html', customerData = customerData)