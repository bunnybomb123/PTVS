from typing import Any

class Node:
    tag = ...  # type: Any
    value = ...  # type: Any
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    def __init__(self, tag, value, start_mark, end_mark) -> None: ...

class ScalarNode(Node):
    id = ...  # type: Any
    tag = ...  # type: Any
    value = ...  # type: Any
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    style = ...  # type: Any
    def __init__(self, tag, value, start_mark=..., end_mark=..., style=...) -> None: ...

class CollectionNode(Node):
    tag = ...  # type: Any
    value = ...  # type: Any
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    flow_style = ...  # type: Any
    def __init__(self, tag, value, start_mark=..., end_mark=..., flow_style=...) -> None: ...

class SequenceNode(CollectionNode):
    id = ...  # type: Any

class MappingNode(CollectionNode):
    id = ...  # type: Any
