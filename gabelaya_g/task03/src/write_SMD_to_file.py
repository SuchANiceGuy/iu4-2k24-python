from parser import Node, Frame


def printSmd(from_parse: list[list[Node], list[Frame]]) -> str:
    with open("output.smd", "w") as file:
        nodes = from_parse[0]
        frames = from_parse[1]

        file.write("// Created by Crowbar 0.741\n")
        file.write("version 1\n")
        file.write("nodes\n")
        for node in nodes:
            file.write(f"  {str(node.to_string())}\n")
        file.write("end\n")
        file.write("skeleton\n")
        for frame in frames:
            file.write(f"{str(frame.to_string())}\n")
        file.write("end\n")
