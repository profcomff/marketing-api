"""Init

Revision ID: f2d45b6daecf
Revises:
Create Date: 2022-08-27 00:59:23.669445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2d45b6daecf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user', sa.Column('id', sa.Integer(), nullable=False), sa.PrimaryKeyConstraint('id'))
    op.create_table(
        'actions_info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('action', sa.String(), nullable=False),
        sa.Column('path_from', sa.String(), nullable=False),
        sa.Column('path_to', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('actions_info')
    op.drop_table('user')
