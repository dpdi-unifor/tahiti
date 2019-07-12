# -*- coding: utf-8 -*-
"""Convolutional layers adjusts.

Revision ID: f4e270f5197b
Revises: 97a1b6042100
Create Date: 2019-07-10 17:35:36.658472

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
revision = 'f4e270f5197b'
down_revision = '97a1b6042100'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5

VIDEO_READER_OPERATION = 5120
VIDEO_GENERATOR_OPERATION = 5121

CONV3D_FORM = 5150
VIDEO_READER_FORM = 5242
VIDEO_GENERATOR_FORM = 5243
APPEARANCE_FORM = 41

PREPROCESSING_CATEGORY = 5064
INPUT_OUTPUT_CATEGORY = 5065


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer),
        column('css_class', Integer),)

    columns = ('id', 'slug', 'enabled', 'type', 'icon', 'css_class')
    data = [
        (VIDEO_READER_OPERATION, "video-reader", 1, 'ACTION', '', 'circle-layout'),
        (VIDEO_GENERATOR_OPERATION, "video-generator", 1, 'ACTION', '', 'circle-layout'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')
    data = [
        (VIDEO_READER_OPERATION, KERAS_PLATAFORM_ID),
        (VIDEO_GENERATOR_OPERATION, KERAS_PLATAFORM_ID),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (VIDEO_READER_OPERATION, 'en', 'Video reader', 'Reads videos from a '
                                                       'data source.'),
        (VIDEO_GENERATOR_OPERATION, 'en', 'Video generator', 'Takes the dataset'
                                                             ' of videos and '
                                                             'generates batches'
                                                             ' of tensor video '
                                                             'data with real-'
                                                             'time data '
                                                             'augmentation.'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_category_id', 'operation_id')
    data = [
        (INPUT_OUTPUT_CATEGORY, VIDEO_READER_OPERATION),
        (PREPROCESSING_CATEGORY, VIDEO_GENERATOR_OPERATION),
    ]
    rows = [dict(zip(columns, row)) for row in data]
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

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        (5388, 'OUTPUT', '', 2, 'ONE', VIDEO_READER_OPERATION, 'train-video'),
        (5389, 'OUTPUT', '', 1, 'ONE', VIDEO_READER_OPERATION, 'validation-video'),
        (5390, 'INPUT', '', 1, 'ONE', VIDEO_GENERATOR_OPERATION, 'video data'),
        (5391, 'OUTPUT', '', 1, 'MANY', VIDEO_GENERATOR_OPERATION, 'generator'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface():
    tb = table(
        'operation_port_interface',
        column('id', Integer),
        column('color', String))

    columns = ('id', 'color')
    data = [
        (29, '#05E8FA'),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_translation():
    tb = table(
        'operation_port_interface_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (29, 'en', 'VideoData'),
        (29, 'pt', 'VideoData'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (5388, 29),
        (5389, 29),

        (5390, 29),
        (5391, 23),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (5388, 'en', 'train video data', 'Video Data'),
        (5389, 'en', 'validation video data', 'Video Data'),

        (5390, 'en', 'video data', 'Video Data'),
        (5391, 'en', 'generator', 'Generator'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
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
        (VIDEO_READER_FORM, 1, 1, 'execution'),
        (VIDEO_GENERATOR_FORM, 1, 1, 'execution'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (VIDEO_READER_FORM, 'en', 'Execution'),
        (VIDEO_READER_FORM, 'pt', 'Execução'),

        (VIDEO_GENERATOR_FORM, 'en', 'Execution'),
        (VIDEO_GENERATOR_FORM, 'pt', 'Execução'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (VIDEO_READER_OPERATION, APPEARANCE_FORM),
        (VIDEO_READER_OPERATION, VIDEO_READER_FORM),

        (VIDEO_GENERATOR_OPERATION, APPEARANCE_FORM),
        (VIDEO_GENERATOR_OPERATION, VIDEO_GENERATOR_FORM),
    ]

    rows = [dict(zip(columns, row)) for row in data]
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
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')

    LIMONERO_IMAGE = "`${LIMONERO_URL}/datasources?simple=true&list=" \
                     "true&enabled=1&formats=VIDEO_FOLDER`"

    data = [
        # Conv3D
        (5542, 'trainable', 'INTEGER', 0, 8, 0, 'checkbox', None, None,
         'EXECUTION', CONV3D_FORM),

        # video reader
        (5543, 'train_images', 'INTEGER', 1, 1, None, 'lookup', LIMONERO_IMAGE,
         None, 'EXECUTION', VIDEO_READER_FORM),
        (5544, 'validation_images', 'INTEGER', 0, 2, None, 'lookup',
         LIMONERO_IMAGE, None, 'EXECUTION', VIDEO_READER_FORM),

        # video generator
        (5545, 'dimensions', 'TEXT', 1, 1, None, 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),
        (5546, 'channels', 'INTEGER', 1, 2, None, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),
        (5547, 'batch_size', 'INTEGER', 1, 3, None, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),
        (5548, 'steps_per_epoch', 'INTEGER', 1, 4, None, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),
        (5549, 'validation_steps', 'INTEGER', 1, 4, None, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),
        (5550, 'epochs', 'INTEGER', 1, 5, None, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),
        (5551, 'workers', 'INTEGER', 0, 6, 2, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),
        (5552, 'max_queue_size', 'INTEGER', 0, 7, 10, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),
        (5553, 'use_multiprocessing', 'INTEGER', 0, 8, 1, 'checkbox', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM),

    ]
    rows = [dict(zip(columns, row)) for row in data]
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
        # Conv3D
        (5542, 'en', 'Trainable', 'Indicates whether the layer in the model is trainable.'),

        # video reader
        (5543, 'en', 'Training videos', ''),
        (5544, 'en', 'Validation videos', ''),

        # video generator
        (5545, 'en', 'Dimensions', ''),
        (5546, 'en', 'Channels', ''),
        (5547, 'en', 'Batch size', ''),
        (5548, 'en', 'Steps per epoch', ''),
        (5549, 'en', 'Validation steps', ''),
        (5550, 'en', 'Epochs', ''),
        (5551, 'en', 'Workers', ''),
        (5552, 'en', 'Max queue size', ''),
        (5553, 'en', 'Use multiprocessing', ''),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 5120 AND 5121'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 5120 AND 5121'),

    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5120 AND 5121'),

    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE operation_id BETWEEN 5120 AND 5121 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port_interface,
     'DELETE FROM operation_port_interface WHERE id BETWEEN 29 AND 29'),
    (_insert_operation_port_interface_translation,
     'DELETE FROM operation_port_interface_translation WHERE id BETWEEN 29 AND 29'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 5388 AND 5391'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 5388 AND 5391'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 5388 AND 5391'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5242 AND 5243'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5542 AND 5553'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5242 AND 5243'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5542 AND 5553'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id BETWEEN 5120 AND 5121'),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if cmd[0]:
                if isinstance(cmd[0], str):
                    connection.execute(cmd[0])
                elif isinstance(cmd[0], list):
                    for row in cmd[0]:
                        connection.execute(row)
                else:
                    cmd[0]()
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
            if cmd[1]:
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
