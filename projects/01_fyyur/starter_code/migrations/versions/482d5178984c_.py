"""empty message

Revision ID: 482d5178984c
Revises: e29e7409b29d
Create Date: 2020-11-08 20:33:32.016792

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '482d5178984c'
down_revision = 'e29e7409b29d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   
    op.add_column('Venue', sa.Column('website',  sa.VARCHAR(length=120), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent',sa.Boolean(), server_default='false'))
    op.add_column('Venue', sa.Column('seeking_description', sa.VARCHAR(length=200), nullable=True))


    op.add_column('Artist', sa.Column('website',  sa.VARCHAR(length=120), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue',sa.Boolean(), server_default='false'))
    op.add_column('Artist', sa.Column('seeking_description', sa.VARCHAR(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###  
    op.drop_column('Venue','website')
    op.drop_column('Venue','seeking_talent')
    op.drop_column('Venue','seeking_description')
    
    op.drop_column('Artist','website')
    op.drop_column('Artist','seeking_venue')
    op.drop_column('Artist','seeking_description')
    # ### end Alembic commands ###
