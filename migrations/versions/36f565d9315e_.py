"""empty message

Revision ID: 36f565d9315e
Revises: 136696c1c8c6
Create Date: 2022-08-22 16:08:11.244532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36f565d9315e'
down_revision = '136696c1c8c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'active')
    # ### end Alembic commands ###