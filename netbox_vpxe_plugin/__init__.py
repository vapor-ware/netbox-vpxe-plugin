"""NetBox vPXE Plugin"""

from extras.plugins import PluginConfig


__title__ = 'netbox-vpxe-plugin'
__version__ = '0.1.0'
__description__ = 'NetBox vPXE Plugin'
__author__ = 'Marco Ceppi'
__author_email__ = 'marco@vapor.io'
__url__ = 'https://github.com/vapor-ware/netbox-vpxe-plugin'
__license__ = 'GNU General Public License v3.0'


class VPXEConfig(PluginConfig):
    """This class defines attributes for the NetBox Virtual Circuit Plugin."""

    name = __title__.replace('-', '_')
    verbose_name = 'vPXE'
    description = __description__
    version = __version__
    base_url = 'vpxe'
    author = __author__
    author_email = __author_email__
    required_settings = []
    default_settings = {}
    caching_config = {}


config = VPXEConfig
