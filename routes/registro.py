from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
from models.user import User

registro = Blueprint("registro", __name__)
