"""table testimonials (001)

Revision ID: 80221c4dd517
Revises: 18f5590ea066
Create Date: 2020-04-21 06:28:53.137128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80221c4dd517'
down_revision = '18f5590ea066'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testimonials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('url_img', sa.String(length=255), nullable=True),
    sa.Column('employee_name', sa.String(length=255), nullable=True),
    sa.Column('company_name', sa.String(length=255), nullable=False),
    sa.Column('company_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testimonials')
    # ### end Alembic commands ###
