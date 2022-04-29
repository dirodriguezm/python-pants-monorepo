python_sources()

poetry_requirements(source="../pyproject.toml")
python_requirement(
    name="gunicorn",
    requirements=["gunicorn"],
)

pex_binary(
    name="app",
    dependencies=[":gunicorn", ":app2"]
)

