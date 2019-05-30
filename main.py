import os
import json
import sqlparse

from node import node

TABLES_DIR = './tables'

def print_tables(sql):
    stmt = sqlparse.parse(sql)[0]
    aliases = set()
    print('=' * 5, stmt, '=' * 5)
    for token in stmt.tokens:
        if type(token) == sqlparse.sql.Identifier:
            alias = token.get_alias()
            parent_name = token.get_parent_name()
            real_name = token.get_real_name()
            if parent_name and parent_name not in aliases:
                print(parent_name, real_name)
                aliases.add(alias)
        

def get_from_string(filename):
    with open(os.path.join(TABLES_DIR, filename)) as f:
        obj = json.load(f)
    L = obj['query'].get('L', None)
    if L:
        from_str = L[0]['M']['from']['S']
    else:
        from_str = obj['query']['M']['from']['S']
    return from_str

if __name__ == '__main__':
    miss = 0
    filenames = [filename for filename in os.listdir(TABLES_DIR) if filename.endswith('.json')]
    for filename in filenames:
        try:
            from_str = get_from_string(filename)
            print_tables(from_str)
        except:
            miss += 1
    
    if miss > 0:
        print('Could not read {} files. Formatting error maybe?'.format(miss))