from setuptools import find_packages,setup

setup(
    name='medical-onco',
    version='0.0.1',
    author='vikash',
    author_email='vikashkumar.evolve@gmail.com',
    install_requires=["pypdf","langchain","torch","accelerate","bitsandbytes","transformers",
                      "sentence_transformers","faiss_cpu","chainlit","huggingface_hub"],
    packages=find_packages()
)