python_sources(name="lib")

poetry_requirements(source="../pyproject.toml")


python_distribution(
    name="dist",
    dependencies=[":lib"],
    provides=python_artifact(
        name="lib1-monorepo",
        version="0.1.4",
    ),
    repositories=["https://test.pypi.org/legacy/"],
)
