from flask import Blueprint, render_template
from .models import Product

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)