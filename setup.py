from setuptools import find_packages
from setuptools import setup

setup(
    name="film",
    version="0.0.2",
    description="Film interpolation",
    author="Google",
    author_email="tuhin@baseten.co",
    url="https://github.com/tuhins/film",
    packages=find_packages(),
    install_requires=[
        "tensorflow==2.8.0", # The latest should include tensorflow-gpu
        "tensorflow-datasets==4.4.0",
        "tensorflow-addons==0.15.0",
        "absl-py==0.12.0",
        "gin-config==0.5.0",
        "parameterized==0.8.1",
        "mediapy==1.0.3",
        "scikit-image==0.19.1",
        "apache-beam==2.34.0",
        "google-cloud-bigquery-storage==1.1.0",
        "natsort==8.1.0",
        "gdown==4.5.4",
        "tqdm==4.64.1",
    ],
)
