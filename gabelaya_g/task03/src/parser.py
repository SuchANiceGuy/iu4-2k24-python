from dataclasses import dataclass


@dataclass
class Vector:
    x: float
    y: float
    z: float

    @classmethod
    def from_list(cls, nums: list[float]):
        return cls(*nums)

    def to_string(self):
        return f"{self.x:.6f} {self.y:.6f} {self.z:.6f}"


@dataclass
class Node:
    node_id: int
    name: str
    parent_id: int

    @classmethod
    def from_text(cls, text: str):
        tokens = [token.strip() for token in text.split()]
        if len(tokens) != 3:
            raise ValueError(f"Invalid string : {text=}")
        try:
            values = [int(tokens[0]), tokens[1], int(tokens[2])]
        except ValueError:
            raise ValueError(f"Cannot create Node from string: {text=}")
        return cls(*values)

    def to_string(self):
        return f"{self.node_id} {self.name} {self.parent_id}"


@dataclass
class Bone:
    bone_id: int
    position: Vector
    rotation: Vector

    @classmethod
    def from_text(cls, text: str):
        tokens_bone = [float(token.strip()) for token in text.split()]
        if len(tokens_bone) != 7:
            raise ValueError(f"Invalid string: {text=}")
        try:
            values = [int(tokens_bone[0]),
                      Vector.from_list(tokens_bone[1:4]),
                      Vector.from_list(tokens_bone[4:7])]
        except ValueError:
            raise ValueError(f"Can't create Bone from string: {text=}")
        return cls(*values)

    def to_string(self):
        return f"{self.bone_id} {self.position.to_string()} {self.rotation.to_string()}"


@dataclass
class Frame:
    frame_time: int
    bones: list[Bone]

    @classmethod
    def from_file(cls, frame_id: int, bones: list[Bone]):
        return cls(frame_id, bones)

    def to_string(self):
        tokens = [f"  time {self.frame_time}"]
        for bone in self.bones:
            tokens.append(f"    {str(bone.to_string())}")
        return "\n".join(tokens)


def parse_nodes(filepath: str) -> list[Node]:
    nodes = []
    parsing = False
    end_keyword = "end"
    with open(filepath, "rt") as fp:
        for line in fp.readlines():
            if parsing:
                if end_keyword in line:
                    return nodes
                nodes.append(Node.from_text(line.strip()))
            elif "nodes" in line:
                parsing = True
    raise ValueError("Did not met an end")


def parse_frames(filepath: str) -> list[Frame]:
    frames = []
    frame_id = None
    parsing = False
    bones = []
    end_keyword = "end"
    start_keyword = "skeleton"
    with open(filepath, "rt") as fp:
        for line in fp.readlines():
            if parsing:
                if end_keyword in line:
                    frames.append(Frame.from_file(frame_id, bones))
                    return frames
                elif "time" in line:
                    if frame_id is not None:
                        frames.append(Frame.from_file(frame_id, bones))
                    bones = []
                    try:
                        frame_id = int(line.strip().split()[1])
                    except ValueError:
                        raise NameError("Wrong frame: {frame_id=}")
                else:
                    bones.append(Bone.from_text(line.strip()))
            elif start_keyword in line:
                parsing = True
    raise ValueError("Did not met an end")


def parse_file(filepath: str):
    nodes = parse_nodes(filepath)
    frames = parse_frames(filepath)
    return [nodes, frames]
