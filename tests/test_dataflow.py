#! -*- coding: utf-8 -*-
"""Test Dataflow module provides tests
for the pygoogleanalytics.dataflow DataFlow class
"""
from pygoogleanalytics import dataflow


class TestDataFlow:
    """TestDataFlow class provides methods for testing DataFlow class
    """

    def test_dataflow(self):
        """DataFlow object should have a body attribute
        """

        flow = dataflow.DataFlow(body=['a', 'b', 'c'])
        assert hasattr(flow, 'body')

    def test_init(self):
        """DataFlow body should be a copy of input list at init
        """

        flow = dataflow.DataFlow(body=['a', 'b', 'c'])
        assert flow.list() == ['a', 'b', 'c']

    def test_add(self):
        """DataFlow summation should result in a new DataFlow
        with concatenated body
        """

        left = dataflow.DataFlow(body=['left'])
        right = dataflow.DataFlow(body=['right'])

        assert (left + right).body == ['left', 'right']

    def test_filter(self):
        """DataFlow filtering should behave as the filter base function
        """

        left = dataflow.DataFlow(body=['left'])
        right = dataflow.DataFlow(body=['right'])

        assert (left + right).filter(
            lambda x: x == 'right'
        ).body == filter(
            lambda x: x == 'right',
            (left + right).body
        )

    def test_reduce(self):
        """DataFlow reducing should behave as the reduce base function
        """

        flow = dataflow.DataFlow(body=['a', 'b', 'c'])
        assert flow.reduce(lambda a, b: a + b, '') == reduce(
            lambda a, b: a + b,
            flow.body
        )

    def test_sortby(self):
        """DataFlow sorting should behave as the sorted base function
        """

        flow = dataflow.DataFlow(body=[2, 3, 1])
        assert flow.sortby(lambda x: x).body == sorted(
            flow.body, key=lambda x: x
        )
