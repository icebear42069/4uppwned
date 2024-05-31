from setuptools import setup, find_packages

setup(
   name='drivingrange',
   version='1.0',
   description='Reservation tool for Foreup',
   author='icebear',
   author_email='bytebearllc@gmail.com',
   packages=find_packages('drivingrange'),
   install_requires=['wheel>=0.37.0', 'undetected-chromedriver==3.5.5', 'selenium==4.21.0', 'fake-useragent==1.5.1'],
)
