"""No foreign key constraint for user

Revision ID: cdb1cd1ef17f
Revises: 6b75dd50398f
Create Date: 2023-03-16 21:02:42.333305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdb1cd1ef17f'
down_revision = '6b75dd50398f'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('actions_info_user_id_fkey', 'actions_info', type_='foreignkey')


def downgrade():
    op.create_foreign_key('actions_info_user_id_fkey', 'actions_info', 'user', ['user_id'], ['id'])
