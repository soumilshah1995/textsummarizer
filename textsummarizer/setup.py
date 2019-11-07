from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="textsummarizer",
    version="1.0.0",
    description="""
    By doing Web Scrapping i am bring a package called  textsummarizer 
     
     what is textsummarizer ?
     Takes a string and return summarized text 
     
     """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/AppleStock",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["textsummarizer"],
    include_package_data=True,
    install_requires=[]
)