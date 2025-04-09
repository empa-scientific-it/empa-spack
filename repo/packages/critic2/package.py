# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Critic2(CMakePackage):
    """Critic2 is a program for the manipulation and analysis of structural and chemical information in molecules and solids"""

    url = "https://github.com/aoterodelaroza/critic2/archive/refs/tags/1.2.tar.gz"

    maintainers("edoardob90")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("GPL-3.0-or-later", checked_by="edoardob90")

    version("1.2", sha256="b59ecffd83405dbcc4b5d157d4a94bf2756916f72e83e09a94d277d54d0f2225")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
