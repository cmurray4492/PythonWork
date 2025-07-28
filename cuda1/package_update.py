import subprocess
import pkg_resources

# you may need to install "setuptools" to get access to pkg_resources

# Iterate through all installed packages
for dist in pkg_resources.working_set:
    package_name = dist.project_name
    try:
        # Upgrade each package
        subprocess.check_call(["pip", "install", "--upgrade", package_name])
    except subprocess.CalledProcessError as e:
        print(f"Failed to update {package_name}: {e}")
