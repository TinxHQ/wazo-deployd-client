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

## Status

```python
client.status.check()
```

## Providers

### List providers

```python
client.providers.list(recurse=True)
client.providers.list(tenant_uuid=tenant_uuid)
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
client.providers.create(provider_data, tenant_uuid=tenant_uuid)
```

### Get a provider

```python
client.providers.get(provider_uuid)
client.providers.get(provider_uuid, tenant_uuid=tenant_uuid)
```

### Update a provider

```python
client.providers.update(provider_uuid, provider_data)
client.providers.update(provider_uuid, provider_data, tenant_uuid=tenant_uuid)
```

### Delete a provider

```python
client.providers.delete(provider_uuid)
client.providers.delete(provider_uuid, tenant_uuid=tenant_uuid)
```

## Instances

### List instances

```python
client.instances.list(limit=1, offset=1, order='name', direction='desc')
client.instances.list(tenant_uuid=tenant_uuid)
client.instances.list()

# List by provider
client.instances.list(provider_uuid=provider_uuid)
client.instances.list(provider_uuid=provider_uuid, tenant_uuid=tenant_uuid)
```

### Create an instance

```python
client.instances.create(provider_uuid, instance_data)
client.instances.create(provider_uuid, instance_data, tenant_uuid=tenant_uuid)
```

### Register an instance

```python
client.instances.register(instance_data)
client.instances.register(instance_data, tenant_uuid=tenant_uuid)
```

### Get an instance

```python
client.instances.get(instance_uuid)
client.instances.get(instance_uuid, tenant_uuid=tenant_uuid)
```

### Get an instance wazo

```python
client.instances.get_wazo(instance_uuid)
client.instances.get_wazo(instance_uuid, tenant_uuid=tenant_uuid)
```

### Update an instance

```python
client.instances.update(instance_uuid, instance_data)
client.instances.update(instance_uuid, instance_data, tenant_uuid=tenant_uuid)
```

### Delete an instance

```python
client.instances.delete(provider_uuid, instance_uuid)
client.instances.delete(provider_uuid, instance_uuid, tenant_uuid=tenant_uuid)
```

### Unregister an instance

```python
client.instances.unregister(instance_uuid)
client.instances.unregister(instance_uuid, tenant_uuid=tenant_uuid)
```

### Register a credential

```python
client.instances.create_credential(instance_uuid, credential_data)
client.instances.create_credential(instance_uuid, credential_data, tenant_uuid=tenant_uuid)
```

### Get a credential

```python
client.instances.get_credential(instancr_uuid, credential_uuid)
client.instances.get_credential(instance_uuid, credential_uuid, tenant_uuid=tenant_uuid)
```

### Update a credential

```python
client.instances.update_credential(instance_uuid, credential_uuid, credential_data)
client.instances.update_credential(instance_uuid, credential_uuid, credential_data, tenant_uuid=tenant_uuid)
```

### Delete a credential

```python
client.instances.delete_credential(instance_uuid, credential_uuid)
client.instances.delete_credential(instance_uuid, credential_uuid, tenant_uuid=tenant_uuid)
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
