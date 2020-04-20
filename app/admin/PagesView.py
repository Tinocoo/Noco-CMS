from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField
from .CKTextArea import CKTextAreaField


class PagesView(ModelView):
    
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    # Edição através da grid
    column_editable_list = ['title']

    # Colunas excluídas da grid
    column_exclude_list = ['body']

    # Campos da grid utilizado para pesquisa
    column_searchable_list = ['title']

    # Substiuição de texto da grid
    column_choices = {
        'status': [
            (0, 'Desabilitado'),
            (1, 'Habilitado'),
        ]
    }

    # Campos utilizados para filtros avançados
    column_filters = [
        'title',
        'created_at',
        'status'
    ]

    column_labels = {
        'title': 'Titulo',
        'created_at': 'Criação',
        'updated_at': 'Atualização'
    }

    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'title',
        'body'
    ]

    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'title',
        'body',
        'status'
    ]


    form_overrides = {
        'body': CKTextAreaField,
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

