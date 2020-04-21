from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from wtforms.fields import SelectField
from .CKTextArea import CKTextAreaField


class TestimonialsView(ModelView):
    
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    # Edição através da grid
    column_editable_list = ['title']

    # Colunas excluídas da grid
    column_exclude_list = [
        'content',
        'url_img',
        'employee_name',
        'company_url'
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
        'content': 'Texto',
        'url_img': 'Imagem',
        'company_name': 'Empresa',
        'employee_name': 'Funcionário',
        'company_url': 'Site',
        'created_at': 'Criação',
        'updated_at': 'Atualização'
    }

    # Campos que serão apresentados na tela de cadastro
    form_create_rules = [
        'title',
        'content',
        'url_img',
        'company_name',
        'employee_name',
        'company_url'
    ]

    # Campos que serão apresentados na tela de edição
    form_edit_rules = [
        'title',
        'content',
        'url_img',
        'company_name',
        'employee_name',
        'company_url',
        'status'
    ]

    form_overrides = {
        'content': CKTextAreaField,
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
