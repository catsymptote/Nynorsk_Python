from src.code_converter import Converter


class Compiler:
    def __init__(self):
        self.converter = Converter()

    def compile_to_NN(self, filename: str):
        assert filename.lower().endswith('.py')
        # Load Python code
        with open(filename, 'r') as f:
            code = f.read()

        # Convert code to nynorsk
        NN_code = self.converter.to_NN(code)

        # Save converted file
        new_filename = filename[:-3] + '.nnpy'
        with open(new_filename, 'w') as f:
            f.write(NN_code)

    def compile_to_Py(self, filename: str):
        assert filename.lower().endswith('.nnpy')
        # Load Python code
        with open(filename, 'r') as f:
            code = f.read()

        # Convert code to nynorsk
        Py_code = self.converter.to_Py(code)

        # Save converted file
        new_filename = filename[:-5] + '.py'
        with open(new_filename, 'w') as f:
            f.write(Py_code)
