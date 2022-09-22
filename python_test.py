import json
import random
import pytest
import unittest

def main() -> (dict, dict, dict, dict,dict, ):
    # NOTE: Get all the parse commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        
    parse_commands = []
    for row in data:
        if 'function' in row and row['function'] == 'parse':
            parse_commands.append(row.copy())
    print(f"parse_commands: {parse_commands}")
    
    parse_commands = [row.copy() for row in data if (row['function'] == 'parse' and 'function' in row) ]
    
    # NOTE: Get all the copy commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    copy_commands = []
    for row in data:
        if 'function' in row and row['function'] == 'copy':
            copy_commands.append(row.copy())
    print(f"copy_commands: {copy_commands}")
    
    copy_commands = [row.copy() for row in data if (row['function'] == 'copy' and 'function' in row) ]


    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    functional_commands = []
    counter = 0
    for row in parse_commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    
    functional_commands = [row.copy() row{'_list':'parse'}{'_counter':counter}  for row in parse_commands  ]
    
    counter = 0
    for row in copy_commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'copy'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    
    print(f"functional_commands: {functional_commands}")

    # NOTE: Get random sampling of data
    random_commands = []
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        random_commands = random.sample(data, 2)
    print(f"random_commands: {random_commands}")

    # NOTE: Write the methodology to catch bad_commands
    
    bad_commands = list()
    bad_commands = [None]*3
    
    for row in data:
        if not 'function' in row or not 'value' in row or row['value'] == '':
            return bad_commands.append(row)
        
    bad_commands = [row for row in data if ('function' not in row or 'value' not in 'row' or row.value == '')]
    
    return parse_commands, copy_commands, functional_commands, random_commands, bad_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands, bad_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
    assert len(bad_commands) == 3
    
    
    class TestCases(unittest.TestCase):

        def parse_commands(self):
            self.assertEqual(parse_commands, [{'function': 'parse', 'help': 'file help', 'value': 'file'}])

        def copy_commands(self):
            self.assertEqual(parse_commands, [{'function': 'copy', 'help': 'copy help', 'value': 'file'}])
        
        def functional_commands(self):
            self.assertEqual(parse_commands, [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}])

        def random_commands(self):
            self.assertEqual(len(random_commands),2)
        
        def bad_commands(self):
            self.assertEqual(len(bad_commands),3)

       