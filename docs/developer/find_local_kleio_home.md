# Finding the ``timelink-home`

In many use cases it is necessary to determine if a given directory is part of  a `timelink_home` directory.

For more information about the structure of ``timelink_home`  see [timelink_home](../reference/timelink_home.md)

The most common use case is when an aoo using `timelink` is launched in a given directory and need to find if the directory is part of a ``timelink` structure or not. This is the case with the command libe command `timelink` or when the timelink package is used from a Jupyter notebook.

The function  `KleioServer.find_local_kleio_home(path)` tests if a path is  a `timelink_home`  and if not searches in directory hierarchy to `path` for one. If `path` is not passed the function will search from the current directory.