# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-cp2k-spm-tools
#
# You can edit this file again by typing:
#
#     spack edit py-cp2k-spm-tools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyCp2kSpmTools(PythonPackage):
    """
    Library and scripts to perform scanning probe microscopy simulations based on a CP2K calculation
    """

    # Package details
    homepage = "https://github.com/nanotech-empa/cp2k-spm-tools"
    pypi = "cp2k_spm_tools/cp2k_spm_tools-1.4.4.tar.gz"

    maintainers("eimrek", "edoardob90")

    license("MIT License", checked_by="edoardob90")

    version("1.4.4", sha256="8295f56120d57ca16511de99c6714ca1b45b30b008ae0c8ecc32be95ed07904d")

    # Dependencies
    # Python version requirement from pyproject.toml
    depends_on("python@3.8:", type=("build", "run"))

    # Build dependencies
    depends_on("py-setuptools@61.0:", type="build")

    # Runtime dependencies
    depends_on("py-numpy@1.22:2", type=("build", "run"))
    depends_on("py-scipy@1.10:2", type=("build", "run"))
    depends_on("py-ase@3.15:4", type=("build", "run"))
    depends_on("py-matplotlib@3.0:4", type=("build", "run"))
    depends_on("py-mpi4py@3.1:", type=("build", "run"))
    depends_on("mpi", type=("build", "run"))  # External MPI dependency
