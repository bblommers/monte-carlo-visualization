
var w = window,
    d = document,
    e = d.documentElement,
    g = d.getElementsByTagName('body')[0],
    x = w.innerWidth || e.clientWidth || g.clientWidth,
    y = w.innerHeight|| e.clientHeight|| g.clientHeight;

var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = x - margin.left - margin.right,
    height = y - margin.top - margin.bottom;


function plot(data) {

var x = d3.scaleLinear()
    .range([0, width])

var y = d3.scaleLinear()
    .range([height, 0])

var xAxis = d3.axisBottom()
    .scale(x);

var yAxis = d3.axisLeft()
    .scale(y);

var line = d3.line()
    .x(function(d) { return x(d.step); })
    .y(function(d) { return y(d.val); })
    .curve(d3.curveLinear);

  var elem = document.querySelector('#graph');
  if (elem) {
      elem.parentNode.removeChild(elem);
  }
  var svg = d3.select("#result").append("svg")
    .attr("id", "graph")
    .attr("width", width)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var xmin = data[0][0].step, xmax = data[0][0].step, ymin = data[0][0].val, ymax = data[0][0].val
  for (i=0; i<data.length; i++) {
    for (j=0; j<data[i].length; j++) {
      xmin = Math.min(xmin, data[i][j].step)
      xmax = Math.max(xmax, data[i][j].step)
      ymin = Math.min(ymin, data[i][j].val)
      ymax = Math.max(ymax, data[i][j].val)
    }
  }

  for (i=0; i<data.length; i++) {
    x.domain([xmin, xmax]);
    y.domain([ymin, ymax]);

    svg.append("path")
      .data([data[i]])
      .attr("class", "line")
      .attr("d", line)
      .attr('stroke', "blue")
  }
  var static_line = []
  for (i=0; i<data[0].length; i++) {
    static_line.push({"step": i, "val": document.getElementById("input_K").value})
  }

  svg.append("path")
    .data([static_line])
    .attr("class", "line")
    .attr("d", line)

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
}

