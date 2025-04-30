ARG BASE_TAG=25.01-py3
FROM nvcr.io/nvidia/pytorch:${BASE_TAG}

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    cmake \
    build-essential \
    python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


# Env vars for MPI from the container
ENV MPI_ROOT="/opt/hpcx/ompi"
ENV NVCC_WRAPPER_DEFAULT_COMPILER="${MPI_ROOT}/bin/mpicxx"
ENV PATH="${MPI_ROOT}/bin:${PATH}"

WORKDIR /opt

# Clone your LAMMPS fork and build with Kokkos + ML‐MACE
ARG LAMMPS_REPO=https://github.com/empa-scientific-it/lammps.git
ARG LAMMPS_BRANCH=mace-features
RUN git clone --depth 1 --branch ${LAMMPS_BRANCH} ${LAMMPS_REPO} lammps

# Build LAMMPS with the optimized configuration
WORKDIR /opt/lammps

RUN mkdir build-grace && cd build-grace && \
    cmake ../cmake \
    -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_INSTALL_PREFIX=/opt/lammps \
    -D CMAKE_CXX_STANDARD=17 \
    -D CMAKE_CXX_STANDARD_REQUIRED=ON \
    -D MPI_HOME=/opt/hpcx/ompi \
    -D CMAKE_PREFIX_PATH="/opt/hpcx/ompi;/usr/local/lib/python3.12/dist-packages/torch/share/cmake" \
    -D MPI_C_COMPILER=/opt/hpcx/ompi/bin/mpicc \
    -D MPI_CXX_COMPILER=/opt/hpcx/ompi/bin/mpicxx \
    -D MPIEXEC_EXECUTABLE=/opt/hpcx/ompi/bin/mpirun \
    -D CMAKE_INCLUDE_PATH=/opt/hpcx/ompi/include \
    -D CMAKE_LIBRARY_PATH=/opt/hpcx/ompi/lib \
    -D PKG_KOKKOS=ON \
    -D Kokkos_ENABLE_CUDA=ON \
    -D Kokkos_ENABLE_OPENMP=ON \
    -D CMAKE_CXX_COMPILER=/opt/lammps/lib/kokkos/bin/nvcc_wrapper \
    -D Kokkos_ARCH_ARMV9_GRACE=ON \
    -D Kokkos_ARCH_HOPPER90=ON \
    -D BUILD_MPI=ON \
    -D BUILD_SHARED_LIBS=ON \
    -D PKG_ML-MACE=ON && \
    make -j"$(nproc)" && \
    make install

# Set up environment to find LAMMPS
ENV PATH="/opt/lammps/bin:${PATH}"
