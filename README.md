# Sample ETL project structure

### /config 
all configuration files, like db connections, server credentials, project configurations etc. Usually in yaml

### /src 
all the code, all pipelines

### /utils 
all connectors, notifications, transformations, generators, etc - all staff of that kind.

### /test 
all ETL testing, Unit-testing, integration, etc

### /dwh_version
database versioning (dwh versioning with Alembic in my case)

### run.py
a runner, which accepts parameters and runs specific pipeline or perform specific needs, for example:

`python run.py --script=load_sales --env=dev`


