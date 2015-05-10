import psutil


class MemoryCollector(object):

    @staticmethod
    def get_usage():
        return psutil.virtual_memory()._asdict()