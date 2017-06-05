"""empty message

Revision ID: b79390447dcc
Revises: 
Create Date: 2017-03-21 10:41:32.630958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b79390447dcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Main',
    sa.Column('MainId', sa.Integer(), nullable=False),
    sa.Column('Content', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('MainId')
    )
    op.create_table('A',
    sa.Column('AId', sa.Integer(), nullable=False),
    sa.Column('MainId', sa.Integer(), nullable=False),
    sa.Column('Content', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['MainId'], ['Main.MainId'], ),
    sa.PrimaryKeyConstraint('AId')
    )
    op.create_table('B',
    sa.Column('BId', sa.Integer(), nullable=False),
    sa.Column('MainId', sa.Integer(), nullable=False),
    sa.Column('Content', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['MainId'], ['Main.MainId'], ),
    sa.PrimaryKeyConstraint('BId')
    )
    op.create_table('C',
    sa.Column('CId', sa.Integer(), nullable=False),
    sa.Column('MainId', sa.Integer(), nullable=False),
    sa.Column('Content', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['MainId'], ['Main.MainId'], ),
    sa.PrimaryKeyConstraint('CId')
    )
    op.create_table('D',
    sa.Column('DId', sa.Integer(), nullable=False),
    sa.Column('MainId', sa.Integer(), nullable=False),
    sa.Column('Content', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['MainId'], ['Main.MainId'], ),
    sa.PrimaryKeyConstraint('DId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('D')
    op.drop_table('C')
    op.drop_table('B')
    op.drop_table('A')
    op.drop_table('Main')
    # ### end Alembic commands ###