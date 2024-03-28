# pull official base image
FROM python:3.12-alpine3.19

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install pipenv and project dependencies
RUN pip install -U pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system --deploy --ignore-pipfile

# copy all other fise in wotk direactory
COPY . .

# open by that port
EXPOSE 8000
