from parser import Node, Frame


def modificationFile(from_parse: list[list[Node], list[Frame]]) -> list[list[Node], list[Frame]]:
    frames = from_parse[1]
    for frame in frames:
        frame.bones[0].position.x = 0
        frame.bones[0].position.y = 0
        frame.bones[0].position.z = 0
    return from_parse
