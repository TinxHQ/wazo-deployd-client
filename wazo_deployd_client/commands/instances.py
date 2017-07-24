# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import json

from xivo_lib_rest_client import RESTCommand


class InstancesCommand(RESTCommand):

    resource = 'tenants'
    _headers = {'Accept': 'application/json'}

    def list_instances_for_tenant(self, tenant_uuid, provider_uuid=None):
        if provider_uuid:
            url = self._provider_instances_all_url(tenant_uuid, provider_uuid)
        else:
            url = self._instances_all_url(tenant_uuid)

        response = self.session.get(
            url,
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def _create_instance(self, tenant_uuid, instance_data, provider_uuid=None):
        if provider_uuid:
            url = self._provider_instances_all_url(tenant_uuid, provider_uuid)
        else:
            url = self._instances_all_url(tenant_uuid)

        response = self.session.post(
            url,
            data=json.dumps(instance_data),
            headers=self._headers,
        )
        if response.status_code != 201:
            self.raise_from_response(response)

        return response.json()

    def register_instance_for_tenant(self, tenant_uuid, instance_data):
        return self._create_instance(tenant_uuid, instance_data)

    def create_instance_for_tenant(self, tenant_uuid, provider_uuid, instance_data):
        return self._create_instance(tenant_uuid, instance_data, provider_uuid=provider_uuid)

    def get_instance_for_tenant(self, tenant_uuid, instance_uuid):
        response = self.session.get(
            self._instances_one_url(tenant_uuid, instance_uuid),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def update_instance_for_tenant(self, tenant_uuid, instance_uuid, instance_data):
        response = self.session.put(
            self._instances_one_url(tenant_uuid, instance_uuid),
            data=json.dumps(instance_data),
            headers=self._headers,
        )
        if response.status_code != 204:
            self.raise_from_response(response)

    def _delete_instance(self, tenant_uuid, instance_uuid, provider_uuid=None):
        if provider_uuid:
            url = self._provider_instances_one_url(
                tenant_uuid,
                instance_uuid,
                provider_uuid,
            )
        else:
            url = self._instances_one_url(tenant_uuid, instance_uuid)

        response = self.session.delete(
            url,
            headers=self._headers,
        )
        if response.status_code != 204:
            self.raise_from_response(response)

    def unregister_instance_for_tenant(self, tenant_uuid, instance_uuid):
        return self._delete_instance(tenant_uuid, instance_uuid)

    def delete_instance_for_tenant(self, tenant_uuid, provider_uuid, instance_uuid):
        return self._delete_instance(tenant_uuid, instance_uuid, provider_uuid=provider_uuid)

    def _instances_all_url(self, tenant_uuid):
        return '{base_url}/{tenant_uuid}/instances'.format(
            base_url=self.base_url,
            tenant_uuid=tenant_uuid,
        )

    def _instances_one_url(self, tenant_uuid, instance_uuid):
        return '{base_url}/{instance_uuid}'.format(
            base_url=self._instances_all_url(tenant_uuid),
            instance_uuid=instance_uuid,
        )

    def _provider_instances_all_url(self, tenant_uuid, provider_uuid):
        return '{base_url}/{tenant_uuid}/providers/{provider_uuid}/instances'.format(
            base_url=self.base_url,
            tenant_uuid=tenant_uuid,
            provider_uuid=provider_uuid,
        )

    def _provider_instances_one_url(self, tenant_uuid, instance_uuid, provider_uuid):
        return '{base_url}/{instance_uuid}'.format(
            base_url=self._provider_instances_all_url(tenant_uuid, provider_uuid),
            instance_uuid=instance_uuid,
        )
