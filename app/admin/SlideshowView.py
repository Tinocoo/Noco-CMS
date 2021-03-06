from flask_admin.contrib.sqla import ModelView
from flask_admin.form import ImageUploadField
from wtforms.fields import SelectField
from .Formatters import Formatters



class SlideshowView(ModelView):

    formatters = Formatters()
    
    column_editable_list = ['name']

    column_exclude_list = [
        'title',
        'subtitle',
        'button_text',
        'button_link',
    ]

    # Campos da grid utilizado para pesquisa
    column_searchable_list = [
        'name'
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
        'created_at'
    ]

    column_labels = {
        'name': 'Nome',
        'url_img': 'Imagem',
        'created_at': 'Criação',
        'updated_at': 'Atualização'
    }

    column_formatters = {
        'created_at': formatters._date_format_br,
        'updated_at': formatters._date_format_br,
        'url_img': formatters._list_thumbnail
    }

    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'name',
        'url_img',
        'title',
        'subtitle',
        'button_text',
        'button_link'
    ]
    
    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'name',
        'url_img',
        'title',
        'subtitle',
        'button_text',
        'button_link',
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
    
