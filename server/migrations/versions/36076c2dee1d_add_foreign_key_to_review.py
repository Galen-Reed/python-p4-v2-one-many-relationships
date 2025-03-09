"""add foreign key to Review

Revision ID: 36076c2dee1d
Revises: 335eec094111
Create Date: 2025-03-09 15:07:55.681334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36076c2dee1d'
down_revision = '335eec094111'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
