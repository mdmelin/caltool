from setuptools import setup, find_packages

setup(
    name="caltool",
    author="Max Melin",
    author_email="mmelin@ucla.edu",
    description="Python library for lab equipment calibration",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
    ],
    packages=find_packages(where="."),
    package_dir={"": "."},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "caltool = caltool.cli:main",
        ],
    },
    # version could be dynamically retrieved here if needed
    # version="0.0.1"  # Uncomment this or use dynamic approach if necessary
)