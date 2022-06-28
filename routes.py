from distutils.log import error
from importlib import import_module
import string
from flask import Blueprint, redirect, render_template, current_app, url_for
from .schemas import URLSchema
from .forms import URLForm
import uuid
from .keygen import key_generator
from dataclasses import asdict


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/", methods=["GET", "POST"])
def index():
    url_form = URLForm()

    if url_form.validate_on_submit():
        url_data = URLSchema(
            _id=uuid.uuid4().hex,
            url=url_form.userinput_url.data,
            shortened_url=key_generator()
        )
        current_app.db.url_database.insert_one(asdict(url_data))

    return render_template(
        template_name_or_list="index.html",
        url_form=url_form,
        given_link=f"http://127.0.0.1:5000/{url_data.shortened_url}"
    )


@pages.route("/<url_id>")
def redirect_func(url_id: string):
    load_url_data = current_app.db.url_database.find_one(
        {"shortened_url": url_id}
    )

    if load_url_data:
        try:
            url_data = URLSchema(**load_url_data)
            return redirect(url_data.url)
        except:
            return render_template(
                template_name_or_list="error_404.html",
                error="An error occured in redirection"
            )

    return render_template(
        template_name_or_list="error_404.html",
        error="The link doesn't exist")
