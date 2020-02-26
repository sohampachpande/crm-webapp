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
    return render_template('newCustomerForm.html')


# Add customer details to database
@app.route('/customer/addCustomerDetails', methods=['GET'])
def addNewCustomer():
    customerData = request.args.to_dict()
    if (db.customerData.find({"name": customerData["name"], "phone": customerData["phone"]}).count() > 0):
        # return render_template('newCustomerAdded.html', text = "Customer with given name already exists")
        return "Customer with given name and phone already exists"

    db.customerData.update(
        {
            "name": customerData["name"],
            "phone": customerData["phone"]
        }, {"$set": customerData},
        upsert=True)

    return render_template('newCustomerAdded.html')


@app.route('/customer/searchCustomerDetails', methods=['GET'])
def searchCustomerDetails():
    customerName = request.args.get("name")
    customerPhone = request.args.get("phone")

    if customerPhone:
        customerData = db.customerData.find({"phone": customerPhone})
    elif customerName:
        customerData = db.customerData.find(
            {"$text": {
                "$search": customerName
            }})
    else:
        print(customerName, customerPhone)
        return "You have to mention name or phone of client"

    return render_template('CustomerSearchPage.html', customerPhone = customerPhone,
                           customerName = customerName, customerData = list(customerData))


@app.route('/customer/getCustomerDetails')
def getCustomerDetails():
    # customerName = request.args.get("name")
    customerPhone = request.args.get("phone")

    customerData = db.customerData.find({
        "phone": customerPhone,
    })

    print("\n\n", customerPhone , "customer details \n\n")

    return render_template('CustomerDetailsPage.html',
                           customerData=list(customerData)[0])