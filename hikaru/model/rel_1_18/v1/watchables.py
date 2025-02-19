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

from .v1 import *


class Watchables(object):  # pragma: no cover
    """
    Attributes of this class are classes that support watches without the namespace
    keyword argument
    """
    PodList = PodList
    Pod = Pod
    SecretList = SecretList
    Secret = Secret
    ReplicationControllerList = ReplicationControllerList
    ReplicationController = ReplicationController
    ClusterRoleList = ClusterRoleList
    ClusterRole = ClusterRole
    ComponentStatusList = ComponentStatusList
    ComponentStatus = ComponentStatus
    ReplicaSetList = ReplicaSetList
    ReplicaSet = ReplicaSet
    RoleBindingList = RoleBindingList
    RoleBinding = RoleBinding
    APIServiceList = APIServiceList
    APIService = APIService
    ResourceQuotaList = ResourceQuotaList
    ResourceQuota = ResourceQuota
    PersistentVolumeClaimList = PersistentVolumeClaimList
    PersistentVolumeClaim = PersistentVolumeClaim
    PersistentVolumeList = PersistentVolumeList
    PersistentVolume = PersistentVolume
    LeaseList = LeaseList
    Lease = Lease
    NamespaceList = NamespaceList
    Namespace = Namespace
    EndpointsList = EndpointsList
    Endpoints = Endpoints
    LimitRangeList = LimitRangeList
    LimitRange = LimitRange
    ServiceAccountList = ServiceAccountList
    ServiceAccount = ServiceAccount
    NodeList = NodeList
    Node = Node
    CustomResourceDefinitionList = CustomResourceDefinitionList
    CustomResourceDefinition = CustomResourceDefinition
    ClusterRoleBindingList = ClusterRoleBindingList
    ClusterRoleBinding = ClusterRoleBinding
    CSIDriverList = CSIDriverList
    CSIDriver = CSIDriver
    MutatingWebhookConfigurationList = MutatingWebhookConfigurationList
    MutatingWebhookConfiguration = MutatingWebhookConfiguration
    StorageClassList = StorageClassList
    StorageClass = StorageClass
    ServiceList = ServiceList
    Service = Service
    RoleList = RoleList
    Role = Role
    StatefulSetList = StatefulSetList
    StatefulSet = StatefulSet
    EventList = EventList
    Event = Event
    JobList = JobList
    Job = Job
    PodTemplateList = PodTemplateList
    PodTemplate = PodTemplate
    CSINodeList = CSINodeList
    CSINode = CSINode
    HorizontalPodAutoscalerList = HorizontalPodAutoscalerList
    HorizontalPodAutoscaler = HorizontalPodAutoscaler
    DeploymentList = DeploymentList
    Deployment = Deployment
    NetworkPolicyList = NetworkPolicyList
    NetworkPolicy = NetworkPolicy
    VolumeAttachmentList = VolumeAttachmentList
    VolumeAttachment = VolumeAttachment
    ControllerRevisionList = ControllerRevisionList
    ControllerRevision = ControllerRevision
    ConfigMapList = ConfigMapList
    ConfigMap = ConfigMap
    PriorityClassList = PriorityClassList
    PriorityClass = PriorityClass
    DaemonSetList = DaemonSetList
    DaemonSet = DaemonSet
    ValidatingWebhookConfigurationList = ValidatingWebhookConfigurationList
    ValidatingWebhookConfiguration = ValidatingWebhookConfiguration


watchables = Watchables


class NamespacedWatchables(object):  # pragma: no cover
    """
    Attributes of this class are classes that support watches with the namespace
    keyword argument
    """
    PodList = PodList
    SecretList = SecretList
    ReplicationControllerList = ReplicationControllerList
    ReplicaSetList = ReplicaSetList
    RoleBindingList = RoleBindingList
    ResourceQuotaList = ResourceQuotaList
    PersistentVolumeClaimList = PersistentVolumeClaimList
    LeaseList = LeaseList
    EndpointsList = EndpointsList
    LimitRangeList = LimitRangeList
    ServiceAccountList = ServiceAccountList
    ServiceList = ServiceList
    RoleList = RoleList
    StatefulSetList = StatefulSetList
    EventList = EventList
    JobList = JobList
    PodTemplateList = PodTemplateList
    HorizontalPodAutoscalerList = HorizontalPodAutoscalerList
    DeploymentList = DeploymentList
    NetworkPolicyList = NetworkPolicyList
    ControllerRevisionList = ControllerRevisionList
    ConfigMapList = ConfigMapList
    DaemonSetList = DaemonSetList
    Pod = Pod
    Secret = Secret
    ReplicationController = ReplicationController
    ReplicaSet = ReplicaSet
    RoleBinding = RoleBinding
    ResourceQuota = ResourceQuota
    PersistentVolumeClaim = PersistentVolumeClaim
    Lease = Lease
    Endpoints = Endpoints
    LimitRange = LimitRange
    ServiceAccount = ServiceAccount
    Service = Service
    Role = Role
    StatefulSet = StatefulSet
    Event = Event
    Job = Job
    PodTemplate = PodTemplate
    HorizontalPodAutoscaler = HorizontalPodAutoscaler
    Deployment = Deployment
    NetworkPolicy = NetworkPolicy
    ControllerRevision = ControllerRevision
    ConfigMap = ConfigMap
    DaemonSet = DaemonSet


namespaced_watchables = NamespacedWatchables
