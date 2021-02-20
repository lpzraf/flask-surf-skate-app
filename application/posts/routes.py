
from flask import (render_template, request,
                   redirect, url_for, Blueprint)
from application.posts.forms import PostForm, DeleteForm
from application.models import User, Post
from application import db
import datetime
from decorators import ensure_authenticated, ensure_correct_user

posts_bp = Blueprint(
    'posts',
    __name__,
    template_folder='templates'
)


# posts index
@posts_bp.route('/', methods=['GET', 'POST'])
@ensure_authenticated
def index(user_id):
    date = datetime.datetime.now().strftime('%A, %b %d, %Y')
    delete_form = DeleteForm()
    found_user = User.query.get(user_id)
    if request.method == 'POST':
        form = PostForm(request.form)
        if form.validate():
            new_posts = Post(request.form['title'], datetime.datetime.now(),
                             request.form['post_body'], user_id)
            db.session.add(new_posts)
            db.session.commit()
            return redirect(url_for('posts.index', user_id=user_id))
        else:
            return render_template('posts/new.html', form=form)
    return render_template('posts/index.html', user=found_user,
                           delete_form=delete_form, date=date)


# posts new
@posts_bp.route('/new', methods=['GET', 'POST'])
@ensure_authenticated
@ensure_correct_user
def new(user_id):
    found_user = User.query.get(user_id)
    post_form = PostForm()
    return render_template('posts/new.html', user=found_user, form=post_form)


# posts edit
@posts_bp.route('/<int:id>/edit')
@ensure_authenticated
@ensure_correct_user
def edit(user_id, id):
    found_post = Post.query.get(id)
    post_form = PostForm(obj=found_post)
    return render_template('posts/edit.html', post=found_post, form=post_form)


# posts show
@posts_bp.route('/<int:id>',  methods=['GET', 'PATCH', 'DELETE'])
@ensure_authenticated
@ensure_correct_user
def show(user_id, id):
    found_post = Post.query.get(id)
    found_user = User.query.get(user_id)
    if request.method == b"PATCH":
        found_post.title = request.form["title"]
        found_post.post_body = request.form["post_body"]
        db.session.add(found_post)
        db.session.commit()
        return redirect(url_for('posts.index', user_id=user_id))
    if request.method == b"DELETE":
        delete_form = DeleteForm(request.form)
        if delete_form.validate():
            db.session.delete(found_post)
            db.session.commit()
        return redirect(url_for('posts.index', user_id=user_id))
    return render_template('posts/show.html', post=found_post, user=found_user)
