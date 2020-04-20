from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField
from .CKTextArea import CKTextAreaField


class FaqsView(ModelView):
    
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    
    column_editable_list = ['title']

    column_exclude_list = [
        'body',
        'img_url',
        'button_text',
        'button_link',
    ]

    # Campos da grid utilizado para pesquisa
    column_searchable_list = [
        'title'
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
        'title',
        'created_at'
    ]

    column_labels = {
        'title': 'Titulo',
        'url_img': 'Imagem',
        'created_at': 'Criação',
        'updated_at': 'Atualização'
    }

    column_formatters = {
        'created_at': lambda v, c, m, p: m.created_at.strftime('%d/%m/%Y %H:%M:%S'),
        'updated_at': lambda v, c, m, p: m.created_at.strftime('%d/%m/%Y %H:%M:%S')
    }

    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'title',
        'url_img',
        'body',
        'button_text',
        'button_link'
    ]
    
    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'title',
        'url_img',
        'body',
        'button_text',
        'button_link',
        'status'
    ]

    form_overrides = {
        'status': SelectField,
        'body': CKTextAreaField
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
    