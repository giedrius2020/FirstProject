import subprocess
import os


def build_executable(script_path, one_file=True, no_console=False, additional_paths=None, exe_name=None):
    """
    Build a single executable from a Python script using PyInstaller.

    Args:
    - script_path (str): Path to the Python script to be converted.
    - one_file (bool): Whether to bundle everything into a single executable.
    - no_console (bool): Whether to suppress the console window for GUI applications.
    - additional_paths (list): List of additional paths to include.
    """
    pyinstaller_path = "pyinstaller"

    # Generate initial spec file
    spec_args = [pyinstaller_path, "--onefile" if one_file else "--onedir", script_path]

    if no_console:
        spec_args.append("--noconsole")
    if exe_name:
        spec_args.extend(["--name", exe_name])
    subprocess.run(spec_args)



    # Modify spec file to include additional paths
    spec_file = os.path.splitext(os.path.basename(script_path))[0] + ".spec"
    if additional_paths:
        with open(spec_file, "r") as file:
            content = file.readlines()

        with open(spec_file, "w") as file:
            for line in content:
                if line.strip().startswith("pathex="):
                    # Add additional paths to the pathex list
                    paths = ", ".join([f"'{path}'" for path in additional_paths])
                    line = f"    pathex=[{paths}],\n"
                file.write(line)

    # Build executable using modified spec file
    build_args = [pyinstaller_path, spec_file]
    print(f"Running command: {' '.join(build_args)}")  # Print the command
    subprocess.run(build_args)


if __name__ == "__main__":
    # Example usage
    script_to_convert = "main.py"
    additional_paths = [r'C:\\Users\\Admin\\PycharmProjects\\VisualSimulation\\my_modules']
    build_executable(script_to_convert,
                     one_file=True,
                     no_console=False,
                     additional_paths=additional_paths,
                     exe_name="Application")
