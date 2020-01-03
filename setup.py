from setuptools import setup, find_packages
setup(
        name="NBCrawler", 
        version="1.0", 
        packges= find_packages(),
        description="Book information crawler using 'NAVER BOOKS API'",
        author="JCHRYS",
        author_email="jchrys@me.com",
        install_requires=["requests",""],
        scripts = [
            ] 
        )
