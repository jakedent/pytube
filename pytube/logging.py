# -*- coding: utf-8 -*-
"""This module implements a log factory."""
from __future__ import absolute_import

import logging


def create_logger(level=logging.ERROR):
    """Create a configured instance of logger.

    :param int level:
        Describe the severity level of the logs to handle.
    """
    fmt = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    date_fmt = '%H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # https://github.com/nficano/pytube/issues/163
    try:
        logger = logging.getLogger('pytube')
        logger.addHandler(handler)
        logger.setLevel(level)
        return logger
    except Exception as l:
        logging.exception('Exception on Handler: {0}'.format(l))
