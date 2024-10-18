from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='static')

balance = 0.0

@app.route("/balance", methods=["GET"])
def get_balance():
    print(f"Your Balance is ${balance:.2f}")
    return jsonify({"balance": balance})

@app.route("/deposit", methods=["POST"])
def deposit():
    global balance
    amount = float(input("Enter an amount to be deposited: "))
    amount = request.json.get("amount")
    if amount < 0:
        return jsonify({"error": "Amount must be positive"}), 400
    balance += amount
    return jsonify({"balance": balance})

@app.route("/withdraw", methods=["POST"])
def withdraw():
    global balance
    amount = float(input("Enter amount to be withdraw : "))
    amount = request.json.get("amount")
    if amount > balance:
        return jsonify({"error": "Insufficient balance"}), 400
    if amount < 0:
        return jsonify({"error": "Amount must be positive"}), 400
    balance -= amount
    return jsonify({"balance": balance})

# Serve static HTML file (index.html)
@app.route('/')
def Banking():
    return send_from_directory(app.static_folder, 'Banking.html')

balance=0
is_running = True

while is_running:
    print('1.show_balance')
    print('2.deposit')
    print('3.withdraw')
    print('4.exit')
     

    choice = input("Enter your choice(1-4): ")

    if choice == '1':
         get_balance(balance)
    elif choice == '2':
         balance += deposit()
    elif choice == '3':
         balance -= withdraw(balance)
    elif choice == '4':
         is_running = False
    else:
         print("Your choice is not vaild")
  
print("Thank You! Have a nice day")
 




if __name__ == '__main__':
    app.run(debug=True)
