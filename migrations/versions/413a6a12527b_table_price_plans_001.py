"""table price_plans (001)

Revision ID: 413a6a12527b
Revises: 80221c4dd517
Create Date: 2020-04-21 12:47:05.403510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '413a6a12527b'
down_revision = '80221c4dd517'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('price_plans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('url_img', sa.String(length=255), nullable=True),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('button_text', sa.String(length=255), nullable=True),
    sa.Column('button_link', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('price_plans')
    # ### end Alembic commands ###