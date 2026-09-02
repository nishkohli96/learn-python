# InsufficientFundsError: Not enough balance to withdraw
#
# Calling super().__init__(message) sets up the standard exception
# message so print(e) and default tracebacks still work normally.
class InsufficientFundsError(Exception):
    def __init__(self, balance: int, amount: int):
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(f"Tried to withdraw {amount}, but balance is only {balance}")


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


bal_amt = withdraw(200, 70)
print(f"bal_amt: {bal_amt}")

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    # repr(e) → type + message.
    # print(repr(e)) # InsufficientFundsError('Tried to withdraw 150, but balance is only 100')
    print("ERROR: ", e)  # the message
    print(f"Account deficit by {e.shortfall}")  # 50 — custom data you can use in the handler


# For real use case scenario we would have to handle custom exceptions like this -
# class PaymentAPIError(Exception):
#     """Raised when the payment gateway call fails."""
#     pass

# def charge_customer(amount, customer_id):
#     try:
#         response = payment_gateway.charge(amount, customer_id)
#         return response
#     except Exception as e:
#         raise PaymentAPIError(
#             f"Failed to charge customer {customer_id} for {amount}"
#         ) from e
# Bonus
# class PaymentAPIError(Exception):
#     def __init__(self, message, original_exception=None):
#         super().__init__(message)
#         self.original_exception = original_exception
#
# print(original_exception) works directly and will show the exception's message.
#
# try:
#     ...
# except Exception as e:
#     raise PaymentAPIError("Payment failed", original_exception=e) from e