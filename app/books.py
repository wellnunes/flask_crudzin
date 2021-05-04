from flask import Blueprint
from .model import Book


bp_books = Blueprint('books', __name__)

@bp_books.route('/create', methods=['POST'])
def create():
    ...

@bp_books.route('/update', methods=['POST'])
def update():
    ...

@bp_books.route('/delete', methods=['GET'])
def delete():
    ...

@bp_books.route('/list', methods=['GET'])
def list():
    ...
