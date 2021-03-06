"""empty message

Revision ID: d93bb88f9ab4
Revises: 482d5178984c
Create Date: 2020-11-09 11:13:10.196784

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd93bb88f9ab4'
down_revision = '482d5178984c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue','genres')
    op.drop_column('Artist','genres')
    op.add_column('Artist', sa.Column('genres', sa.ARRAY(sa.String), nullable=False,server_default='{}'))
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String), nullable=False,server_default='{}'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###  
    op.drop_column('Venue','genres')
    op.drop_column('Artist','genres')
    op.add_column('Artist', sa.Column('genres',  sa.VARCHAR(length=120), nullable=False))
    op.add_column('Venue', sa.Column('genres',  sa.VARCHAR(length=120), nullable=False))
    # ### end Alembic commands ###
