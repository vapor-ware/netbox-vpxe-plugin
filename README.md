# NetBox vPXE Plugin

A plugin for [NetBox](https://github.com/netbox-community/netbox) that supports vPXE.
vPXE is a system designed to deliver light weight iPXE boot targets to machines and networks that other can't run traditional server provisioning.

## Installing

Since the plugin is published on [PyPI](https://pypi.org/project/netbox-vpxe-plugin/), netbox-vpxe-plugin can be installed via pip

```python
pip install netbox-vpxe-plugin
```

To enable to plugin, add the plugin's name to the `PLUGINS` list in `configuration.py`:

```python
PLUGINS = ['netbox_vpxe_plugin'] # Note that the name here use underscore, not hyphen.
```

Don't forget to restart NetBox to load the new plugin.

You might also have to manually run the database migrations for Netbox to create the appropriate tables.

```bash
python3 manage.py migrate
```

For more information about installing plugins, refer to [NetBox's documentation.](https://netbox.readthedocs.io/en/stable/plugins/)

## Using

## Developing

Plugins are essentially self-contained Django apps which integrate with NetBox to provide custom functionality.
For more information, see [NetBox documentation](https://netbox.readthedocs.io/en/stable/plugins/development/).

## Contributing

If you experience a bug, would like to ask a question, or request a feature, open a new issue and provide as much context as possible.
All contributions, questions, and feedback are welcomed and appreciated.

## License

NetBox vPXE Plugin is licensed under GPLv3.
See [LICENSE](LICENSE) for more info.
