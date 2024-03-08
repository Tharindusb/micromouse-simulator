import subprocess
import sys

def isConanInstalled():
    try:
        subprocess.check_output(["conan", "--version"], stderr=subprocess.STDOUT)
        print("Conan is already installed.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Conan is not installed.")
        return False
    
def installConan():
    try:
        print("Installing Conan...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "conan"])
        print("Conan installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Conan: {e}")
    
def libInstall():
    pass

def main():
    if isConanInstalled():
        print("Conan is already installed.")
    else:
        print("Conan is not installed.")
        installConan()

def runConan(build_type):
    subprocess.run(('conan' ,'install', '.', 
        '--build', 'missing', '--output-folder=./dependencies',
        f'--settings=build_type={build_type}'))
    

if __name__ == "__main__":
    # main()
    # runConan('Debug')
    subprocess.run(("./Vendor/bin/windows/premake5.exe","vs2022"))
