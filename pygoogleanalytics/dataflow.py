#! -*- coding: utf-8 -*-
"""Dataflow module provides DataFlow class implementing functional methods
over a core immutable container and public functions to build Dataflow objects
from raw google analytics response
"""

from collections import namedtuple


def from_response(raw_response):
    """Google Analytics API specific function
    Converts raw_response dict into list of namedtuple

    Args:
        `raw_response`  (dict)  dict representation
            of Google Analytics API Response

    Returns:
        list: list of namedtuple representing flattened response data
    """

    RawData = namedtuple('RawData', [
        _.replace(':', '_').lower()
        for _ in raw_response['reports'][0]['columnHeader']['dimensions']
    ] + [
        _['name'].replace(':', '_').lower()
        for _ in raw_response['reports'][0]['columnHeader']['metricHeader'][
            'metricHeaderEntries'
        ]
    ])

    body = [
        RawData(*(
            x.encode('utf-8')
            for x in _['dimensions'] + _['metrics'][0]['values']
        ))
        for _ in raw_response['reports'][0]['data']['rows']
    ] if 'rows' in raw_response['reports'][0]['data'] else []

    return body


def flow_maker(raw_response):
    """Build DataFlow object from Google Analytics API response
    using from_response function
    """

    return DataFlow(**from_response(raw_response))


class DataFlow(object):
    """DataFlow class provides a container with functional methods
    """

    def __init__(self, body):
        """Assign `body` as internal container

        Args:
            `body`  (list): list-like container
        """

        self.body = body

    def __add__(self, other):
        """Define `+` operator for DataFlow class as concatenation operator

        Args:
            `other` (DataFlow): object with which to concatenate `self`

        Returns:
            DataFlow: new DataFlow, concatenation of `self` and `other`
        """

        return DataFlow(self.body + other.body)

    def __iadd__(self, other):
        """Define `+=` operator for DataFlow class as concatenation operator

        Args:
            `other` (DataFlow): object with which to concatenate `self`

        Returns:
            DataFlow: new DataFlow, concatenation of `self` and `other`
        """

        return self + other

    def filter(self, f):
        """Define filter chain method

        Args:
            `f` (lambda x: True|False) one to bool function

        Returns:
            DataFlow: new DataFlow with `body` filter by `f`
        """

        return DataFlow(filter(f, self.body))

    def list(self):
        """Convert DataFlow object to list

        Returns:
            DataFlow.body: as list of object
        """

        return list(self.body)

    def map(self, f):
        """Define map chain method

        Args:
            `f` (lambda x: y) one to one function

        Returns:
            DataFlow: new DataFlow with `body` mapped over with `f`
        """

        return DataFlow(map(f, self.body))

    def reduce(self, f, initial_value=None):
        """Define reduce operation

        Args:
            `f`             (lambda a, b: c)    many to one function
            `initial_value` (object)            initial value for
                                                reducing operation

        Returns:
            object: reducing result
        """

        return reduce(f, self.body, initial_value)

    def sortby(self, f):
        """Define sortby chain method

        `f` extract from each `body` element the key used to sort elements

        Args:
            `f` (lambda x: y) one to one function

        Returns:
            DataFlow: new DataFlow sorted with key function `f`
        """

        return DataFlow(sorted(self.body, key=f))

    def __repr__(self):
        """Convert DataFlow to str

        Returns:
            str: string representation of DataFlow
        """

        return '\n'.join(
            repr(_) for _ in self.body
        )
