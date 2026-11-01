from DataStructures.Tree import rbt_node as rn
from DataStructures.List import single_linked_list as sll


def new_map():
    
    return {"root": None, "type": "RBT"}


def default_compare(key, element):
    if key == rn.get_key(element):
        return 0
    elif key > rn.get_key(element):
        return 1
    
    return -1


def size_tree(root):
    if root is None:
        return 0
    
    return root["size"]


def is_red(node_rbt):
    if node_rbt is None:
        return False
    
    return rn.is_red(node_rbt)


def flip_node_color(node_rbt):
    if node_rbt is not None:
        if is_red(node_rbt):
            rn.change_color(node_rbt, rn.BLACK)
        else:
            rn.change_color(node_rbt, rn.RED)
    
    return node_rbt


def flip_colors(node_rbt):
    
    flip_node_color(node_rbt)
    flip_node_color(node_rbt["left"])
    flip_node_color(node_rbt["right"])
    
    return node_rbt


def rotate_left(node_rbt):
    x = node_rbt["right"]
    node_rbt["right"] = x["left"]
    x["left"] = node_rbt

    rn.change_color(x, node_rbt["color"])
    rn.change_color(node_rbt, rn.RED)

    x["size"] = node_rbt["size"]
    node_rbt["size"] = size_tree(node_rbt["left"]) + size_tree(node_rbt["right"]) + 1
    
    return x


def rotate_right(node_rbt):
    x = node_rbt["left"]
    node_rbt["left"] = x["right"]
    x["right"] = node_rbt

    rn.change_color(x, node_rbt["color"])
    rn.change_color(node_rbt, rn.RED)

    x["size"] = node_rbt["size"]
    node_rbt["size"] = size_tree(node_rbt["left"]) + size_tree(node_rbt["right"]) + 1
    
    return x

def insert_node(root, key, value):
    if root is None:
        return rn.new_node(key, value)

    if default_compare(key, root) < 0:
        root["left"] = insert_node(root["left"], key, value)
        
    elif default_compare(key, root) > 0:
        root["right"] = insert_node(root["right"], key, value)
        
    else:
        root["value"] = value

    if is_red(root["right"]) == True and is_red(root["left"]) == False:
        root = rotate_left(root)
        
    if is_red(root["left"]) == True and is_red(root["left"]["left"]) == True:
        root = rotate_right(root)
        
    if is_red(root["left"]) == True and is_red(root["right"]) == True:
        flip_colors(root)

    root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
    
    return root


def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    rn.change_color(my_rbt["root"], rn.BLACK)
    
    return my_rbt

def get_node(root, key):
    if root is None:
        return None
    cmp = default_compare(key, root)
    if cmp < 0:
        return get_node(root["left"], key)
    elif cmp > 0:
        return get_node(root["right"], key)
    else:
        return rn.get_value(root)


def get(my_rbt, key):
    if my_rbt["root"] is None:
        return None
    
    return get_node(my_rbt["root"], key)


def contains(my_rbt, key):
    if my_rbt["root"] is None:
        return False
    
    return get(my_rbt, key) is not None


def size(my_rbt):
    if my_rbt["root"] is None:
        return 0    
    
    return size_tree(my_rbt["root"])

def is_empty(my_rbt):
    return my_rbt["root"] is None


def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        sll.add_last(key_list, rn.get_key(root))
        key_set_tree(root["right"], key_list)
        
    return key_list


def key_set(my_rbt):
    if my_rbt["root"] is None:
        return sll.new_list()
    
    return key_set_tree(my_rbt["root"], sll.new_list())


def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        sll.add_last(value_list, rn.get_value(root))
        value_set_tree(root["right"], value_list)
        
    return value_list


def value_set(my_rbt):
    if my_rbt["root"] is None:
        return sll.new_list()
    
    return value_set_tree(my_rbt["root"], sll.new_list())

def get_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return rn.get_key(root)
    
    return get_min_node(root["left"])


def get_min(my_rbt):
    if my_rbt["root"] is None:
        return None
    
    return get_min_node(my_rbt["root"])


def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return rn.get_key(root)
    
    return get_max_node(root["right"])


def get_max(my_rbt):
    if my_rbt["root"] is None:
        return None
    
    return get_max_node(my_rbt["root"])

def height_tree(root):
    if root is None:
        return 0
    
    return max(height_tree(root["left"]), height_tree(root["right"])) + 1


def height(my_rbt):
    if my_rbt["root"] is None:
        return 0
    
    return height_tree(my_rbt["root"])


def keys_range(root, key_initial, key_final, list_key):
    if root is not None:
        key = rn.get_key(root)
        if key_initial < key:
            keys_range(root["left"], key_initial, key_final, list_key)
        if key_initial <= key <= key_final:
            sll.add_last(list_key, key)
        if key < key_final:
            keys_range(root["right"], key_initial, key_final, list_key)
            
    return list_key


def keys(my_rbt, key_initial, key_final):
    if my_rbt["root"] is None:
        return sll.new_list()
    
    return keys_range(my_rbt["root"], key_initial, key_final, sll.new_list())


def values_range(root, key_initial, key_final, value_list):
    if root is None:
        return value_list
    
    key = rn.get_key(root)
    if key_initial < key:
        values_range(root["left"], key_initial, key_final, value_list)
    if key_initial <= key <= key_final:
        sll.add_last(value_list, rn.get_value(root))
    if key < key_final:
        values_range(root["right"], key_initial, key_final, value_list)
        
def values(my_rbt, key_initial, key_final):
    if my_rbt["root"] is None:
        return sll.new_list()
    
    return values_range(my_rbt["root"], key_initial, key_final, sll.new_list())