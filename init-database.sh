#!/bin/bash

set -e

psql -v --username "Webservice" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE web;
EOSQL