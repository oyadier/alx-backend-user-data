#!/usr/bin/env python3
'''Writing logs to file'''
import logging
from typing import List


def filter_datum(fields:List, redaction:str,
                 message: str, seperator:str)-> str:
    
    