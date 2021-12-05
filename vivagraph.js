var graph = Viva.Graph.graph();
graph.addLink(1, 2);

var graphics = Viva.Graph.View.webglGraphics();

var renderer = Viva.Graph.View.renderer(graph,
    {
        graphics : graphics
    });
renderer.run();
