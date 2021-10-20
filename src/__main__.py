import sys
import os
from src.compiler import Compiler


def main():
    assert len(sys.argv) > 2
    main_file = sys.argv[0]
    cwd = os.path.dirname(main_file)[:-4]

    command = sys.argv[1]
    filename = sys.argv[2]

    comp = Compiler()

    if command in ['compile', 'build']:
        if filename.lower().endswith('.py'):
            comp.compile_to_NN(filename)
        else:
            comp.compile_to_Py(filename)
    elif command == 'run':
        assert filename.endswith('.nnpy')
        comp.compile_to_Py(filename)
        filepath = f'{cwd}/{filename[:-5]}.py'
        os.system(f'python {filepath}')
        os.remove(filepath)


if __name__ == '__main__':
    main()
