from typing import List, Tuple, Dict

class TemplateMap:
    def __init__(self):
        self.template_map: Dict[int, Tuple[int, int, int, int]] = {}

    def add_template(self, question_number: int, coordinates: Tuple[int, int, int, int]):
        self.template_map[question_number] = coordinates

    def get_template(self, question_number: int) -> Tuple[int, int, int, int]:
        return self.template_map.get(question_number)

    def get_all_templates(self) -> List[Tuple[int, int, int, int]]:
        return list(self.template_map.values())

    def clear_templates(self):
        self.template_map.clear()