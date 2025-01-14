FROM postgres:15

# Install extensions
RUN apt-get update \
    && apt-get install -y postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*

# Custom PostgreSQL configuration
COPY postgresql.conf /etc/postgresql/postgresql.conf

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"] 