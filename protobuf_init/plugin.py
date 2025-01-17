import logging
import sys
from collections import defaultdict
from google.protobuf.compiler import plugin_pb2 as plugin
from os.path import sep
from pathlib import Path
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


HEADER = "# Generated by protobuf_init. Do not edit manually.\n"


def get_pb2_import_content(filename: str, objects: List[str]) -> str:
    proto_file_name = Path(filename).stem + "_pb2"
    proto_module_name = proto_file_name.replace("-", "_")
    imports = ""
    for obj in objects:
        imports += f"from .{proto_module_name} import {obj}\n"
    return imports


def get_grpcio_import_content(filename: str, objects: List[str]) -> str:
    proto_file_name = Path(filename).stem + "_pb2_grpc"
    proto_module_name = proto_file_name.replace("-", "_")
    grpc_objects = [
        "{obj}Servicer",
        "{obj}Stub",
        "add_{obj}Servicer_to_server",
        "{obj}",
    ]
    imports = ""
    for obj in objects:
        for grpc_obj in grpc_objects:
            objstr = grpc_obj.format(obj=obj)
            imports += f"from .{proto_module_name} import {objstr}\n"
    return imports


def get_grpclib_import_content(filename: str, objects: List[str]) -> str:
    proto_file_name = Path(filename).stem + "_grpc"
    proto_module_name = proto_file_name.replace("-", "_")
    grpc_objects = [
        "{obj}Stub",
        "{obj}Base",
    ]
    imports = ""
    for obj in objects:
        for grpc_obj in grpc_objects:
            objstr = grpc_obj.format(obj=obj)
            imports += f"from .{proto_module_name} import {objstr}\n"
    return imports


def process(
    request: plugin.CodeGeneratorRequest, response: plugin.CodeGeneratorResponse
) -> None:
    # parse the options
    options = request.parameter.split(",") if request.parameter else []
    import_libs = []
    for option in options:
        if option.split("=")[0] == "imports":
            import_libs = option.split("=")[-1].split("+")

    # extract the objects from each file
    assets = defaultdict(lambda: defaultdict(list))
    for proto_file in request.proto_file:
        filename = proto_file.name
        objects = [field.name for field in proto_file.message_type]
        objects += [field.name for field in proto_file.enum_type]
        services = [field.name for field in proto_file.service]
        assets[filename]["objects"] = objects
        assets[filename]["services"] = services

    # build the init files
    files = defaultdict(str)
    for filename, objmap in assets.items():
        content = ""
        for objtype, objects in objmap.items():
            if objtype == "objects" and len(objects) > 0:
                if "protobuf" in import_libs:
                    content += get_pb2_import_content(filename, objects)
            elif objtype == "services" and len(objects) > 0:
                if "grpcio" in import_libs:
                    content += get_grpcio_import_content(filename, objects)
                if "grpclib" in import_libs:
                    content += get_grpclib_import_content(filename, objects)
        if sep not in filename:
            fname = "__init__.py"
        else:
            fname = str(Path(filename).parent / "__init__.py")
        if files[fname] == "":
            files[fname] += HEADER
        files[fname] += content

    # identify any additional empty init files upwards
    init_files = set(files.keys())
    for init_file in init_files:
        path = Path(init_file).parent
        while path != path.parent:
            if str(path / "__init__.py") in init_files:
                path = path.parent
                continue
            else:
                files[str(path / "__init__.py")] = HEADER
            path = path.parent

    # pack up the files
    for f, c in files.items():
        file = response.file.add()
        file.name = f
        file.content = c


def main() -> None:
    value = sys.stdin.buffer.read()
    request = plugin.CodeGeneratorRequest.FromString(value)
    response = plugin.CodeGeneratorResponse()
    process(request, response)
    sys.stdout.buffer.write(response.SerializeToString())


if __name__ == "__main__":
    main()
