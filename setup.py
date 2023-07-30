import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-end-MLProject-With-MLFlow"
AUTHOR_USER_NAME = 'dasakanksha97'
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "das.akanksha97@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description= "A small python package for ML app",
    long_description= long_description,
    long_description_content = "text/markdown",
    url = f"https://{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
package_dir = {"": "src"},
packages = setuptools.find_packages(where="src")
)