dazl-pb
=======

Protobuf-generated classes (and type hints) for use with dazl.

This module can be used directly without dazl if all you want are the
Protobuf-generated classes, but it is not explicitly designed with this in
mind.

If you'd like to build this from source, run

```
make wheel
```

Note that this bulid is quite a bit more complicated than a usual Python build.
Almost everything included in the "source" distribution is actually generated.
Because this is such a bespoke build, the Poetry/pyproject.toml approach
doesn't really work as well here.
