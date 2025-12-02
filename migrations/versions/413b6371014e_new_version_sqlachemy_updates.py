"""New version sqlachemy updates

Revision ID: 413b6371014e
Revises: 0ea7185ac58b
Create Date: 2025-11-27 22:27:15.710601

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '413b6371014e'
down_revision = '0ea7185ac58b'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'actions_info',
        'additional_data',
        existing_type=sa.VARCHAR(),
        type_=sa.JSON(),
        existing_nullable=True,
        postgresql_using='additional_data::json',
    )


def downgrade():
    op.alter_column(
        'actions_info',
        'additional_data',
        existing_type=sa.JSON(),
        type_=sa.VARCHAR(),
        existing_nullable=True,
        postgresql_using='additional_data::text',
    )
