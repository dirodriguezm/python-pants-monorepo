FROM python:3.8
ENV PEX_SCRIPT="gunicorn"
COPY app2/app2_pex.pex /app/app.pex
WORKDIR /app
EXPOSE 5000
CMD ["python", "app.pex", "app2.app:app", "-b", "0.0.0.0:5000"]
