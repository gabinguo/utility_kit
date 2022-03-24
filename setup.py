from setuptools import setup

setup(
    name="kp_utility",
    version='0.0.1',
    licence="MIT",
    description="tool functions for every project",
    author="Kunpeng GUO",
    author_email="kunpeng.guo@univ-st-etienne.fr",
    url="https://github.com/gabinguo/",
    download_url="https://github.com/gabinguo/utility_kit/releases/download/beta_v1/utility_kit_0.0.2.tar.gz",
    keywords=["script", "anything", "python", "utils_functions"],
    install_requires=[
        "tqdm>=4.60.0",
        "requests==2.25.1",
        "rich>=12.0.1"
    ],
    python_requires=">=3.6.0",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
