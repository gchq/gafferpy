import re
from codecs import open
from pathlib import Path
from setuptools import setup, find_packages

###############################################################################

name = "gafferpy"
packages = find_packages(where="src")
meta_path = Path("src", "gafferpy", "__init__.py")
keywords = ["class", "attribute", "boilerplate"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
python_requires = ">s3.6"
install_requires = []
extras_require = {
    "requests": ["requests>=2.4.0"],
    "dev": [
        "tox",
        "pytest",
        "requests>=2.4.0",
        "sphinx~=7.2.6",
        "sphinx-rtd-theme~=1.3.0"
    ]
}

###############################################################################

here = Path(__file__).parent


def read(parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with open(here / parts, "rb", "utf-8") as f:
        return f.read()


meta_file = read(meta_path)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        meta_file, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError(f"Unable to find __{meta}__ string.")


version = find_meta("version")
uri = find_meta("uri")

# Get the long description from the README.md file
with open(here / "README.md", encoding="utf-8") as f:
    long = f.read()

setup(
    name=name,
    version=version,
    description=find_meta("description"),
    long_description=long,
    author=find_meta("author"),
    license=find_meta("license"),
    url=uri,
    maintainer=find_meta("author"),
    keywords=keywords,
    packages=packages,
    package_dir={"": "src"},
    zip_safe=False,
    classifiers=classifiers,
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=python_requires,
    py_modules=["gafferpy.gafferpy", "gafferpy.gafferpy_examples", "gafferpy.fishbowl"]
)
