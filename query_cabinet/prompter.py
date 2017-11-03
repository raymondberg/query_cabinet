import os
import string

class Prompter():
    @classmethod
    def query_description(cls):
        return cls.multi_line_get('Please paste a detailed description of this query: ', '..')

    @classmethod
    def query_group(cls, groups=None):
        if groups is not None:
            print('\nGroups: \n{}\n'.format('t'.join(groups)))
        return input('What is the group of the query? ')

    @classmethod
    def query_name(cls, group_location):
        print('\nQueries: ')
        groups = os.listdir(group_location)
        print('\t'.join(groups))
        print()
        return input('What is the name of the query? ')

    @classmethod
    def query_sql(cls):
        return cls.multi_line_get('Please paste your query template: ')

    @classmethod
    def sql_param_details(cls, template_string):
        params = []
        param_names = [s[1] for s in string.Formatter().parse(template_string) if s[1] is not None]
        for param_name in param_names:
            print('A parameter was detected with the name `{}`'.format(param_name))
            description = input('\tDescribe this parameter? ')
            params.append({'name': param_name, 'description': description})
        return params

    @classmethod
    def resolved_template(cls, statement, params):
        filled_params = {}
        for param_details in params:
            print(param_details['description'])
            name = param_details['name']
            filled_params[name] = input('Enter a value for `{}` > '.format(name))

        return statement.format(**filled_params)

    @classmethod
    def multi_line_get(cls, message, end_character=';'):
        lines = [ input('{} (end with {}) '.format(message, end_character)) ]

        while end_character not in lines[-1]:
            lines.append(input('> '))

        return '\n'.join(lines)

