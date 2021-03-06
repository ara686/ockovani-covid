"""empty message

Revision ID: 0a03ba37cdc3
Revises: aa2c9e377c1b
Create Date: 2021-03-02 20:08:32.237588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a03ba37cdc3'
down_revision = 'aa2c9e377c1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ockovani_registrace',
    sa.Column('datum', sa.Date(), nullable=False),
    sa.Column('ockovaci_misto_id', sa.Unicode(), nullable=False),
    sa.Column('vekova_skupina', sa.Unicode(), nullable=False),
    sa.Column('povolani', sa.Unicode(), nullable=False),
    sa.Column('stat', sa.Unicode(), nullable=False),
    sa.Column('rezervace', sa.Boolean(), nullable=False),
    sa.Column('datum_rezervace', sa.Date(), nullable=False),
    sa.Column('pocet', sa.Integer(), nullable=True),
    sa.Column('import_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['import_id'], ['importy.id'], ),
    sa.ForeignKeyConstraint(['ockovaci_misto_id'], ['ockovaci_mista.id'], ),
    sa.PrimaryKeyConstraint('datum', 'ockovaci_misto_id', 'vekova_skupina', 'povolani', 'stat', 'rezervace', 'datum_rezervace', 'import_id')
    )
    op.create_table('ockovani_rezervace',
    sa.Column('datum', sa.Date(), nullable=False),
    sa.Column('ockovaci_misto_id', sa.Unicode(), nullable=False),
    sa.Column('volna_kapacita', sa.Integer(), nullable=True),
    sa.Column('maximalni_kapacita', sa.Integer(), nullable=True),
    sa.Column('kalendar_ockovani', sa.Unicode(), nullable=False),
    sa.Column('import_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['import_id'], ['importy.id'], ),
    sa.ForeignKeyConstraint(['ockovaci_misto_id'], ['ockovaci_mista.id'], ),
    sa.PrimaryKeyConstraint('datum', 'ockovaci_misto_id', 'kalendar_ockovani', 'import_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ockovani_rezervace')
    op.drop_table('ockovani_registrace')
    # ### end Alembic commands ###
