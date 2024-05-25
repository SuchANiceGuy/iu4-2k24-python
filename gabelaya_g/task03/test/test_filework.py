import extras
import parser
from types import Node, Frame, Vector, Bone

example_string = "bind \"ins\" \"bot_place\""
example_Node_line = '41 "finger_middle_meta_R" 40'
example_Vector_list = [0.676769, -0.888888, -9.999999]
example_Bone_line = '0 6.296374 0.851588 36.241392 -0.000453 -1.482353 3.047921'
example_Nodes = """  0 "pelvis" -1
  1 "lean_root" -1
  2 "cam_driver" -1
  3 "spine_0" 0
  4 "spine_1" 3
  5 "spine_2" 4
  end
  """


def test_node_builder():
    node1 = Node.from_text(example_Node_line)
    assert node1.node_id == 41
    assert node1.name == '"finger_middle_meta_R"'
    assert node1.parent_id == 40


def test_Vector_builder():
    vector = Vector.from_list(example_Vector_list)
    assert vector.x == 0.676769
    assert vector.y == -0.888888
    assert vector.z == -9.999999


def test_Bone_builder():
    bone = Bone.from_text(example_Bone_line)
    assert bone.bone_id == 0
    assert bone.position == Vector.from_list([6.296374, 0.851588, 36.241392])
    assert bone.rotation == Vector.from_list([-0.000453, -1.482353, 3.047921])


def test_parse_nodes():
    filepath = extras.get_filepath("a_move_c4_runNE.smd")
    assert parser.parse_nodes(filepath)[0] == Node.from_text('0  "pelvis" -1')
