"""create posts table

Revision ID: 36f3e706c790
Revises: 
Create Date: 2026-07-28 00:17:29.710529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36f3e706c790'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(),nullable=False,primary_key=True), sa.Column('title', sa.String(), nullable=False),sa.Column('content', sa.String(), nullable=False), sa.Column('published', sa.Boolean,nullable=False, server_default='True' ))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
