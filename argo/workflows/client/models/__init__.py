# coding: utf-8

# flake8: noqa
"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: 2.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from argo.workflows.client.models.v1alpha1_archive_strategy import V1alpha1ArchiveStrategy
from argo.workflows.client.models.v1alpha1_arguments import V1alpha1Arguments
from argo.workflows.client.models.v1alpha1_artifact import V1alpha1Artifact
from argo.workflows.client.models.v1alpha1_artifact_location import V1alpha1ArtifactLocation
from argo.workflows.client.models.v1alpha1_artifact_repository_ref import V1alpha1ArtifactRepositoryRef
from argo.workflows.client.models.v1alpha1_artifactory_artifact import V1alpha1ArtifactoryArtifact
from argo.workflows.client.models.v1alpha1_artifactory_auth import V1alpha1ArtifactoryAuth
from argo.workflows.client.models.v1alpha1_continue_on import V1alpha1ContinueOn
from argo.workflows.client.models.v1alpha1_dag_task import V1alpha1DAGTask
from argo.workflows.client.models.v1alpha1_dag_template import V1alpha1DAGTemplate
from argo.workflows.client.models.v1alpha1_executor_config import V1alpha1ExecutorConfig
from argo.workflows.client.models.v1alpha1_git_artifact import V1alpha1GitArtifact
from argo.workflows.client.models.v1alpha1_hdfs_artifact import V1alpha1HDFSArtifact
from argo.workflows.client.models.v1alpha1_hdfs_config import V1alpha1HDFSConfig
from argo.workflows.client.models.v1alpha1_hdfs_krb_config import V1alpha1HDFSKrbConfig
from argo.workflows.client.models.v1alpha1_http_artifact import V1alpha1HTTPArtifact
from argo.workflows.client.models.v1alpha1_inputs import V1alpha1Inputs
from argo.workflows.client.models.v1alpha1_metadata import V1alpha1Metadata
from argo.workflows.client.models.v1alpha1_node_status import V1alpha1NodeStatus
from argo.workflows.client.models.v1alpha1_outputs import V1alpha1Outputs
from argo.workflows.client.models.v1alpha1_parameter import V1alpha1Parameter
from argo.workflows.client.models.v1alpha1_pod_gc import V1alpha1PodGC
from argo.workflows.client.models.v1alpha1_raw_artifact import V1alpha1RawArtifact
from argo.workflows.client.models.v1alpha1_resource_template import V1alpha1ResourceTemplate
from argo.workflows.client.models.v1alpha1_retry_strategy import V1alpha1RetryStrategy
from argo.workflows.client.models.v1alpha1_s3_artifact import V1alpha1S3Artifact
from argo.workflows.client.models.v1alpha1_s3_bucket import V1alpha1S3Bucket
from argo.workflows.client.models.v1alpha1_script_template import V1alpha1ScriptTemplate
from argo.workflows.client.models.v1alpha1_sequence import V1alpha1Sequence
from argo.workflows.client.models.v1alpha1_template import V1alpha1Template
from argo.workflows.client.models.v1alpha1_template_ref import V1alpha1TemplateRef
from argo.workflows.client.models.v1alpha1_user_container import V1alpha1UserContainer
from argo.workflows.client.models.v1alpha1_value_from import V1alpha1ValueFrom
from argo.workflows.client.models.v1alpha1_workflow import V1alpha1Workflow
from argo.workflows.client.models.v1alpha1_workflow_list import V1alpha1WorkflowList
from argo.workflows.client.models.v1alpha1_workflow_spec import V1alpha1WorkflowSpec
from argo.workflows.client.models.v1alpha1_workflow_status import V1alpha1WorkflowStatus
from argo.workflows.client.models.v1alpha1_workflow_step import V1alpha1WorkflowStep
from argo.workflows.client.models.v1alpha1_workflow_template import V1alpha1WorkflowTemplate
from argo.workflows.client.models.v1alpha1_workflow_template_list import V1alpha1WorkflowTemplateList
from argo.workflows.client.models.v1alpha1_workflow_template_spec import V1alpha1WorkflowTemplateSpec

from kubernetes.client.models import *
