pex_binary(
    name="app1_pex",
    entry_point="app1.app:main"
)
docker_image(
    name="app1",
    image_tags=[
        "{build_args.TYPE}",
        "{build_args.TYPE}-{build_args.GIT_COMMIT}",
    ],
    extra_build_args=["GIT_COMMIT", "TYPE"]
)
poetry_requirements(
    name="poetry",
)
