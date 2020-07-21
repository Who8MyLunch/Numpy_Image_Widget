
from setuptools import setup, find_packages

version = '2020.7.21'

setup(
    name='numpy_image_widget',
    packages=find_packages(),
    install_requires=['numpy', 'image_attendant', 'ipyevents', 'ipywidgets'],

    version=version,
    author='Pierre V. Villeneuve',
    author_email='pierre.villeneuve@gmail.com',
    description='An easy-to-use Jupyter widget for displaying images from Numpy data arrays',
    url='https://github.com/who8mylunch/Numpy_Image_Widget',
    license='MIT',
    keywords=['jupyter', 'widget', 'numpy', 'image'],
)
