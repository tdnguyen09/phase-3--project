"""add albums in the table

Revision ID: c33d9874fb62
Revises: a17a728c323b
Create Date: 2024-06-01 22:57:46.877359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c33d9874fb62'
down_revision: Union[str, None] = 'a17a728c323b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
