FROM mysql:5.7

ENV MYSQL_DATABASE='db'
ENV MYSQL_PASSWORD='password'

COPY db/mysql_script.sql /docker-entrypoint-initdb.d/

EXPOSE 3306