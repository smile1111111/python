# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_node_system_info import V1NodeSystemInfo


class TestV1NodeSystemInfo(unittest.TestCase):
    """ V1NodeSystemInfo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NodeSystemInfo(self):
        """
        Test V1NodeSystemInfo
        """
        model = kubernetes.client.models.v1_node_system_info.V1NodeSystemInfo()


if __name__ == '__main__':
    unittest.main()
