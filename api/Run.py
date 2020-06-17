import os
import subprocess
import tempfile


def _createFiles(suffix: str):
    inputfd, inputname = tempfile.mkstemp(dir='./api/temp')
    codefd, codename = tempfile.mkstemp(dir='./api/temp', suffix=suffix)
    outputfd, outputname = tempfile.mkstemp(dir='./api/temp')
    return inputfd, inputname, codefd, codename, outputfd, outputname


def Python(code: str, inputString: str):

    # inputfd, inputname, codefd, codename, outputfd, outputname = _createFiles('.py')
    inputfd, inputname = tempfile.mkstemp(dir='./api/temp')
    codefd, codename = tempfile.mkstemp(dir='./api/temp', suffix='.py')
    outputfd, outputname = tempfile.mkstemp(dir='./api/temp')

    try:
        with os.fdopen(inputfd, 'w+') as fh:
            fh.write(inputString)
        with os.fdopen(codefd, 'w+') as fh:
            fh.write(code)

        command = f'cat {inputname} | python3 {codename} > {outputname} 2>&1'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True)

        with os.fdopen(outputfd, 'r+') as fh:
            output = fh.read()

    except Exception as e:
        output = ""
        print(e.__class__)

    finally:
        os.remove(inputname)
        os.remove(codename)
        os.remove(outputname)
        return output


def Java(code: str, inputString: str):

    inputfd, inputname, codefd, codename, outputfd, outputname = _createFiles('.java')

    try:
        with os.fdopen(inputfd, 'w+') as fh:
            fh.write(inputString)
        with os.fdopen(codefd, 'w+') as fh:
            fh.write(code)

        command = f'cat {inputname} | javac {codename} > {outputname} 2>&1'
        subprocess.run(command, shell=True)

        with os.fdopen(outputfd, 'r+') as fh:
            output = fh.read()

        if len(output) == 0:
            command = f'cat {inputname} | java {codename[:-5]} > {outputname} 2>&1'
            subprocess.run(command, shell=True)
            with os.fdopen(outputfd, 'r+') as fh:
                output = fh.read()

    except Exception as e:
        output = ""
        print(e)

    finally:
        os.remove(inputname)
        os.remove(codename)
        os.remove(outputname)
        return output


def Cpp(code: str, inputString: str):

    inputfd, inputname, codefd, codename, outputfd, outputname = _createFiles('.cpp')

    try:
        with os.fdopen(inputfd, 'w+') as fh:
            fh.write(inputString)
        with os.fdopen(codefd, 'w+') as fh:
            fh.write(code)

        command = f'cat {inputname} | make {codename} > {outputname} 2>&1'
        subprocess.run(command, shell=True)

        with os.fdopen(outputfd, 'r+') as fh:
            output = fh.read()

        if len(output) > 28:
            output = output[27:]
        else:
            command = f'cat {inputname} | {codename[:-4]} > {outputname} 2>&1'
            subprocess.run(command, shell=True)
            with os.fdopen(outputfd, 'r+') as fh:
                output = fh.read()

    except Exception as e:
        output = ""
        print(e)

    finally:
        os.remove(inputname)
        os.remove(codename)
        os.remove(outputname)
        return output


def C(code: str, inputString: str):

    inputfd, inputname, codefd, codename, outputfd, outputname = _createFiles('.c')

    try:
        with os.fdopen(inputfd, 'w+') as fh:
            fh.write(inputString)
        with os.fdopen(codefd, 'w+') as fh:
            fh.write(code)

        command = f'cat {inputname} | make {codename} > {outputname} 2>&1'
        subprocess.run(command, shell=True)

        with os.fdopen(outputfd, 'r+') as fh:
            output = fh.read()

        if len(output) > 20:
            output = output[20:]
        else:
            command = f'cat {inputname} | {codename[:-2]} > {outputname} 2>&1'
            subprocess.run(command, shell=True)
            with os.fdopen(outputfd, 'r+') as fh:
                output = fh.read()

    except Exception as e:
        output = ""
        print(e)

    finally:
        os.remove(inputname)
        os.remove(codename)
        os.remove(outputname)
        return output

def Dart(code: str, inputString: str):

    inputfd, inputname, codefd, codename, outputfd, outputname = _createFiles('.dart')

    try:
        with os.fdopen(inputfd, 'w+') as fh:
            fh.write(inputString)
        with os.fdopen(codefd, 'w+') as fh:
            fh.write(code)

        command = f'cat {inputname} | dart {codename} > {outputname} 2>&1'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True)

        with os.fdopen(outputfd, 'r+') as fh:
            output = fh.read()

    except Exception as e:
        output = ""
        print(e)

    finally:
        os.remove(inputname)
        os.remove(codename)
        os.remove(outputname)
        return output

def Golang(code: str, inputString: str):

    inputfd, inputname, codefd, codename, outputfd, outputname = _createFiles('.go')

    try:
        with os.fdopen(inputfd, 'w+') as fh:
            fh.write(inputString)
        with os.fdopen(codefd, 'w+') as fh:
            fh.write(code)

        command = f'cat {inputname} | go run {codename} > {outputname} 2>&1'
        subprocess.run(command, stdout=subprocess.PIPE, shell=True)

        with os.fdopen(outputfd, 'r+') as fh:
            output = fh.read()

    except Exception as e:
        output = ""
        print(e)

    finally:
        os.remove(inputname)
        os.remove(codename)
        os.remove(outputname)
        return output