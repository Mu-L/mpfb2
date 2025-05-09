import bpy, os
from pytest import approx
from .. import dynamic_import
from .. import ObjectService
from .. import NodeService
NodeWrapperMpfbColorRouter2 = dynamic_import("mpfb.entities.nodemodel.v2.composites.nodewrappermpfbcolorrouter2", "NodeWrapperMpfbColorRouter2")

def test_composite_is_available():
    assert NodeWrapperMpfbColorRouter2

def test_composite_can_create_instance():
    node_tree_name = ObjectService.random_name()
    node_tree = NodeService.create_node_tree(node_tree_name)
    node = NodeWrapperMpfbColorRouter2.create_instance(node_tree)
    assert node
    assert node.node_tree.name == "MpfbColorRouter2"
    assert "Group Output" in node.node_tree.nodes
    assert "Math" in node.node_tree.nodes
    assert "Mix" in node.node_tree.nodes
    assert "Group Input" in node.node_tree.nodes
    has_link_to_output = False
    for link in node.node_tree.links:
        if link.to_node.name == "Group Output":
            has_link_to_output = True
    assert has_link_to_output
    node_tree.nodes.remove(node)
    NodeService.destroy_node_tree(node_tree)

def test_composite_validate_tree():
    node_tree_name = ObjectService.random_name()
    node_tree = NodeService.create_node_tree(node_tree_name)
    node = NodeWrapperMpfbColorRouter2.create_instance(node_tree)
    assert NodeWrapperMpfbColorRouter2.validate_tree_against_original_def()
    node_tree.nodes.remove(node)
    NodeService.destroy_node_tree(node_tree)
