"""added slug to port

Revision ID: 3ada503c2991
Revises: 38745782554d
Create Date: 2017-06-08 11:41:45.995039

"""
from alembic import op
import sqlalchemy as sa
from alembic import op
from sqlalchemy import Integer, String
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '3ada503c2991'
down_revision = '38745782554d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operation_port', sa.Column('slug', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###
    op.execute(text(
        ''' UPDATE operation_port, operation_port_translation
            SET operation_port.slug = operation_port_translation.name
            WHERE operation_port_translation.id = operation_port.id '''))
    op.execute(text("""
        UPDATE operation_port_interface_operation_port
        SET operation_port_interface_id = 19
        WHERE operation_port_id IN
            (SELECT id FROM operation_port WHERE operation_id IN
                (26, 35, 68, 69, 70, 71, 81) AND type = 'OUTPUT'
            );"""))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('operation_port', 'slug')

    op.execute(text("""
        UPDATE operation_port_interface_operation_port
        SET operation_port_interface_id = 1
        WHERE operation_port_id IN
            (SELECT id FROM operation_port WHERE operation_id IN
                (35, 68, 69, 70, 71, 81)  AND type = 'OUTPUT'
            );"""))

    # ### end Alembic commands ###
