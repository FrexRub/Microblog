"""LikesTweet add UniqueConstraint

Revision ID: 7e147741286b
Revises: 83f3e7b9d796
Create Date: 2024-03-15 17:41:15.258819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e147741286b'
down_revision: Union[str, None] = '83f3e7b9d796'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('idx_unique_user_tweet', 'likes_tweet', ['user_id', 'tweet_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('idx_unique_user_tweet', 'likes_tweet', type_='unique')
    # ### end Alembic commands ###
