from setuptools import setup, find_packages
from koalixcrm.version import KOALIXCRM_VERSION

setup(name='koalix-crm',
      version=KOALIXCRM_VERSION,
      description='koalixcrm is a tiny and easy to use Customer-Relationship-Management'
                  ' Software (CRM) including tiny and easy to use Accounting Software',
      url='http://github.com/scaphilo/koalixcrm',
      author='Aaron Riedener',
      author_email='aaron.riedener@gmail.com',
      license='BSD',
      packages=find_packages(exclude=["projectsettings", "documentation"]),
      install_requires=['Django==3.2.20',
                        'django-filebrowser==3.14.3',
                        'lxml==5.1.0',
                        'olefile==0.46',
                        'Pillow==7.1.2',
                        'psycopg2-binary==2.8.4',
                        'pytz==2022.4',
                        'django-grappelli==2.15.7',
                        'djangorestframework==3.14.0',
                        'djangorestframework-xml==2.0.0',
                        'markdown==3.1.1',
                        'django-filter==23.5',
                        'pandas==1.5.3',
                        'matplotlib==3.7.5'
                        ],
      zip_safe=False,
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 3.10', ],
      python_requires='~=3.5',
      include_package_data=True,
)
