"""create dim locations

Revision ID: c4eb1c193679
Revises: 
Create Date: 2019-09-01 20:33:35.836533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4eb1c193679'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE TABLE dim_location(
        id INT,
        location_name varchar(127),
        state varchar(64),
        city varchar(127)
    );
    """)


def downgrade():
    op.execute("""DROP TABLE dim_location CASCADE;""")
