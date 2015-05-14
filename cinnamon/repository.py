from flask import Flask, jsonify, request
from system_aggregator import SystemAggregator


app = Flask(__name__)
system_aggregator = SystemAggregator()


@app.route("/", methods=["GET"])
def system():
    if request.method == "GET":
        return jsonify(**system_aggregator.get_usage())


@app.route("/cpu", methods=["GET"])
def cpu():
    if request.method == "GET":
        return jsonify(**system_aggregator.get_cpu_usage())


@app.route("/memory", methods=["GET"])
def memory():
    if request.method == "GET":
        return jsonify(**system_aggregator.get_memory_usage())


@app.route("/disk", methods=["GET"])
def disk():
    if request.method == "GET":
        return jsonify(**system_aggregator.get_disk_usage())


@app.route("/network", methods=["GET"])
def network():
    if request.method == "GET":
        return jsonify(**system_aggregator.get_network_usage())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
