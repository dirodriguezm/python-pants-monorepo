docker_image(
    name="docker_app2",
    image_tags=[
        "{build_args.TYPE}",
        "{build_args.TYPE}-{build_args.GIT_COMMIT}",
    ],
)
pex_binary(
    name="app2_pex",
    dependencies=[ ":poetry", "app2/app2:app2_source"],
    resolve="app2"
)
poetry_requirements(
    name="poetry",
    resolve="app2"
)

