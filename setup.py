from setuptools import setup, find_packages


# Lire le contenu de requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='multi_server',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,  # Utiliser la liste des dépendances lue depuis requirements.txt
    entry_points={
        'console_scripts': [
            'multi_server=multi_server.__main__:main',
        ],
    },
)