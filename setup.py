from setuptools import find_packages, setup

package_name = 'pa_warehouse_status'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AnthonyBebek',
    maintainer_email='anthony@viagi.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pineapple_gossip_bot = pa_warehouse_status.pineapple_gossip_bot:main',
            'gossip_publisher = pa_warehouse_status.talker:main',
            'gossip_PLC = pa_warehouse_status.PLC:main'
        ],
    },
)
