"""No nesessary fields

Revision ID: d1136ec942ac
Revises: e2c2d4fe34f1
Create Date: 2023-03-16 21:31:00.557581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1136ec942ac'
down_revision = 'e2c2d4fe34f1'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('actions_info', 'user_id', existing_type=sa.INTEGER(), nullable=False)
    op.alter_column('actions_info', 'path_from', existing_type=sa.VARCHAR(), nullable=True)


def downgrade():
    op.alter_column('actions_info', 'path_from', existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column('actions_info', 'user_id', existing_type=sa.INTEGER(), nullable=True)
