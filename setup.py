from setuptools import setup, find_packages

setup(
    name='gittalk',
    version='0.0.1a0',
    description='Audio & video annotations for your code with Git!',
    long_description=('For more information, visit:'
                      ' https://github.com/sandeepraju/git-talk'),
    author='Team Git Talk',
    author_email='whats-our-email@u.northwestern.edu',  # TODO: add a valid email here
    license=open('LICENSE', 'r').read(),
    url='https://github.com/sandeepraju/git-talk',
    download_url='https://github.com/sandeepraju/git-talk/archive/master.zip',
    entry_points="""
    [console_scripts]
    gittalk=cli:run
    """,
    packages=find_packages(),
    py_modules=['cli'],
    install_requires=[
        # TODO: add deps
    ],
    tests_require=[
        'pylint==1.6.4'
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
