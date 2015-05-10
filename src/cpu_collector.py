import psutil


class CpuCollector(object):

    @staticmethod
    def get_usage():
        return {
            "usage": 100 - psutil.cpu_times_percent(interval=1, percpu=False).idle
        }