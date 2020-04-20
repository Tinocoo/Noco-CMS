from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField, SelectField
from werkzeug.security import generate_password_hash



class UserView(ModelView):
    
    # Tela de edição em modal
    edit_modal = True

    # Edição através da grid
    column_editable_list = ['name']
    
    # Colunas excluídas da grid
    column_exclude_list = [
        'password'
    ]
    
    # Campos da grid utilizado para pesquisa
    column_searchable_list = [
        'email'
    ]

    # Substiuição de texto da grid
    column_choices = {
        'status': [
            (0, 'Desabilitado'),
            (1, 'Habilitado'),
        ]
    }
    
    # Campos utilizados para filtros avançados
    column_filters = [
        'name',
        'email'
    ]
    
    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'name',
        'email',
        'password',
    ]
    
    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'name',
        'email',
        'status'
    ]
    
    # Fields personalizados no formulário
    form_extra_fields = {
        'password': PasswordField("Password")
    }

    form_overrides = {
        'status': SelectField
    }

    form_args = {
        'status': dict(
            choices=[
                (0, 'Desabilitado'),
                (1, 'Habilitado'),
            ],
            coerce=int
        )
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(form.password.data)
    