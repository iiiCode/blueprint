from flask import Blueprint, url_for, request

simple_page = Blueprint("simple_page", __name__, static_folder="static")

@simple_page.route('/', defaults={"page": "index"})
@simple_page.route("/<page>")
def show(page):
    return "Simple Page: " + page

@simple_page.route("/show_url")
def simple_page_show_url():
    return request.url_root[:-1] + url_for("simple_page.static", filename="style.css")

@simple_page.route("/url")
def simple_page_url():
    return request.url_root[:-1] + url_for(".simple_page_url")
