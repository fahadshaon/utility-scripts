import re
import os
import collections

import argparse

COMMENT_LINES = 5
use_rx = re.compile('^USE `(?P<db>.*)`;', flags=re.IGNORECASE)


def list_db(file_path):
    """
    List database in provided database file.

    :param file_path:
    :return: None
    """
    with open(file_path) as f:
        print('Database found - ')
        for l in f:
            ls = l.strip()

            r = use_rx.search(ls)
            if r:
                db = r.group('db')
                print(db)


def extract_db(file_path, db_name, out_dir):
    """
    Extract database sql from a MySQL.sql dump.
    Output is written into `database-name`.sql file.

    :param file_path: .sql file path
    :param db_name: name of the database to extract
    :param out_dir: directory where the extracted database is written.
    :return: None
    """
    last_k = collections.deque()
    flag = False
    out_file = None
    with open(file_path) as in_file:
        for l in in_file:
            ls = l.strip()
            if len(last_k) == COMMENT_LINES:
                prev_line = last_k.popleft()
                if flag:
                    out_file.write(prev_line)

            last_k.append(l)

            r = use_rx.search(ls)
            if not r:
                continue

            if r.group('db') == db_name:
                flag = True
                out_file = open(os.path.join(out_dir, '{}.sql'.format(db_name)), 'wb')
            elif flag:
                flag = False
                if out_file:
                    out_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A python script to extract single database '
                                                 'info from a multi-database MySQL dump')

    subparsers = parser.add_subparsers(help='sub-command help', dest='subparser_name')

    parser_list = subparsers.add_parser('list', help='List all the database in database dump.')
    parser_list.add_argument('file_path', type=str, help='Path to MySQL dump to parse.')
    parser_list.set_defaults(func=list_db)

    parser_extract = subparsers.add_parser('extract', help='Extract a database from mysql dump.')
    parser_extract.add_argument('file_path', type=str, help='Path to MySQL dump to parse.')
    parser_extract.add_argument('database', type=str, help='Database name')
    parser_extract.add_argument('output_dir', type=str, help='Output directory to store extracted file.')
    parser_extract.set_defaults(func=extract_db)

    args = parser.parse_args()
    if args.subparser_name == 'list':
        list_db(args.file_path)
    elif args.subparser_name == 'extract':
        extract_db(args.file_path, args.database, args.out_dir)
    else:
        print('Invalid command')
