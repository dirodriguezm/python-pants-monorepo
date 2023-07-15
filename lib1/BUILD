poetry_requirements(
    name="poetry",
    resolve=parametrize("app1", "app2")
)

python_sources(name="lib1", resolve=parametrize("app1", "app2"), sources=["lib1/**/*.py"])
python_tests(name="lib1_tests", resolve=parametrize("app1", "app2"),sources=["tests/**/*.py"])
