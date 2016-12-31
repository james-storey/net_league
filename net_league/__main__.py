# -*- coding: utf-8 -*-

import net_league

def get_parser():
    parser = argparse.ArgumentParser()
    # TODO: add module cli commands and arguments
    return parser

def main(argv=None):
    parser = get_parser()
    args = parser.parse_args() if argv is None else parser.parse_args(argv)
    # TODO: use argument values

if __name__ == '__main__':
    main()
