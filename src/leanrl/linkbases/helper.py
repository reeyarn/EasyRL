import xml.etree.ElementTree as ET

# from typing import Dict, List, Set
# from dataclasses import dataclass, field
import xml.etree.ElementTree as ET

# from ..core.namespaces import qname, ArcRoles
# from ..utils import extract_concept_from_href
# from .hierarchy import ConceptNode, ConceptTree

def get_specific_role_tree(memfs, pre_filename, role_keywords):
    """
    Parses the _pre.xml file and extracts the hierarchy ONLY for the presentationLink 
    that matches the role_keywords.
    
    Returns:
        tuple: (root_node, adjacency_map)
        - root_node: The starting concept name (str)
        - adjacency_map: Dict {parent: [children]} ordered by the 'order' attribute
    """
    with memfs.open(pre_filename, 'rb') as f:
        tree = ET.parse(f)
        root_xml = tree.getroot()
    
    # Namespaces usually found in XBRL
    ns = {'xlink': 'http://www.w3.org/1999/xlink'}
    
    target_link = None
    
    # 1. Find the correct presentationLink by Role
    for link in root_xml.findall(".//{http://www.xbrl.org/2003/linkbase}presentationLink"):
        role = link.get('{http://www.w3.org/1999/xlink}role', '').lower()
        
        # Check if ALL keywords exist in the role string
        if all(k in role for k in role_keywords):
            # Exclusion filters (avoid Parentheticals)
            if "parenthetical" not in role:
                target_link = link
                print(f"Found Role: {role}")
                break
    
    if target_link is None:
        return None, None

    # 2. Build the Adjacency List for THIS role only
    # Structure: parent -> list of (order, child)
    adj = {}
    all_children = set()
    all_nodes = set()
    
    # Find all arcs (parent-child relationships)
    for arc in target_link.findall(".//{http://www.xbrl.org/2003/linkbase}presentationArc"):
        parent = arc.get('{http://www.w3.org/1999/xlink}from')
        child = arc.get('{http://www.w3.org/1999/xlink}to')
        order = float(arc.get('order', 1.0))
        
        if parent not in adj:
            adj[parent] = []
        
        adj[parent].append((order, child))
        all_children.add(child)
        all_nodes.add(parent)
        all_nodes.add(child)
    
    # Sort children by order
    for parent in adj:
        adj[parent].sort(key=lambda x: x[0])
        adj[parent] = [x[1] for x in adj[parent]] # Keep just the name
        
    # 3. Find the Root (Node with no parent in this specific graph)
    potential_roots = all_nodes - all_children
    if not potential_roots:
        return None, None
        
    # Usually the root is the one that looks like 'StatementAbstract' or 'IncomeStatementAbstract'
    # Fallback to the first one found
    root = list(potential_roots)[0]
    
    # Prefer a root that ends in 'Abstract' or 'LineItems' if multiple exist
    for r in potential_roots:
        if 'Statement' in r and 'Abstract' in r:
            root = r
            break

    return root, adj