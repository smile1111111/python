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


class V1ISCSIVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, fs_type=None, iqn=None, iscsi_interface=None, lun=None, read_only=None, target_portal=None):
        """
        V1ISCSIVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fs_type': 'str',
            'iqn': 'str',
            'iscsi_interface': 'str',
            'lun': 'int',
            'read_only': 'bool',
            'target_portal': 'str'
        }

        self.attribute_map = {
            'fs_type': 'fsType',
            'iqn': 'iqn',
            'iscsi_interface': 'iscsiInterface',
            'lun': 'lun',
            'read_only': 'readOnly',
            'target_portal': 'targetPortal'
        }

        self._fs_type = fs_type
        self._iqn = iqn
        self._iscsi_interface = iscsi_interface
        self._lun = lun
        self._read_only = read_only
        self._target_portal = target_portal

    @property
    def fs_type(self):
        """
        Gets the fs_type of this V1ISCSIVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi

        :return: The fs_type of this V1ISCSIVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """
        Sets the fs_type of this V1ISCSIVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi

        :param fs_type: The fs_type of this V1ISCSIVolumeSource.
        :type: str
        """

        self._fs_type = fs_type

    @property
    def iqn(self):
        """
        Gets the iqn of this V1ISCSIVolumeSource.
        Target iSCSI Qualified Name.

        :return: The iqn of this V1ISCSIVolumeSource.
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """
        Sets the iqn of this V1ISCSIVolumeSource.
        Target iSCSI Qualified Name.

        :param iqn: The iqn of this V1ISCSIVolumeSource.
        :type: str
        """
        if iqn is None:
            raise ValueError("Invalid value for `iqn`, must not be `None`")

        self._iqn = iqn

    @property
    def iscsi_interface(self):
        """
        Gets the iscsi_interface of this V1ISCSIVolumeSource.
        Optional: Defaults to 'default' (tcp). iSCSI interface name that uses an iSCSI transport.

        :return: The iscsi_interface of this V1ISCSIVolumeSource.
        :rtype: str
        """
        return self._iscsi_interface

    @iscsi_interface.setter
    def iscsi_interface(self, iscsi_interface):
        """
        Sets the iscsi_interface of this V1ISCSIVolumeSource.
        Optional: Defaults to 'default' (tcp). iSCSI interface name that uses an iSCSI transport.

        :param iscsi_interface: The iscsi_interface of this V1ISCSIVolumeSource.
        :type: str
        """

        self._iscsi_interface = iscsi_interface

    @property
    def lun(self):
        """
        Gets the lun of this V1ISCSIVolumeSource.
        iSCSI target lun number.

        :return: The lun of this V1ISCSIVolumeSource.
        :rtype: int
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """
        Sets the lun of this V1ISCSIVolumeSource.
        iSCSI target lun number.

        :param lun: The lun of this V1ISCSIVolumeSource.
        :type: int
        """
        if lun is None:
            raise ValueError("Invalid value for `lun`, must not be `None`")

        self._lun = lun

    @property
    def read_only(self):
        """
        Gets the read_only of this V1ISCSIVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.

        :return: The read_only of this V1ISCSIVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1ISCSIVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.

        :param read_only: The read_only of this V1ISCSIVolumeSource.
        :type: bool
        """

        self._read_only = read_only

    @property
    def target_portal(self):
        """
        Gets the target_portal of this V1ISCSIVolumeSource.
        iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).

        :return: The target_portal of this V1ISCSIVolumeSource.
        :rtype: str
        """
        return self._target_portal

    @target_portal.setter
    def target_portal(self, target_portal):
        """
        Sets the target_portal of this V1ISCSIVolumeSource.
        iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).

        :param target_portal: The target_portal of this V1ISCSIVolumeSource.
        :type: str
        """
        if target_portal is None:
            raise ValueError("Invalid value for `target_portal`, must not be `None`")

        self._target_portal = target_portal

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
