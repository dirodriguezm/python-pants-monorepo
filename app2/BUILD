docker_image(
    name="docker_app2",
    image_tags=[
        "{build_args.TYPE}",
        "{build_args.TYPE}-{build_args.GIT_COMMIT}",
    ],
)
pex_binary(
    name="app2_pex",
    dependencies=[ ":poetry", "app2:app2"],
    resolve="app2"
)
poetry_requirements(
    name="poetry",
    resolve="app2"
)

python_sources(name="app2", resolve="app2", sources=["app2/**/*.py"])
python_tests(name="app2_tests", resolve="app2", sources=["tests/**/test*.py"])
