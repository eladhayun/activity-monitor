import time
import psutil


class NetworkCollector(object):

    @staticmethod
    def get_rate():
        rate = psutil.net_io_counters()
        return rate.bytes_sent + rate.bytes_recv

    @staticmethod
    def get_usage():
        d1_rate = NetworkCollector.get_rate()
        time.sleep(1)
        d2_rate = NetworkCollector.get_rate()
        return {
            "rate": (d2_rate - d1_rate) / (1024 * 1024)
        }