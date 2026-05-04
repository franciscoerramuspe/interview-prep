'''
1. Build CRUD APIs Fast


Exercises
    Expense tracking API
    Create expense
    Approve expense
    Get expenses by user
    Invoice system
    Upload invoice metadata
    Mark paid/unpaid
    Search invoices
    Card transactions API
    Authorize transaction
    Decline if limit exceeded
    What they test
    Data modeling
    Endpoint structure
    Validation
    Clean code
    Speed
    Stack suggestion

Python + FastAPI'''

'''
    before building any of this, is really important to define the data structures
    some questions you can ask yourself are:
        "how do the expense report should look like?"
        "which features do I want to support? i.e 
            CRUD expenses?
            fitler expenses by user?
            should expenses have a paid status(paid/unpaid)?
            should expenses have a limit?
    
    the list goes on and on and you should reach to a state that where you feel comfortable clearing the ambiguity before even writing a single line of code
'''

'''
    assume we want:
        1) CRUD expenses
        2) filter expenses by user
        3) filter expenses by state
        4) filter expenses by min_value or max_value
    expense schema
        expense_id
        user_id
        description
        amount
        status
'''

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

ALLOWED_KEYS = {"expense_id", "user_id", "description", "amount", "status"}

expenses = [
    {
        "expense_id": 1,
        "user_id": 1,
        "description": "Lunch at Chipotle",
        "amount": 12.97,
        "status": "paid"
    },
   {
        "expense_id": 2,
        "user_id": 2,
        "description": "Uber",
        "amount": 20.15,
        "status": "pending"
    },
   {
        "expense_id": 3,
        "user_id": 1,
        "description": "Hotel",
        "amount": 90.72,
        "status": "paid"
    },
]

# GET methods
@app.get("/expenses")
def get_expenses():
    return expenses

@app.get("/expenses/{user_id}")
def get_expenses_by_user(user_id: int):
    id_is_valid = user_id > 0

    if not user_id or not id_is_valid:
        raise HTTPException(status_code=400, detail="user_id must be an int greater than 0")

    expensesFromUser = [expense for expense in expenses if expense["user_id"] == user_id]

    if not expensesFromUser:
        raise HTTPException(status_code=404, detail="No expenses found for user with user_id {user_id}")

    return expensesFromUser
      


# POST
# tip: when creating resources, send them via body params
    # this keeps urls cleaner and easier to validate, and avoid manipulation
@app.post('/expense')
# given that an expense has many params, pass a dict and validate rather than passing all the fields as params
def add_expense(expense: dict): 
    for field in expense:
        if field not in ALLOWED_KEYS:
            raise HTTPException(status_code=400, detail=f"Field {field} not allowed. An expense must have the attached fields: {ALLOWED_KEYS}")
        
    expenses.append(expense)
    return JSONResponse(status_code=200, content={"message": "successfully added expense"})


# DELETE
@app.delete("/expense/{expense_id}")
def delete_expense(expense_id: int):
    for i, expense in enumerate(expenses):
        current_expense_id = expense["expense_id"]
        is_present = current_expense_id == expense_id

        if is_present:
            del expenses[i]
            return JSONResponse(status_code=200, content={"message": "successfully deleted expense"})
    
    raise HTTPException(status_code=404, detail="expense not found")

# PUT
@app.put('/expense/{expense_id}')
def update_expense(expense_id: int, details_to_update)



        