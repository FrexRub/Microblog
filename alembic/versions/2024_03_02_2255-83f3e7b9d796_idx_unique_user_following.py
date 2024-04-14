"""idx_unique_user_following

Revision ID: 83f3e7b9d796
Revises: a700ddc3716a
Create Date: 2024-03-02 22:55:26.482113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83f3e7b9d796'
down_revision: Union[str, None] = 'a700ddc3716a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('idx_unique_user_following', 'followers', ['user_id', 'following_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('idx_unique_user_following', 'followers', type_='unique')
    # ### end Alembic commands ###
