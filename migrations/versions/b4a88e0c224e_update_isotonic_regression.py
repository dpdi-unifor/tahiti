# -*- coding: utf-8 -*-

"""Update isotonic regression

Revision ID: b4a88e0c224e
Revises: 3e10f106043c
Create Date: 2019-10-14 17:13:12.586484

"""

from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json


# revision identifiers, used by Alembic.
revision = 'b4a88e0c224e'
down_revision = '3e10f106043c'
branch_labels = None
depends_on = None

ISOTONIC_ID = 4046
ISOTONIC_FORM = 4045
MODEL_PORT = 9999
INPUT_PORT = 9999
OUTPUT_PORT = 9999


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (ISOTONIC_ID, "isotonic-regression-model", 1, "TRANSFORMATION",
         "fa-battery-quarter"),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_new_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (ISOTONIC_ID, 4),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )
    columns = [c.name for c in tb.columns]
    data = [
        # Regression
        (ISOTONIC_ID, "en", "Isotonic Regression", "Isotonic Regression"),
        (ISOTONIC_ID, "pt", "Regressão Isotônica", "Regressão Isotônica"),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        (ISOTONIC_ID, 4),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('order', Integer),
        column('multiplicity', String),
        column('operation_id', Integer),
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (INPUT_PORT, "INPUT", None, 1, "ONE", ISOTONIC_ID, "train input data"),
        (MODEL_PORT, "OUTPUT", None, 2, "MANY", ISOTONIC_ID, "model"),
        (OUTPUT_PORT, "OUTPUT", None, 1, "MANY", ISOTONIC_ID, "output data"),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (INPUT_PORT, "pt", "entrada do treino", "Train input data"),
        (MODEL_PORT, "pt", "modelo", "Output model"),
        (OUTPUT_PORT, "pt", "dados de saída", "Dados de saída"),
        (INPUT_PORT, "en", "train input data", "Train input data"),
        (MODEL_PORT, "en", "model", "Output model"),
        (OUTPUT_PORT, "en", "output data", "Output data"),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    data = [
        (INPUT_PORT, 1),
        (MODEL_PORT, 2),
        (OUTPUT_PORT, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]

    # Regression
    data = [
        (ISOTONIC_ID, 1),
        (ISOTONIC_ID, 21),
        (ISOTONIC_ID, 8),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        (ISOTONIC_FORM, 1, 1, 'execution'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (ISOTONIC_FORM, 'en', 'Execution'),
        (ISOTONIC_FORM, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        [ISOTONIC_ID, ISOTONIC_FORM],
        [ISOTONIC_ID, 41],
        [ISOTONIC_ID, 110],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field():
    tb = table(
        'operation_form_field',
        column('id', Integer),
        column('name', String),
        column('type', String),
        column('required', Integer),
        column('order', Integer),
        column('default', Text),
        column('suggested_widget', String),
        column('values_url', String),
        column('values', String),
        column('scope', String),
        column('form_id', Integer),
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    data = [

        # Flatten - data_format
        (245, 'y_min', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION',
         ISOTONIC_FORM, None),
        (248, 'y_max', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION',
         ISOTONIC_FORM, None),
        (487, 'out_of_bounds', 'TEXT', 0, 3, "nan", 'dropdown', None,
         json.dumps([
             {"key": "nan", "value": "nan"},
             {"key": "clip", "value": "clip"},
             {"key": "raise", "value": "raise"}
         ]),
         'EXECUTION', ISOTONIC_FORM, None),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        # Flatten - data_format
        (245, 'en', 'Y min', 'Y min.'),
        (245, 'pt', 'Y min', 'Y min.'),

        (248, 'en', 'Y max', 'Y max.'),
        (248, 'pt', 'Y max', 'Y max.'),

        (487, 'en', 'Out of bounds', 'Out of bounds.'),
        (487, 'pt', 'Out of bounds', 'Out of bounds.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = {}'.format(ISOTONIC_ID)),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(ISOTONIC_ID)),
    (_insert_new_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = {}'
     .format(ISOTONIC_ID)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id = {}'.format(ISOTONIC_ID)),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = {}'.format(ISOTONIC_FORM)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = {}'
     .format(ISOTONIC_FORM)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id = {}'.format(ISOTONIC_ID)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id IN ({}, {}, {})'
     .format(INPUT_PORT, OUTPUT_PORT, MODEL_PORT)),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN ({}, {}, {})'
     .format(INPUT_PORT, OUTPUT_PORT, MODEL_PORT)),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE '
     'operation_port_id IN ({}, {}, {})'
     .format(INPUT_PORT, OUTPUT_PORT, MODEL_PORT)),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN ?? AND ??;'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN ?? AND ??;'),

]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()

