"""empty message

Revision ID: 7c416c4718a6
Revises: b79390447dcc
Create Date: 2017-03-22 13:14:36.076769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c416c4718a6'
down_revision = 'b79390447dcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ProjectFile',
    sa.Column('ProjectFileId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('ProjectFileId')
    )
    op.create_table('ProjectLog',
    sa.Column('ProjectLogId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('ProjectLogId')
    )
    op.create_table('CommitFile',
    sa.Column('CommitFileId', sa.Integer(), nullable=False),
    sa.Column('ProjectLogId', sa.Integer(), nullable=False),
    sa.Column('ProjectFileId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ProjectFileId'], ['ProjectFile.ProjectFileId'], ),
    sa.ForeignKeyConstraint(['ProjectLogId'], ['ProjectLog.ProjectLogId'], ),
    sa.PrimaryKeyConstraint('CommitFileId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('CommitFile')
    op.drop_table('ProjectLog')
    op.drop_table('ProjectFile')
    # ### end Alembic commands ###
