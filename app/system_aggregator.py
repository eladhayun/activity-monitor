import json

from cpu_collector import CpuCollector
from disk_collector import DiskCollector
from memory_collector import MemoryCollector
from network_collector import NetworkCollector


class SystemAggregator(object):
    def __init__(self):
        self._cpu_collector = CpuCollector()
        self._disk_collector = DiskCollector()
        self._memory_collector = MemoryCollector()
        self._network_collector = NetworkCollector()

    def get_usage(self):
        return {
            "CPU": self._cpu_collector.get_usage(),
            "Disk": self._disk_collector.get_usage(),
            "Memory": self._memory_collector.get_usage(),
            "Network": self._network_collector.get_usage()
        }

    def get_cpu_usage(self):
        return self._cpu_collector.get_usage()

    def get_disk_usage(self):
        return self._disk_collector.get_usage()

    def get_memory_usage(self):
        return self._memory_collector.get_usage()

    def get_network_usage(self):
        return self._network_collector.get_usage()

    def __str__(self):
        return json.dumps(self.get_usage(), indent=4, sort_keys=True)