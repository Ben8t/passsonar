
## Build Docker image

`docker build -t passsonar .`

## Run Docker container (dev)

`docker container run --rm -it -v $(pwd):/app -p 8501:8501 passsonar bash`

# Resources

* https://matplotlib.org/3.1.1/gallery/axisartist/demo_floating_axes.html
* https://kite.com/python/examples/5561/matplotlib-plot-a-polar-plot
* https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html
* https://matplotlib.org/tutorials/intermediate/gridspec.html
* https://python4astronomers.github.io/plotting/advanced.html
* https://fcpython.com/visualisation/drawing-pass-map-python