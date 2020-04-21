from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField


class MenuItensView(ModelView):

    # Edição através da grid
    column_editable_list = ['description']

    # Colunas excluídas da grid
    column_exclude_list = ['menu_id']

    # Campos da grid utilizado para pesquisa
    column_searchable_list = [
        'description'
    ]

    # Campos utilizados para filtros avançados
    column_filters = [
        'description',
        'url'
    ]

    column_labels = {
        'description': 'Descrição',
        'url': 'URL'
    }

    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'description',
        'url'
    ]

    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'description',
        'url'
    ]
