from app import app
@app.route("/product/add")
def product():
    return "This is a Product add function"