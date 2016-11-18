from setuptools import setup, find_packages

setup(
    name='git-talk',
    version='0.0.5a0',
    description='Audio & video annotations for your code with Git!',
    long_description=('For more information, visit:'
                      ' https://github.com/sandeepraju/git-talk'),
    author='Team Git Talk',
    author_email='gittalk338@gmail.com',
    license=open('LICENSE', 'r').read(),
    url='https://github.com/sandeepraju/git-talk',
    download_url='https://github.com/sandeepraju/git-talk/archive/master.zip',
    entry_points="""
    [console_scripts]
    gittalk=cli:run
    """,
    include_package_data=True,
    packages=find_packages(),
    py_modules=['cli'],
    install_requires=[
        'httplib2',
        'google-api-python-client',
        'oauth2client'
    ],
    tests_require=[
        'pylint==1.6.4',
    ],
    keywords=[
        'git', 'developer', 'audio', 'video',
        'commentary', 'code', 'github'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 2 - Pre-Alpha',
    ]
)
