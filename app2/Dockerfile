FROM python:3.7
ENV PEX_SCRIPT="gunicorn"
COPY app2.app2/app.pex /app/app.pex
WORKDIR /app
EXPOSE 5000
CMD ["./app.pex", "app2.app:app", "-b", "0.0.0.0:5000"]
