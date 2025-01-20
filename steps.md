Steps to use stackinator to build the uenv locally

[stackinator docs](https://eth-cscs.github.io/stackinator/configuring/)

```
git clone git@github.com:eth-cscs/stackinator.git
(cd stackinator; ./bootstrap)
export PATH=$PWD/stackinator/bin:$PATH
git clone git@github.com:eth-cscs/alps-cluster-config.git

# run stack-config and make on a compute node
srun -n1 -t180 --pty bash

stack-config -r /capstor/scratch/cscs/bcumming/empa/empa-spack/uenv/gpaw/v25.1/eiger -b /dev/shm/bcumming/gpaw -s ./alps-cluster-config/eiger -c ./cache.yaml

# create your own build cache in $SCRATCH/build-cache
# https://eth-cscs.github.io/stackinator/build-caches/
```
