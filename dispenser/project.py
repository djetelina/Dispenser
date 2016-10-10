from typing import List

class Project:

    def __init__(self, name: str, version: str, keywords: List[str], dependencies: List[str],
                 python_versions: List[str], short_description: str, path: str, test_suite: str,
                 author: object, url: str, license_name: str):
        self.name = name
        self.version = version
        self.keywords = keywords
        self.dependencies = dependencies
        self.python_versions = python_versions
        self.short_description = short_description
        self.path = path
        self.test_suite = test_suite
        self.url = url
        self.author = author
        self.license_name = license_name
