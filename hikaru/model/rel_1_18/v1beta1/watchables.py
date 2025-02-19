#
# Copyright (c) 2021 Incisive Technology Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
DO NOT EDIT THIS FILE!

This module is automatically generated using the Hikaru build program that turns
a Kubernetes swagger spec into the code for the hikaru.model package.
"""

from .v1beta1 import *


class Watchables(object):  # pragma: no cover
    """
    Attributes of this class are classes that support watches without the namespace
    keyword argument
    """
    LeaseList = LeaseList
    Lease = Lease
    RoleBindingList = RoleBindingList
    RoleBinding = RoleBinding
    RoleList = RoleList
    Role = Role
    PodSecurityPolicyList = PodSecurityPolicyList
    PodSecurityPolicy = PodSecurityPolicy
    ValidatingWebhookConfigurationList = ValidatingWebhookConfigurationList
    ValidatingWebhookConfiguration = ValidatingWebhookConfiguration
    RuntimeClassList = RuntimeClassList
    RuntimeClass = RuntimeClass
    PodDisruptionBudgetList = PodDisruptionBudgetList
    PodDisruptionBudget = PodDisruptionBudget
    APIServiceList = APIServiceList
    APIService = APIService
    StorageClassList = StorageClassList
    StorageClass = StorageClass
    EndpointSliceList = EndpointSliceList
    EndpointSlice = EndpointSlice
    PriorityClassList = PriorityClassList
    PriorityClass = PriorityClass
    VolumeAttachmentList = VolumeAttachmentList
    VolumeAttachment = VolumeAttachment
    EventList = EventList
    Event = Event
    IngressList = IngressList
    Ingress = Ingress
    CSIDriverList = CSIDriverList
    CSIDriver = CSIDriver
    CSINodeList = CSINodeList
    CSINode = CSINode
    CronJobList = CronJobList
    CronJob = CronJob
    ClusterRoleBindingList = ClusterRoleBindingList
    ClusterRoleBinding = ClusterRoleBinding
    CertificateSigningRequestList = CertificateSigningRequestList
    CertificateSigningRequest = CertificateSigningRequest
    ClusterRoleList = ClusterRoleList
    ClusterRole = ClusterRole
    CustomResourceDefinitionList = CustomResourceDefinitionList
    CustomResourceDefinition = CustomResourceDefinition
    IngressClassList = IngressClassList
    IngressClass = IngressClass
    MutatingWebhookConfigurationList = MutatingWebhookConfigurationList
    MutatingWebhookConfiguration = MutatingWebhookConfiguration


watchables = Watchables


class NamespacedWatchables(object):  # pragma: no cover
    """
    Attributes of this class are classes that support watches with the namespace
    keyword argument
    """
    LeaseList = LeaseList
    RoleBindingList = RoleBindingList
    RoleList = RoleList
    PodDisruptionBudgetList = PodDisruptionBudgetList
    EndpointSliceList = EndpointSliceList
    EventList = EventList
    IngressList = IngressList
    CronJobList = CronJobList
    Lease = Lease
    RoleBinding = RoleBinding
    Role = Role
    PodDisruptionBudget = PodDisruptionBudget
    EndpointSlice = EndpointSlice
    Event = Event
    Ingress = Ingress
    CronJob = CronJob


namespaced_watchables = NamespacedWatchables
