from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField
from .CKTextArea import CKTextAreaField


class PricePlansView(ModelView):
    
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    # Edição através da grid
    column_editable_list = ['title']

    # Colunas excluídas da grid
    column_exclude_list = [
        'body',
        'price',
        'url_img',
        'button_text',
        'button_link'
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
        'created_at',
        'price'
    ]

    column_labels = {
        'title': 'Titulo',
        'body': 'Conteúdo',
        'url_img': 'Imagem',
        'price': 'Preço',
        'button_text': 'Texto Botão',
        'button_link': 'Link Botão',
        'created_at': 'Criação',
        'updated_at': 'Atualização'
    }

    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'title',
        'url_img',
        'body',
        'price',
        'button_text',
        'button_link'
    ]

    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'title',
        'url_img',
        'body',
        'price',
        'button_text',
        'button_link',
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
