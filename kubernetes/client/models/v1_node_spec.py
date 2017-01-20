# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NodeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, external_id=None, pod_cidr=None, provider_id=None, unschedulable=None):
        """
        V1NodeSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'external_id': 'str',
            'pod_cidr': 'str',
            'provider_id': 'str',
            'unschedulable': 'bool'
        }

        self.attribute_map = {
            'external_id': 'externalID',
            'pod_cidr': 'podCIDR',
            'provider_id': 'providerID',
            'unschedulable': 'unschedulable'
        }

        self._external_id = external_id
        self._pod_cidr = pod_cidr
        self._provider_id = provider_id
        self._unschedulable = unschedulable

    @property
    def external_id(self):
        """
        Gets the external_id of this V1NodeSpec.
        External ID of the node assigned by some machine database (e.g. a cloud provider). Deprecated.

        :return: The external_id of this V1NodeSpec.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this V1NodeSpec.
        External ID of the node assigned by some machine database (e.g. a cloud provider). Deprecated.

        :param external_id: The external_id of this V1NodeSpec.
        :type: str
        """

        self._external_id = external_id

    @property
    def pod_cidr(self):
        """
        Gets the pod_cidr of this V1NodeSpec.
        PodCIDR represents the pod IP range assigned to the node.

        :return: The pod_cidr of this V1NodeSpec.
        :rtype: str
        """
        return self._pod_cidr

    @pod_cidr.setter
    def pod_cidr(self, pod_cidr):
        """
        Sets the pod_cidr of this V1NodeSpec.
        PodCIDR represents the pod IP range assigned to the node.

        :param pod_cidr: The pod_cidr of this V1NodeSpec.
        :type: str
        """

        self._pod_cidr = pod_cidr

    @property
    def provider_id(self):
        """
        Gets the provider_id of this V1NodeSpec.
        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>

        :return: The provider_id of this V1NodeSpec.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """
        Sets the provider_id of this V1NodeSpec.
        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>

        :param provider_id: The provider_id of this V1NodeSpec.
        :type: str
        """

        self._provider_id = provider_id

    @property
    def unschedulable(self):
        """
        Gets the unschedulable of this V1NodeSpec.
        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#manual-node-administration\"

        :return: The unschedulable of this V1NodeSpec.
        :rtype: bool
        """
        return self._unschedulable

    @unschedulable.setter
    def unschedulable(self, unschedulable):
        """
        Sets the unschedulable of this V1NodeSpec.
        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#manual-node-administration\"

        :param unschedulable: The unschedulable of this V1NodeSpec.
        :type: bool
        """

        self._unschedulable = unschedulable

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
