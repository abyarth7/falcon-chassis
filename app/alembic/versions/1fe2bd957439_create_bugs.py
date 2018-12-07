"""create bugs

Revision ID: 1fe2bd957439
Revises: 9f9d0e9095cc
Create Date: 2018-12-07 15:24:31.805052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fe2bd957439'
down_revision = '9f9d0e9095cc'
branch_labels = None
depends_on = None


def upgrade():  
    op.create_table(
        'bug',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('bug_tracker_url', sa.String(), nullable=False),
        sa.Column('root_cause', sa.String()),
        sa.Column('who', sa.String()),
        sa.Column('when', sa.DateTime(), default=sa.func.now()))


def downgrade():  
    op.drop_table('bug')
