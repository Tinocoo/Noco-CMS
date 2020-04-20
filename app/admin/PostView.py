from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField, TextAreaField
from wtforms.widgets import TextArea


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class PostView(ModelView):
    
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    # Edição através da grid
    column_editable_list = ['title']

    # Colunas excluídas da grid
    column_exclude_list = ['description']

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
        'created_at': 'Criação',
        'updated_at': 'Atualização'
    }

    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'title',
        'thumbnail',
        'description',
        'categories',
    ]

    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'title',
        'thumbnail',
        'description',
        'categories',
        'status'
    ]


    form_overrides = {
        'description': CKTextAreaField,
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
