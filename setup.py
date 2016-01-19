from setuptools import setup
import string

with open('README.md') as f:
    readme = f.read()
with open('requirements.txt') as f:
    requirements = map(string.strip, open('requirements.txt').readlines())

setup(name='vweb',
      version='1.2.3',
      description='Simple Python Website Frame work',
      long_description=readme,
      url='https://github.com/dlink/vweb',
      author='David Link',
      author_email='dvlink@gmail.com',
      license='GNU General Public License (GPL)',
      packages=['vweb'],
      zip_safe=False,
      install_requires=requirements
)
