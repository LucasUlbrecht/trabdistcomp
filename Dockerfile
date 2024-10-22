#Inicializa o venv e roda o flask

FROM python:3-slim

EXPOSE 5002

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]

#Roda o MySQL
#pfv isso não é final plmdsssss não pense que isso é final
FROM mysql:latest

USER mysql

# Variaveis de ambiente para um user novo
ENV MYSQL_USER=external_user
ENV MYSQL_PASSWORD=password
ENV MYSQL_DATABASE=my_database

# Comandos para dar as permissões necessarias
RUN mysql -u root -p -e "CREATE USER '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
RUN mysql -u root -p -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$MYSQL_USER'@'%';"
RUN mysql -u root -p -e "FLUSH PRIVILEGES;"

EXPOSE 3306

CMD ["mysqld"]