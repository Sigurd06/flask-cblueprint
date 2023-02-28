from flask_cblueprint.utils import filesystem

def list_blueprints(blueprints_folder, cb = None) -> list[str]:
    available_blueprints = filesystem.list_directories(blueprints_folder, ["__pycache__", "__boilerplate__"])

    if cb:
        for blueprint_name in available_blueprints:
            cb(blueprint_name)

    return available_blueprints

def list_boilerplate_skeletons(boilerplate_folder) -> list[str]:
    return filesystem.list_directories(boilerplate_folder + "/skeletons")


def list_boilerplate_models(boilerplate_folder) -> list:
    return filesystem.list_files(
        boilerplate_folder + "/models", file_extension="py.template")