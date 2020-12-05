import os
import subprocess
import tempfile


def _create_files(suffix: str) -> tuple:
    """
    :param suffix: string
    :return: Input, Code and Output File Name and Descriptor
    :rtype: tuple
    """
    input_file_descriptor, input_file_name = tempfile.mkstemp(dir='./api/temp')
    code_file_descriptor, code_file_name = tempfile.mkstemp(dir='./api/temp', suffix=suffix)
    output_file_descriptor, output_file_name = tempfile.mkstemp(dir='./api/temp')
    return input_file_descriptor, input_file_name, code_file_descriptor, code_file_name, output_file_descriptor, output_file_name


def python(code: str, input_string: str) -> str:
    """
    :param code: string
    :param input_string: string
    :return: Output of the code.
    """

    input_file_descriptor, input_file_name, code_file_descriptor, code_file_name, output_file_descriptor, output_file_name = _create_files(
        '.py')
    output = ""
    try:
        with os.fdopen(input_file_descriptor, 'w+') as fh:
            fh.write(input_string)
        with os.fdopen(code_file_descriptor, 'w+') as fh:
            fh.write(code)

        command = f'cat {input_file_name} | python3 {code_file_name} > {output_file_name} 2>&1'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=15)

        with os.fdopen(output_file_descriptor, 'r+') as fh:
            output = fh.read()

    except subprocess.TimeoutExpired:
        output = "TLE (15s)."
    except Exception as e:
        output = e.__class__

    finally:
        os.remove(input_file_name)
        os.remove(code_file_name)
        os.remove(output_file_name)
        return output


def java(code: str, input_string: str) -> str:
    """
    :param code: string
    :param input_string: string
    :return: Output of the code.
    """
    input_file_descriptor, input_file_name, code_file_descriptor, code_file_name, output_file_descriptor, output_file_name = _create_files(
        '.java')
    output = ""
    try:
        with os.fdopen(input_file_descriptor, 'w+') as fh:
            fh.write(input_string)
        with os.fdopen(code_file_descriptor, 'w+') as fh:
            fh.write(code)

        command = f'cat {input_file_name} | java {code_file_name} > {output_file_name} 2>&1'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=15)

        with os.fdopen(output_file_descriptor, 'r+') as fh:
            output = fh.read()

    except subprocess.TimeoutExpired:
        output = "TLE (15s)."
    except Exception as e:
        output = e.__class__

    finally:
        os.remove(input_file_name)
        os.remove(code_file_name)
        os.remove(output_file_name)
        return output


def cpp(code: str, input_string: str) -> str:
    """
    :param code: string
    :param input_string: string
    :return: Output of the code.
    """
    input_file_descriptor, input_file_name, code_file_descriptor, code_file_name, output_file_descriptor, output_file_name = _create_files(
        '.cpp')
    output = ""
    try:
        data, temp = os.pipe()
        os.write(temp, bytes(f"{input_string}\n", "utf-8"))
        os.close(temp)
        with os.fdopen(code_file_descriptor, 'w+') as fh:
            fh.write(code)
        s = subprocess.check_output(f"g++ {code_file_name} -o a;./a", stdin=data, shell=True, timeout=15)
        output = s.decode('utf-8')
    except subprocess.TimeoutExpired:
        output = "TLE (15s)."
    except Exception as e:
        output = e.__class__

    finally:
        os.remove(input_file_name)
        os.remove(code_file_name)
        os.remove(output_file_name)
        os.remove('./a')
        return output


def c(code: str, input_string: str) -> str:
    """
    :param code: string
    :param input_string: string
    :return: Output of the code.
    """

    input_file_descriptor, input_file_name, code_file_descriptor, code_file_name, output_file_descriptor, output_file_name = _create_files(
        '.c')
    output = ""

    try:
        with os.fdopen(input_file_descriptor, 'w+') as fh:
            fh.write(input_string)
        with os.fdopen(code_file_descriptor, 'w+') as fh:
            fh.write(code)

        command = f'gcc {code_file_name} > {output_file_name}'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=15)

        with os.fdopen(output_file_descriptor, 'r+') as fh:
            output = fh.read()

        if len(output) > 20:
            output = output[20:]
        else:
            command = f'./a.out < {input_file_name} > {output_file_name} 2>&1'
            subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=15)
            with open(output_file_name, 'r+') as fh:
                output = fh.read()

    except subprocess.TimeoutExpired:
        output = "TLE (15s)."
    except Exception as e:
        output = e.__class__

    finally:
        os.remove(input_file_name)
        os.remove(code_file_name)
        os.remove(output_file_name)
        os.remove('./a.out')
        return output


def dart(code: str, input_string: str) -> str:
    """
    :param code: string
    :param input_string: string
    :return: Output of the code.
    """

    input_file_descriptor, input_file_name, code_file_descriptor, code_file_name, output_file_descriptor, output_file_name = _create_files(
        '.dart')
    output = ""

    try:
        with os.fdopen(input_file_descriptor, 'w+') as fh:
            fh.write(input_string)
        with os.fdopen(code_file_descriptor, 'w+') as fh:
            fh.write(code)

        command = f'cat {input_file_name} | dart {code_file_name} > {output_file_name} 2>&1'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=15)

        with os.fdopen(output_file_descriptor, 'r+') as fh:
            output = fh.read()

    except subprocess.TimeoutExpired:
        output = "TLE (15s)."
    except Exception as e:
        output = e.__class__

    finally:
        os.remove(input_file_name)
        os.remove(code_file_name)
        os.remove(output_file_name)
        return output


def golang(code: str, input_string: str) -> str:
    """
    :param code: string
    :param input_string: string
    :return: Output of the code.
    """

    input_file_descriptor, input_file_name, code_file_descriptor, code_file_name, output_file_descriptor, output_file_name = _create_files(
        '.go')
    output = ""

    try:
        with os.fdopen(input_file_descriptor, 'w+') as fh:
            fh.write(input_string)
        with os.fdopen(code_file_descriptor, 'w+') as fh:
            fh.write(code)

        command = f'cat {input_file_name} | go run {code_file_name} > {output_file_name} 2>&1'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=15)

        with os.fdopen(output_file_descriptor, 'r+') as fh:
            output = fh.read()

    except subprocess.TimeoutExpired:
        output = "TLE (15s)."
    except Exception as e:
        output = e.__class__

    finally:
        os.remove(input_file_name)
        os.remove(code_file_name)
        os.remove(output_file_name)
        return output


def rust(code: str, input_string: str) -> str:
    """
    :param code: string
    :param input_string: string
    :return: Output of the code.
    """

    input_file_descriptor, input_file_name, code_file_descriptor, code_file_name, output_file_descriptor, output_file_name = _create_files(
        '.rs')
    output = ""

    try:
        with os.fdopen(input_file_descriptor, 'w+') as fh:
            fh.write(input_string)
        with os.fdopen(code_file_descriptor, 'w+') as fh:
            fh.write(code)

        command = f'rustc {code_file_name} > {output_file_name}'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=15)

        with os.fdopen(output_file_descriptor, 'r+') as fh:
            output = fh.read()

        if len(output) > 0:
            pass
        else:
            command = f'./{code_file_name[:-3].rsplit("/", 1)[-1]} < {input_file_name} > {output_file_name} 2>&1'
            subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=15)
            with open(output_file_name, 'r+') as fh:
                output = fh.read()

    except subprocess.TimeoutExpired:
        output = "TLE (15s)."
    except Exception as e:
        output = e.__class__

    finally:
        os.remove(input_file_name)
        os.remove(code_file_name)
        os.remove(output_file_name)
        os.remove(f'./{code_file_name[:-3].rsplit("/", 1)[-1]}')
        return output
