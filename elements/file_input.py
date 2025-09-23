from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_input_files(self, file: str, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)