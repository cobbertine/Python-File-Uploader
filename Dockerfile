FROM python:3.8.5-alpine3.11
RUN pip3 install pipenv
WORKDIR ~/PyFiUp/
COPY Pipfile* ./
RUN pipenv install --ignore-pipfile
COPY . .
ENTRYPOINT [ "pipenv", "run", "python3", "PyFiUp.py", "--output", "/docker_mount_uploads" ]