#!/usr/bin/env python
import argparse
import jotformlib
import os
import logging
import report


def load_config():
    logging.debug("load_config()")
    return {
    }


def configure_logging(loglevel):
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level)


def run():
    args = parse_args()
    configure_logging(args.loglevel)
    config = load_config()
    client = jotformlib.JotformClient()
    func = getattr(report, "report_{}".format(args.report_name))
    func(client, config)


def parse_args():
    parser = argparse.ArgumentParser()
    reports = [
        'print_zero_submissions',
        'print_all_submissions_to_json',
        'print_all_forms_to_json'
    ]
    parser.add_argument("report_name", choices=report.REPORTS)
    parser.add_argument("--loglevel", default='INFO', choices=['INFO', 'DEBUG'])
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    run()
