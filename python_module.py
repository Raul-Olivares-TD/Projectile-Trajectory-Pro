def get_color_prims():
    """Getting the prims of the color node.
    
    :return: Primitives
    :rtype: <hou.Geometry>
    """

    color_node = hou.node(f"{hou.pwd().path()}/prim_colors")
    prims = color_node.geometry().prims()
    
    # Color node primitives
    return prims

    
def get_blast_node():
    """Getting the blast node in HDA.
    
    :return: Blast node
    :rtype: <hou.Node>
    """
    
    blast_node = hou.node(f"{hou.pwd().path()}/show_prims")
    
    #Blast node
    return blast_node

    
def menu():
    """Show the prims by a menu."""
    
    token_list = []
    label_list = []   
    
    for prim in get_color_prims():
        prim_num = str(prim.number())
        token_list.append(prim_num)
        label_list.append(f"Show impact: {prim_num}")
     
    n_type = hou.pwd().type().definition()
    group = n_type.parmTemplateGroup() 
    
    menu = hou.pwd().parm("menu").parmTemplate()
    #Tokens
    menu.setMenuItems(token_list)
    #Labels
    menu.setMenuLabels(label_list)

    group.replace("menu", menu)
    n_type.setParmTemplateGroup(group)
    
    
def visualize_prim():
    """Refresh the menu to see the impact of the selected primitives."""
    
    menu_prim = hou.pwd().parm("menu").evalAsInt()

    for prim in get_color_prims():
        prim_num = prim.number()
        
        if prim_num == menu_prim:
            get_blast_node().parm("group").set(str(prim_num))
            get_blast_node().parm("negate").set(1)
        
        
def show_all_prims():
    """Show the complete trajectory with all prims."""
    
    get_blast_node().parm("group").set(str(""))
    get_blast_node().parm("negate").set(1)