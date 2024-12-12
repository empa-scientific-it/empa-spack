# empa-spack

Spack packages of software used or maintained at Empa.

## Prerequisites

1. Ensure you have Spack installed on your system. Follow the [Spack installation guide](https://spack.readthedocs.io/en/latest/getting_started.html) if needed.
2. Ensure `git` is installed on your system to clone this repository.

## Add this repository

1. **Clone**

Clone the repository to your local system:
```bash
git clone https://github.com/empa-scientificit/empa-spack.git /path/to/local/repo
```

2. **Add the repository to Spack**

Register the cloned repository with Spack:
```bash
spack repo add /path/to/local/repo
```

You can confirm that the repository was added successfully by running:
```bash
spack repo list
```
You should see an entry for this repository, followed by the built-in Spack repository.

3. **Check for available packages**

To list all packages provided by this repository, run:
```bash
spack list
```

Packages from this repository will appear with the repository's namespace (e.g., `empa.package-name`).


## Using the custom packages

1. **Search for a package**

You can search for a specific package using:
```bash
spack info package-name
```

2. **Install a package**

Install any package from this repository as you would for any Spack package:
```bash
spack install package-name
```

If you want to make sure to install a package from this specific repository, specify the namespace explicitly:
```bash
spack install empa.package-name
```

Remember that Spack's repos order matters. If you have multiple repositories with the same package, Spack will use the first one in the list.

For example, if your `repos.yaml` file looks like:
```yaml
repos:
  - ~/proto
  - /usr/local/spack
  - $spack/var/spack/repos/builtin
```

The command `spack install hdf5` will install the package from the `~/proto` repository, if available. If not, it will install the package from the `/usr/local/spack` repository, falling back to the built-in Spack repository if necessary, and failing if no repository provides the package.

Also note that:
> Any unqualified package name will be resolved by searching `repos.yaml` from the first entry to the last. You can force a particular repository's package by using a fully qualified name.

## Repository structure

This repository must follow the standard Spack repository structure:
```
repo/
  ├── repo.yaml   # Metadata for the repository
  └── packages/   # Directory containing package recipes
      ├── package1/
      │   └── package.py
      └── package2/
          └── package.py
```

The `repo.yaml` defines the namespace as `empa`. For example:
```yaml
repo:
  namespace: empa
```

---

For additional info, refer to the [Spack documentation](https://spack.readthedocs.io).
