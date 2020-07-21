"""empty message

Revision ID: 985c4943fc33
Revises: 2f553b52d53b
Create Date: 2020-07-21 14:42:05.499139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '985c4943fc33'
down_revision = '2f553b52d53b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('badge_number', sa.String(), nullable=True),
    sa.Column('officer_name', sa.String(), nullable=True),
    sa.Column('parties', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reports')
    # ### end Alembic commands ###
