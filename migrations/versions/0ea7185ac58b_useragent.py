"""Useragent

Revision ID: 0ea7185ac58b
Revises: d1136ec942ac
Create Date: 2023-05-05 12:25:03.383848

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '0ea7185ac58b'
down_revision = 'd1136ec942ac'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('user_agent', sa.String(), nullable=True))


def downgrade():
    op.drop_column('user', 'user_agent')
