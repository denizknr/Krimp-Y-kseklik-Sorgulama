from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="krimp_yukseklik",
    version="0.0.1",
    description="Krimp Yükseklik Sorgulama — ERPNext/Frappe Uygulama Modülü",
    author="denizknr",
    author_email="",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
