"""empty message

Revision ID: ddf34c35137e
Revises: 2db6ddffefc4
Create Date: 2018-04-27 09:05:57.958849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddf34c35137e'
down_revision = '2db6ddffefc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('likes', sa.Integer(), nullable=True))
    op.drop_constraint(u'posts_user_id_key', 'posts', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'posts_user_id_key', 'posts', ['user_id'])
    op.drop_column('posts', 'likes')
    # ### end Alembic commands ###
