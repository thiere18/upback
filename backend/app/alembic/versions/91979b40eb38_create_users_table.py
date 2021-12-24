"""create users table

Revision ID: 91979b40eb38
Revises: 
Create Date: 2020-03-23 14:53:53.101322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "91979b40eb38"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(100),nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("first_name", sa.String(100)),
        sa.Column("last_name", sa.String(100)),
        sa.Column("address", sa.String(100)),
        sa.Column("hashed_password", sa.String(100), nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False),
        sa.Column("restricted_areas", sa.String(100)),
        sa.Column("permitted_areas",sa.String(100)),
        sa.Column("restricted_sources",sa.String(100)),
        sa.Column("permitted_sources",sa.String(100)),
        sa.Column("restricted_tags", sa.String(100)),
        sa.Column("permitted_tags", sa.String(100)),
        # sa.Column("is_superuser", sa.Boolean, nullable=False),
        sa.Column("role", sa.String(100),nullable=False,server_default=sa.text('user'),),
    )


def downgrade():
    op.drop_table("user")
