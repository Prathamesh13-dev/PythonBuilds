from flask import Flask,render_template,request,redirect,url_for
accounts ={}
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
class Account:
    def __init__(self,name,age,balance):
        self.name = name
        self.age = age
        self.balance = balance
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -=amount
            return f"Withdrawn {amount} successfully ✅"
        else :
            return "Insufficient balance ❌"
    def deposit(self,amount):
        self.balance +=amount
        return f"Deposited {amount} successfully ✅"
@app.route('/create_page',methods=['GET','POST'])
def create_account():
    if request.method == 'POST':
        Account_no = int(request.form["account_no"])
        name = request.form["name"]
        age = int(request.form["age"])
        balance = int(request.form["balance"])

        accounts[Account_no] = Account(name,age,balance) 
        return redirect(url_for("home")) 
    return render_template("create.html")
@app.route('/withdraw_page',methods = ['GET','POST'])
def withdraw():
    if request.method =='POST':
        Account_no = int(request.form['account_no'])
        amt = int(request.form["amount"])
        result =accounts[Account_no].withdraw(amt)
        return result
    return render_template("withdraw.html")
@app.route('/deposit_page',methods=['GET','POST'])
def Deposit():
    if request.method == 'POST':
        Account_number = int(request.form["account_no"])
        amt = int(request.form["amount"])
        result = accounts[Account_number].deposit(amt)
        return result
    return render_template("deposit.html")
@app.route('/balance_page',methods=['GET','POST'])
def balance():
    if request.method == 'POST':
        Account_number = int(request.form["account_no"])
        result = accounts[Account_number].balance
        return f"Your Balance is {result} ₹"
    return render_template("balance.html")
@app.route('/accounts',methods=['GET','POST'])
def acc():
    return f"Total accounts {len(accounts)}"
if __name__ == "__main__":
    app.run(debug=True)
