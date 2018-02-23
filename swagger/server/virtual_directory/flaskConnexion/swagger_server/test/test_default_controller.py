# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dir import Dir  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_dir(self):
        """Test case for create_dir

        
        """
        response = self.client.open(
            '/api/dir/{dir_name}'.format(dir_name='dir_name_example'),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dirs_get(self):
        """Test case for dirs_get

        
        """
        response = self.client.open(
            '/api/dirs',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dir_by_id(self):
        """Test case for get_dir_by_id

        
        """
        response = self.client.open(
            '/api/dir/{dir_name}'.format(dir_name='dir_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
