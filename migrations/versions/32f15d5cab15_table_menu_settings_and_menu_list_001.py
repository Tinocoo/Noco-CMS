"""table menu_settings and menu_list (001)

Revision ID: 32f15d5cab15
Revises: 413a6a12527b
Create Date: 2020-04-21 14:38:46.811291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32f15d5cab15'
down_revision = '413a6a12527b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('menu_lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=False),
    sa.Column('menu_id', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['menu_id'], ['menu_settings.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu_lists')
    op.drop_table('menu_settings')
    # ### end Alembic commands ###
