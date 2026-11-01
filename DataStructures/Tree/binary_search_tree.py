from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import bst_node as bnode

def new_map():
    return {"root":None}


def put(my_bts, key, value):

    my_bts["root"] = insert_node(my_bts["root"], key, value)
    return my_bts

def insert_node (root, key, value):
    if root is None:
        return bnode.new_node(key, value)
    
    if key > bnode.get_key(root):
        return insert_node(root["right"], key, value)

    elif key < bnode.get_key(root):
        return insert_node(root["left"], key, value)
    else:
        root["value"] = value        
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
        
    return root


def get_node(root, key):
    
    if root is None:
        return None
    
    if key < bnode.get_key(root):
        return get_node(root["left"], key)
    elif key > bnode.get_key(root):
        return get_node(root["right"], key)
    else:   
        return bnode.get_value(root)

def get(my_bst, key):
    
    value = get_node(my_bst["root"], key)
    return value
        
        
def remove (my_bst, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst

def remove_node (root, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    if root is None:
        return None
    
    if key < bnode.get_key(root):
        root["left"] = remove_node(root["left"], key)
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
    elif key > bnode.get_key(root):
        root["right"] = remove_node(root["right"], key)
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
    else:
        if root["right"] is None and root["left"] is None:
            return None
        elif root["right"] is not None and root["left"] is None:
            return root["right"]
        
        elif root["right"] is None and root["left"] is not None:
            return root["left"]
        else:
            menormayores = root["right"]
            while menormayores["left"] is not None:
                menormayores = menormayores["left"]
                
            root["key"] = bnode.get_key(menormayores)
            root["value"] = bnode.get_value(menormayores)
            root["right"] = remove_node(root["right"], bnode.get_key(root))
            root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
            
    return root


def size_tree(root):
    if root is None:
        return 0
    else:
        return size_tree(root["left"]) + size_tree(root["right"]) + 1
    
def size(my_bst):
    return size_tree(my_bst["root"])


def contains(my_bst, key):
    busqueda = get(my_bst, key)
    if busqueda is None:
        return False
    else:
        return True


def is_empty(my_bst):
    booleano = my_bst["root"] is None
    return booleano


def key_set_tree(root, keys):
    if root is not None:
        key_set_tree(root["left"], keys)
        sl.add_last(keys, bnode.get_key(root))
        key_set_tree(root["right"], keys)
        
    return None

def key_set(my_bst):
    keys = sl.new_list()
    key_set_tree(my_bst["root"], keys)
    return keys


def value_set_tree(root, values):
    if root is not None:
        value_set_tree(root["left"], values)
        sl.add_last(values, bnode.get_value(root))
        value_set_tree(root["right"], values)
    return None
        
def value_set(my_bst):
    values = sl.new_list()
    value_set_tree(my_bst["root"], values)
    return values


def get_min_node(root):
    
    raiz = root
    
    while raiz["left"] is not None:
        raiz = raiz["left"]
        
    return bnode.get_key(raiz)

def get_min(my_bst):
    if my_bst["root"] is not None:
        return get_min_node(my_bst["root"])
    
    return None


def get_max_node(root):
    
    raiz = root
    
    while raiz["right"] is not None:
        raiz = raiz["right"]
        
    return bnode.get_key(raiz)

def get_max(my_bst):
    
    if my_bst["root"] is not None:
        return get_max_node(my_bst["root"])
    
    return None
   
    
def delete_min_tree(root):
    if root is not None:
        if root["left"] is None:
            return root["right"]
        
        root["left"] = delete_min_tree(root["left"])
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
        return root
    return None

def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst


def delete_max_tree(root):
    if root is not None:
    
        if root["right"] is None:
            return root["left"]
        
        root["right"] = delete_max_tree(root["right"])
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
        return root
    return None

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst


def height_tree (root):
    
    if root is None:
        return 0
    
    altura_izquierda = height_tree(root["left"])
    altura_derecha = height_tree(root["right"])
    
    return 1 + max(altura_izquierda, altura_derecha)

def height (my_bst):
    
    return height_tree(my_bst["root"])


def floor_key (root, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    if root is None:
        return None
    
    if key == bnode.get_key(root):
        return bnode.get_key(root)
    
    if key < bnode.get_key(root):
        return floor_key(root["left"], key)
    
    elegido = floor_key(root["right"], key)
    if elegido is not None:
        return elegido
    
    return bnode.get_key(root)

def floor (my_bst, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    return floor_key(my_bst["root"], key)


def ceiling_key (root, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    if root is None:
        return None
    
    if key == bnode.get_key(root):
        return bnode.get_key(root)
    
    if key > bnode.get_key(root):
        return floor_key(root["right"], key)
    
    elegido = floor_key(root["right"], key)
    if elegido is not None:
        return elegido
    
    return bnode.get_key(root)

def ceiling (my_bst, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    return floor_key(my_bst["root"], key)


def keys_range (root, key_initial, key_final, list_key):
    
    if root is None:
        return list_key
    
    if key_initial < bnode.get_key(root):
        keys_range(root["left"], key_initial, key_final, list_key)
    
    if key_initial <= bnode.get_key(root) <= key_final:
        sl.add_last(list_key, bnode.get_key(root))
        
    if bnode.get_key(root) < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)
        
    return list_key

def keys (my_bst, key_initial, key_final):
    
    lista_llaves = sl.new_list()
    keys_range(my_bst["root"], key_initial, key_final, lista_llaves)
    
    return lista_llaves 


def values_range (root, key_lo, key_hi, list_values):
    
    if root is None:
        return list_values
    
    if key_lo < bnode.get_key(root):
        values_range(root["left"], key_lo, key_hi, list_values)
        
    if key_lo <= bnode.get_key(root) <= key_hi:
        sl.add_last(list_values, bnode.get_value(root))
        
    if bnode.get_key(root) < key_hi:
        values_range(root["right"], key_lo, key_hi, list_values)
        
    return list_values

def values (my_bst, key_initial, key_final):
    
    lista_valores = sl.new_list()
    values_range(my_bst["root"], key_initial, key_final, lista_valores)
    
    return lista_valores


def select_key (root, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    if root is None:
        return None
    
    tamaño_izquierda = size_tree(root["left"])
    
    if tamaño_izquierda > key:
        return select_key(root["left"], key)
    elif tamaño_izquierda < key:
        return select_key(root["right"], key - (tamaño_izquierda - 1))
    else:
        return root
    
def select (my_bst, pos): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    nodo = select_key(my_bst["root"], pos)
    if nodo is not None:
        return nodo["key"]
    
    return None


def rank_keys (root, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    if root is None:
        return 0
    
    if key <= bnode.get_key(root):
        return rank_keys(root["left"], key)
    
    return 1 + size_tree(root["left"]) + rank_keys(root["right"], key)

def rank (my_bst, key): # No estaba en el laboratorio, pero como estaba en el test, la implementamos por si acaso y para futuros labs.
    
    return rank_keys(my_bst["root"], key)