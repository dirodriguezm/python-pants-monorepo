pex_binary(
    name="app1_pex",
    entry_point="app1.app:main",
    resolve="app1"
)
docker_image(
    name="app1-docker",
    image_tags=[
        "{build_args.TYPE}",
        "{build_args.TYPE}-{build_args.GIT_COMMIT}",
    ],
    extra_build_args=["GIT_COMMIT", "TYPE"]
)
poetry_requirements(
    name="poetry",
    resolve="app1"
)

python_sources(name="app1",sources=["app1/**/*.py"], resolve="app1")

python_tests(name="app1_tests", resolve="app1", sources=[ "tests/**/*.py" ])
