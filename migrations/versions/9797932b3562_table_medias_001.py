"""table medias (001)

Revision ID: 9797932b3562
Revises: 738e64986e4f
Create Date: 2020-04-20 08:11:46.465530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9797932b3562'
down_revision = '738e64986e4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medias')
    # ### end Alembic commands ###
