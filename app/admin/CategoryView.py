from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField


class CategoryView(ModelView):
    
    # Tela de edição em modal
    edit_modal = True

    # Edição através da grid
    column_editable_list = ['description']

    # Substiuição de texto da grid
    column_choices = {
        'status': [
            (0, 'Desabilitado'),
            (1, 'Habilitado'),
        ]
    }

    column_labels = {
        'description': 'Descrição',
        'created_at': 'Criação',
        'updated_at': 'Atualização'
    }

    column_formatters = {
        'created_at': lambda v, c, m, p: m.created_at.strftime('%d/%m/%Y %H:%M:%S'),
        'updated_at': lambda v, c, m, p: m.created_at.strftime('%d/%m/%Y %H:%M:%S')
    }

    column_exclude_list = ['post']
    
    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'description'
    ]

    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'description',
        'status'
    ]

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
