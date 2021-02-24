# distributed-computing-explorations
Some ideas around concurrency and distributed computing

![nuclear powered](https://user-images.githubusercontent.com/58792/47737559-6c658900-dc2e-11e8-85fc-56ad0c9bf2d6.jpg)

Techniques used:

* [GPU (Using CUDA)](https://github.com/noahgift/nuclear_powered_command_line_tools/blob/master/nuclearcli.py#L136)
* [JIT](https://github.com/noahgift/nuclear_powered_command_line_tools/blob/master/nuclearcli.py#L159)
* [Machine Learning (Kmeans Clustering)](https://github.com/noahgift/nuclear_powered_command_line_tools/blob/master/nuclearcli.py#L170)
* [True Multi-Threaded (no GIL) Parallelization](https://github.com/noahgift/nuclear_powered_command_line_tools/blob/master/nuclearcli.py#L123)
* [Colored output from Click](https://github.com/noahgift/nuclear_powered_command_line_tools/blob/master/nuclearcli.py#L164)
* [Timing decorators](https://github.com/noahgift/nuclear_powered_command_line_tools/blob/master/nuclearcli.py#L29)
* [GPU Mandelbrot (Jupyter Notebook)](https://github.com/noahgift/nuclear_powered_command_line_tools/blob/master/notebooks/numba-cuda.ipynb)


## Chapter on Distributed Computing

* [distributed-computing](https://paiml.com/docs/home/books/cloud-computing-for-data/chapter04-distributed-computing/)

### Notebooks and Examples

* [concurrency-notebook-python](https://github.com/noahgift/distributed-computing-explorations/blob/main/Concurrency_Python.ipynb)
* [nuclear-powered-command-line-tool](https://github.com/noahgift/nuclear_powered_command_line_tools/blob/master/nuclearcli.py)
* [serial](https://github.com/noahgift/distributed-computing-explorations/blob/main/serial-means.py) vs [distributed kmeans](https://github.com/noahgift/distributed-computing-explorations/blob/main/parallel-kmeans.py)

### GPU Pricing Amazon

https://aws.amazon.com/ec2/pricing/on-demand/

Cheapest:  g4dn.xlarge	4	N/A	16 GiB	125 GB NVMe SSD	$0.526 per Hour


### References

[Turbocharging Python with Command Line Tools Article](https://www.kite.com/blog/python/python-command-line-tools/)
