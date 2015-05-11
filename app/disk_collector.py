import psutil


class DiskCollector(object):

    @staticmethod
    def get_usage():
        return psutil.disk_usage('/')._asdict()