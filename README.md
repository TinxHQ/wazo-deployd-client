# wazo-deployd-client

A python client library to access wazo-deployd

## Usage

### Creating a client

```python
from wazo_deployd_client import Client
client = Client('localhost', verify_certificate=False)
```

## Config

```python
client.config.get()
```

## Providers

### List providers

```python
client.providers.list()
client.tenant(tenant_uuid, other_tenant_uuid).providers.list()
```

### Get informations provider

```python
client.providers.list_images()
client.providers.list_locations()
client.providers.list_key_pairs()
client.providers.list_sizes()
client.providers.list_subnets()
client.providers.list_networks()
client.providers.list_regions()
```

### List platforms

```python
client.providers.platforms.list()
```

### Create a provider

```python
client.providers.create(provider_data)
client.tenant(tenant_uuid).providers.create(provider_data)
```

### Get a provider

```python
client.providers.get(provider_uuid)
client.tenant(tenant_uuid).providers.get(provider_uuid)
```

### Update a provider

```python
client.providers.update(provider_uuid, provider_data)
client.tenant(tenant_uuid).providers.update(provider_uuid, provider_data)
```

### Delete a provider

```python
client.providers.delete(provider_uuid)
client.tenant(tenant_uuid).providers.delete(provider_uuid)
```

## Instances

### List instances

```python
client.instances.list(limit=1, offset=1, order='name', direction='desc')
client.tenant(tenant_uuid, other_tenant_uuid).instances.list()

# List by provider
client.instances.list(provider_uuid=provider_uuid)
client.tenant(tenant_uuid).instances.list(provider_uuid=provider_uuid)
```

### Create an instance

```python
client.instances.create(provider_uuid, instance_data)
client.tenant(tenant_uuid).instances.create(provider_uuid, instance_data)
```

### Register an instance

```python
client.instances.register(instance_data)
client.tenant(tenant_uuid).instances.register(instance_data)
```

### Get an instance

```python
client.instances.get(instance_uuid)
client.tenant(tenant_uuid).instances.get(instance_uuid)
```

### Get an instance wazo

```python
client.instances.get_wazo(instance_uuid)
client.tenant(tenant_uuid).instances.get_wazo(instance_uuid)
```

### Pass wizard for an instance

```python
client.instances.wizard(instance_uuid, wizard_data)
client.tenant(tenant_uuid).instances.wizard(instance_uuid, wizard_data)
```

### Update an instance

```python
client.instances.update(instance_uuid, instance_data)
client.tenant(tenant_uuid).instances.update(instance_uuid, instance_data)
```

### Delete an instance

```python
client.instances.delete(provider_uuid, instance_uuid)
client.tenant(tenant_uuid).instances.delete(provider_uuid, instance_uuid)
```

### Unregister an instance

```python
client.instances.unregister(instance_uuid)
client.tenant(tenant_uuid).instances.unregister(instance_uuid)
```

### Register a credential

```python
client.instances.create_credential(instance_uuid, credential_data)
client.tenant(tenant_uuid).instances.create_credential(instance_uuid, credential_data)
```

### Get a credential

```python
client.instances.get_credential(instancr_uuid, credential_uuid)
client.tenant(tenant_uuid).instances.get_credential(instance_uuid, credential_uuid)
```

### Update a credential

```python
client.instances.update_credential(instance_uuid, credential_uuid, credential_data)
client.tenant(tenant_uuid).instances.update_credential(instance_uuid, credential_uuid, credential_data)
```

### Delete a credential

```python
client.instances.delete_credential(instance_uuid, credential_uuid)
client.tenant(tenant_uuid).instances.delete_credential(instance_uuid, credential_uuid)
```

## Debian package

Follow the following steps to build a debian package for wazo-deployd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-deployd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
