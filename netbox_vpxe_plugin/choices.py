from utilities.choices import ChoiceSet


class OperatingSystemChoices(ChoiceSet):

    UBUNTU_16_04 = 'xenial'
    UBUNTU_18_04 = 'bionic'
    UBUNTU_20_04 = 'focal'

    WINDOWS_SERVER_2019 = 'win2019'

    TYPE_OTHER = 'other'

    CHOICES = (
        ('Ubuntu', (
            (UBUNTU_16_04, 'Ubuntu 16.04 (Xenial)'),
            (UBUNTU_18_04, 'Ubuntu 16.04 (Bionic)'),
            (UBUNTU_20_04, 'Ubuntu 20.04 (Focal)'),
        )),
        ('Windows', (
            (WINDOWS_SERVER_2019, 'Windows Server 2019'),
        )),
        ('Other', (
            (TYPE_OTHER, 'Other'),
        )),
    )


class BootConfigTypeChoices(ChoiceSet):

    TYPE_PRESEED = 'preseed'
    TYPE_KICKSTART = 'kickstart'

    CHOICES = (
        (TYPE_PRESEED, 'Preseed'),
        (TYPE_KICKSTART, 'Kickstart'),
    )
