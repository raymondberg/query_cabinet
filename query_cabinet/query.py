import os

import csv
import yaml

from .prompter import Prompter
from .connection import dict_cursor

class Query:
    QUERY_TOP_LEVEL_DIRECTORY = 'queries'

    @staticmethod
    def file_path(query_group, query_name):
        return os.path.join(Query.group_path(query_group), query_name)

    @staticmethod
    def group_path(query_group):
        return os.path.join(Query.QUERY_TOP_LEVEL_DIRECTORY, query_group)

    @classmethod
    def groups(cls):
        return os.listdir(cls.QUERY_TOP_LEVEL_DIRECTORY)

    @classmethod
    def list(cls, group):
        return os.listdir(cls.group_path(group))

    @classmethod
    def build_from_user_input(cls):
        query_group = Prompter.query_group(cls.groups())
        query_name = Prompter.query_name(cls.list(group))
        query_description = Prompter.query_description()
        query_sql = Prompter.query_sql()
        query_params = Prompter.sql_param_details(sql)

        return cls(
            group=query_group,
            name=query_name,
            description=query_description,
            sql=query_sql,
            param_definitions=query_params
        )

    @classmethod
    def load(cls, query_group, query_name):
        if query_group is None:
            query_group = Prompter.query_group(cls.groups())
        if query_name is None:
            query_name = Prompter.query_name(cls.list(query_group))
        with open(cls.file_path(query_group, query_name), 'r') as file:
            data = yaml.load(file.read())
            return cls(
                group=query_group,
                name=query_name,
                description=data['description'],
                sql=data['query'],
                param_definitions=data['query_params']
            )

    def __init__(self, group, name, description, sql, param_definitions):
        self.group = group
        self.name = name
        self.description = description
        self.sql = sql
        self.param_definitions = param_definitions

    @property
    def filename(self):
        return Query.file_path(self.group, self.name)

    def run(self, connection, params=None):
        resolved_statement = Prompter.resolved_template(self.sql, self.param_definitions, params)
        cursor = connection.cursor(cursor_factory=dict_cursor)
        print('Executing query..........', end='')
        cursor.execute(resolved_statement)
        print('COMPLETE')
        return cursor

    def dump_result(self, cursor, output_filepath):
        self.row_count = 0
        with open(output_filepath, 'w') as csvfile:
            initial_result = cursor.fetchone()
            if initial_result:
              self.row_count += 1
              writer = csv.DictWriter(
                      csvfile,
                      fieldnames=dict(initial_result).keys()
              )
              writer.writeheader()
              writer.writerow(initial_result)

              while True:
                  row = cursor.fetchone()
                  if row is None: break

                  writer.writerow(row)
                  self.row_count += 1

    def initialize_group_path(self):
        group_path = self.group_path(self.group)
        if not os.path.isdir(group_path):
            os.mkdir(group_path)

    def save(self):
        self.initialize_group_path()

        contents = {
            'description': self.description,
            'name': self.name,
            'query': self.sql,
            'query_params': self.param_definitions,
        }

        with open(self.file_path(self.group, self.name), 'w') as file:
            file.write(yaml.dump(contents, default_flow_style=False))

