from flask import redirect, url_for
from flask.templating import render_template
from flask.views import MethodView
from flask_restful import reqparse
from werkzeug.security import check_password_hash
from app.models.Users import Users
from app.repositories import BaseResource


class ManageLogin(MethodView):


    def get(self):
        return render_template('admin/login.html')

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email')
        parser.add_argument('password')
        data = parser.parse_args()
        user = BaseResource(Users).getFirst({'email': data['email']})
        if user['status'] == 200:
            response = user['result'][0]
            if check_password_hash(response['password'], data['password']):
                return redirect(url_for('admin.index'))

        return redirect(url_for('login.ManageLogin'))
