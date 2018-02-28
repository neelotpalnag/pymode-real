from setuptools import setup

setup(name='py_modevo',
      version='0.1.0',
      packages=['py_modevo'],
      entry_points={
          'console_scripts': [
              'py_modevo = py_modevo.__main__.main'
          ]
      }, install_requires=['py-pareto-gen']
      )
