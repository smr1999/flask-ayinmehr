"""empty message

Revision ID: ff2ba7ed8943
Revises: 94c1061e3d17
Create Date: 2022-08-17 09:34:08.712253

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ff2ba7ed8943'
down_revision = '94c1061e3d17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'content',
               existing_type=mysql.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'content',
               existing_type=mysql.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
