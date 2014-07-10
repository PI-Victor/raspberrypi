try:
    import setuptools as s
except ImportError:
    import distutils.core as s

config = {
    'name': 'RaspberryPi',
    'include_package_data': True,
    'version': 'unversioned',
    'author': 'p-victor          ',
    'url': 'http://github.com/p-victor',
    'long_description': open('README.md').read(),
    'zip_safe': False,
    'packages': s.find_packages(),
    'install_requires':[
        'flask',
        'pygal',
        'sqlalchemy'
    ],
}

s.setup(**config)
