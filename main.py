# .travis.yml
config = """
language: python
python:
  - "2.7"
  - "pypy"
  - "3.7"
  - "pypy3"
  
stages: 
  - name: test
  
install:
  - pip install -r requirements.txt
  
script: pytest
"""
