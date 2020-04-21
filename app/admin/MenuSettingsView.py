from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField


class MenuSettingsView(ModelView):

    # Edição através da grid
    column_editable_list = ['description']

    # Colunas excluídas da grid
    column_exclude_list = ['menus_config']

    # Campos da grid utilizado para pesquisa
    column_searchable_list = [
        'description'
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
        'description',
        'created_at',
        'status'
    ]

    column_labels = {
        'description': 'Descrição',
        'created_at': 'Criação',
        'updated_at': 'Atualização'
    }

    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'description',
        'menus_config'
    ]

    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'description',
        'menus_config',
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
