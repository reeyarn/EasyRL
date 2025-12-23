# src/easyrl/linkbases/label.py
from dataclasses import dataclass
from ..core.parser import StreamingParser
from ..core.namespaces import NS_LINK, NS_XLINK

@dataclass
class LabelInfo:
    concept: str
    label: str
    documentation: str | None = None

class LabelLinkbaseParser(StreamingParser):
    """Parse label linkbase files for labels and documentation."""
    
    ROLE_DOCUMENTATION = 'http://www.xbrl.org/2003/role/documentation'
    ROLE_LABEL = 'http://www.xbrl.org/2003/role/label'
    
    def parse(self, role: str = ROLE_DOCUMENTATION) -> dict[str, str]:
        """Extract concept -> text mapping for a given role."""
        loc_map: dict[str, str] = {}
        label_map: dict[str, str] = {}
        arcs: list[tuple[str, str]] = []
        
        tags = {f'{NS_LINK}loc', f'{NS_LINK}label', f'{NS_LINK}labelArc'}
        
        for elem in self._iter_elements(tags):
            if elem.tag == f'{NS_LINK}loc':
                self._handle_loc(elem, loc_map)
            elif elem.tag == f'{NS_LINK}label':
                self._handle_label(elem, label_map, role)
            elif elem.tag == f'{NS_LINK}labelArc':
                self._handle_arc(elem, arcs)
        
        return self._resolve(loc_map, label_map, arcs)
    
    def _handle_loc(self, elem, loc_map):
        label = elem.get(f'{NS_XLINK}label')
        href = elem.get(f'{NS_XLINK}href')
        if label and href:
            loc_map[label] = href.split('#')[-1]
    
    # ... other methods