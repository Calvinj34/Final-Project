"""empty message

Revision ID: a0b60521bac9
Revises: 8b7c6885baed
Create Date: 2023-03-09 16:14:39.698893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0b60521bac9'
down_revision = '8b7c6885baed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout', schema=None) as batch_op:
        batch_op.drop_constraint('workout_Equipment_key', type_='unique')
        batch_op.drop_constraint('workout_Location_key', type_='unique')
        batch_op.drop_constraint('workout_Muscle_key', type_='unique')
        batch_op.drop_constraint('workout_Time_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout', schema=None) as batch_op:
        batch_op.create_unique_constraint('workout_Time_key', ['Time'])
        batch_op.create_unique_constraint('workout_Muscle_key', ['Muscle'])
        batch_op.create_unique_constraint('workout_Location_key', ['Location'])
        batch_op.create_unique_constraint('workout_Equipment_key', ['Equipment'])

    # ### end Alembic commands ###
