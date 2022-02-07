from dataclasses import dataclass
from app.catalog import main
from .models import Book,Publication
from flask import render_template, request, redirect,url_for,flash
from flask_login import login_required 
from app.catalog.models import Book
from app import db
from app.catalog.forms import CreateBookForm, EditBookForm


@main.route("/")
def home():
    book = Book.query.all()
    return render_template("home.html", books=book)

@main.route("/show/publisher/<publisher_id>")
def show_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
    return render_template("publication.html", publisher=publisher, publisher_books=publisher_books)


@main.route("/delete/<int:book_id>", methods=['GET','POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == "POST":
        db.session.delete(book)
        db.session.commit()
        flash("book deleted successfully!")
        return redirect(url_for('main.home'))
    return render_template('delete.html',book=book,book_id=book_id)


@main.route('/edit/<int:book_id>', methods=['GET','POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash("Book added successfully!")
        return redirect(url_for('main.home'))
    return render_template('edit.html',form=form)


@main.route('/create/<int:pub_id>',methods=['GET','POST'])
def add_book(pub_id):
    form = CreateBookForm()
    form.pub_id.data =pub_id
    if form.validate_on_submit():
        book = Book(
            title = form.title.data,
            author = form.author.data,
            format = form.format.data,
            avg_rating = form.avg_rating.data,
            image = form.image.data,
            num_pages= form.num_pages.data,
            pub_id = form.pub_id.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Book added!')
        return redirect(url_for('main.home'))

    return render_template('create.html',form=form,pub_id=pub_id)