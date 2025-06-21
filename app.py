from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"✅ ₹{amount} deposited successfully."
        else:
            return "❌ Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= 0:
            return "❌ Invalid withdrawal amount."
        elif amount > self.balance:
            return "❌ Insufficient balance."
        else:
            self.balance -= amount
            return f"✅ ₹{amount} withdrawn successfully."

    def check_balance(self):
        return f"💰 Current balance: ₹{self.balance:.2f}"

account = BankAccount()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transaction', methods=['POST'])
def transaction():
    data = request.json
    action = data['action']
    amount = float(data.get('amount', 0))

    if action == 'deposit':
        result = account.deposit(amount)
    elif action == 'withdraw':
        result = account.withdraw(amount)
    elif action == 'balance':
        result = account.check_balance()
    else:
        result = "❌ Invalid action"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
