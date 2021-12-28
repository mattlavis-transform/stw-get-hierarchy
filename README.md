# Generate commodity code hierarchy for Single Trade Window CHIEG service

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python3 -m venv venv/`
  `source venv/bin/activate`

- Install necessary Python modules 

  - certifi==2021.5.30
  - chardet==4.0.0
  - idna==2.10
  - psycopg2-binary==2.8.6
  - python-dotenv==0.15.0
  - requests==2.25.1
  - urllib3==1.26.6

  via `pip3 install -r requirements.txt`

## Usage

### To create the extract
`python3 create_stw_hierarchy.py`
