import sqlalchemy as sa
from alembic import op


revision = '6b75dd50398f'
down_revision = 'f2d45b6daecf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('actions_info', sa.Column('additional_data', sa.String(), nullable=True))
    op.add_column('user', sa.Column('union_number', sa.String(), nullable=True))
    op.add_column('user', sa.Column('modify_ts', sa.DateTime(), nullable=True))
    op.execute(f'UPDATE "user" SET modify_ts = current_timestamp')
    op.alter_column('user', 'modify_ts', nullable=False)
    op.add_column('user', sa.Column('create_ts', sa.DateTime(), nullable=True))
    op.execute(f'UPDATE "user" SET create_ts = current_timestamp')
    op.alter_column('user', 'create_ts', nullable=False)


def downgrade():
    op.drop_column('user', 'create_ts')
    op.drop_column('user', 'modify_ts')
    op.drop_column('user', 'union_number')
    op.drop_column('actions_info', 'additional_data')
