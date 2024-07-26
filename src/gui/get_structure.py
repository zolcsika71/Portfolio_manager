# src/gui/get_structure.py
import logging
import json

logger = logging.getLogger('gui_get_structure')


class GuiStructureLoader:
    def __init__(self, structure_path):
        self.structure_path = structure_path

        logger.info('Module get_structure initialized')
        self.get_gui_structure()

    def load_json(self):
        logger.info('JSON import')
        with open(self.structure_path, 'r') as file:
            return json.load(file)

    def get_gui_structure(self):
        return self.load_json()

# Example usage:
# loader = GuiStructureLoader()
# structure = loader.get_gui_structure()
