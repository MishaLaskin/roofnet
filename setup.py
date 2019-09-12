from setuptools import setup


def required_packages():
    deps = [
        'pandas',
        'numpy',
        'matplotlib',
        'torch',
        'torchvision',
        'pillow',
        'seaborn',
    ]


setup(name='roofnet',
      version='0.1',
      description='Code for RoofNet',
      url='http://github.com/MishaLaskin/roofnet',
      author='ML',
      author_email='laskin.misha@gmail.com',
      install_requires=required_packages(),
      license='MIT',
      packages=['roofnet'],
      zip_safe=False)
