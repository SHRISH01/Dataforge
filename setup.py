from setuptools import setup, find_packages

# Load the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Dataforge",  
    version="1.0.0", 
    author="Shrish Kamboj",
    author_email="shrishkamboz@gmail.com",
    description="An automated visualization and Feature Engineering tool for datasets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SHRISH01/Dataforge",  
    packages=find_packages(), 
    classifiers=[
        "Development Status :: 3 - Alpha", 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7", 
    install_requires=[
        "pandas>=1.1.0",
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
        "seaborn>=0.11.0",
        "plotly>=5.0.0",
        "scikit-learn>=0.24.0",
    ],
    extras_require={
        "dev": [  
            "pytest>=6.0.0",
            "black>=23.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    include_package_data=True, 
    entry_points={
        "console_scripts": [
            "autoviz=autoviz.cli:main",  
            "featureiq=featureiq.cli:main",  
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/SHRISH01/Dataforge/issues",
        "Source Code": "https://github.com/SHRISH01/Dataforge",
    },
    keywords=[
        "Data Visualization",
        "Feature Engineering",
        "Aata Analysis",
        "Data Science",
        "Machine Learning",
    ],
)
