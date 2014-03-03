
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'This is my first python project',
    'author':'Li Shuo',
    'url':'LATER',
    'download_url':'tell you later',
    'author_email':'hnuiton@gmail.com',
    'version':'0.1'
    'install_requires': ['nose'],
    'packages': ['ex47']
    'scripts':[],
    'name':'firstpythonproject'
}
setup(**config)
