
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af8fa7460019'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('chat_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chat_session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('chat_session')
    op.drop_table('chat_message')
