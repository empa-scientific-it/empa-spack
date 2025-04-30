#!/usr/bin/env bash
set -euo pipefail

# Prepare build directory
mkdir -p build-grace
cd build-grace

# Make sure nvcc_wrapper invokes mpicxx under the hood
export MPI_ROOT="/opt/hpcx/ompi"
export NVCC_WRAPPER_DEFAULT_COMPILER="${MPI_ROOT}/bin/mpicxx"

# Configure with CMake
cmake ../cmake \
  -D CMAKE_BUILD_TYPE=Release \
  -D CMAKE_INSTALL_PREFIX=$(pwd) \
  -D CMAKE_CXX_STANDARD=17 \
  -D CMAKE_CXX_STANDARD_REQUIRED=ON \

  #------------------------------------------------------------------------------
  # Point CMake at your custom MPI under /opt/hpcx/ompi
  #------------------------------------------------------------------------------
  -D MPI_HOME=/opt/hpcx/ompi \
  -D CMAKE_PREFIX_PATH=/opt/hpcx/ompi \
  -D MPI_C_COMPILER=/opt/hpcx/ompi/bin/mpicc \
  -D MPI_CXX_COMPILER=/opt/hpcx/ompi/bin/mpicxx \
  -D MPIEXEC_EXECUTABLE=/opt/hpcx/ompi/bin/mpirun \
  -D CMAKE_INCLUDE_PATH=/opt/hpcx/ompi/include \
  -D CMAKE_LIBRARY_PATH=/opt/hpcx/ompi/lib \

  #------------------------------------------------------------------------------
  # Kokkos + CUDA + OpenMP + Grace/Hopper
  #------------------------------------------------------------------------------
  -D PKG_KOKKOS=ON \
  -D Kokkos_ENABLE_CUDA=ON \
  -D Kokkos_ENABLE_OPENMP=ON \
  -D CMAKE_CXX_COMPILER=${PWD}/../lib/kokkos/bin/nvcc_wrapper \
  -D Kokkos_ARCH_ARMV9_GRACE=ON \
  -D Kokkos_ARCH_HOPPER90=ON \

  #------------------------------------------------------------------------------
  # Torch for ML-MACE
  #------------------------------------------------------------------------------
  -D CMAKE_PREFIX_PATH=/usr/local/lib/python3.12/dist-packages/torch/share/cmake \

  #------------------------------------------------------------------------------
  -D BUILD_MPI=ON \
  -D BUILD_SHARED_LIBS=ON \
  -D PKG_ML-MACE=ON

# Build & install
#make -j"${JOBS}"
#make install
