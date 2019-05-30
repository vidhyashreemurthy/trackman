import os
import json
import sqlparse

TABLES_DIR = './tables'

def print_tables(sql):
    stmt = sqlparse.parse(sql)[0]
    aliases = set()
    for token in stmt.tokens:
        if type(token) == sqlparse.sql.Identifier:
            alias = token.get_alias()
            parent_name = token.get_parent_name()
            real_name = token.get_real_name()
            if parent_name and parent_name not in aliases:
                print(parent_name, real_name)
                aliases.add(alias)

if __name__ == '__main__':
    miss = 0
    filenames = [filename for filename in os.listdir(TABLES_DIR) if filename.endswith('.json')]
    for filename in filenames:
        try:
            with open(os.path.join(TABLES_DIR, filename)) as f:
                print(filename)
                from_str = json.load(f)['query']['L'][0]['M']['from']['S']
                print(from_str)
                print_tables(from_str)
                print('=' * 10)
        except:
            miss += 1

    print('Could not read {} files. Formatting error maybe?'.format(miss))