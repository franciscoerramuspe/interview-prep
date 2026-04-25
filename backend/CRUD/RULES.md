# Rules

As I am new to writing backend in python, I will write rules or tricks here as I am finding them

## REST APIs
#### HTTP Status Codes

| Code | Meaning |
|------|---------|
| `200` | OK |
| `201` | Created (use this for successful POST) |
| `400` | Bad Request |
| `401` | Unauthorized (not logged in) |
| `403` | Forbidden (logged in but no permission) |
| `404` | Not Found |
| `422` | Unprocessable Entity |
| `500` | Internal Server Error |

#### How to curl
   * structure: 
       * if using GET: `curl http://localhost:8000/endpoint`
       * if not using GET: `curl -X POST/PUT/DELETE http://localhost:8000/endpoint`
          * For POST/PUT with a body: `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://localhost:8000/endpoint`
          * For DELETE (usually targets a resource by id): `curl -X DELETE http://localhost:8000/endpoint/1`

## Python agnostic
* Managing dictionaries
   * ✅ Wrap keys in quotes
     newExpense = { "name": expenseName, "price": expensePrice }
   * iterating through dictionaries



## Fast API framework

    * Managing  



Path params
