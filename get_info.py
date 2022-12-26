import urllib.request
import txt_parser, csv_parser


class InfoTool:
    def __init__(self, filename):
        self.CPU_URL = "https://www.userbenchmark.com/resources/download/csv/CPU_UserBenchmarks.csv"
        self.GPU_URL = "https://www.userbenchmark.com/resources/download/csv/GPU_UserBenchmarks.csv"
        self.cpus = []
        self.cpu_scores = []
        self.gpus = []
        self.gpu_scores = []
        self.current_cpu = None
        self.current_gpu = None
        self.filename = filename

    def get_info(self):
        # download the file
        urllib.request.urlretrieve(self.CPU_URL, "cpu.csv")
        urllib.request.urlretrieve(self.GPU_URL, "gpu.csv")

        tp = txt_parser.TXTParser()

        self.current_cpu, self.current_gpu = tp.parse(self.filename)

        cp = csv_parser.CSVParser()

        self.cpus, self.cpu_scores = cp.parse("cpu.csv")

        self.gpus, self.gpu_scores = cp.parse("gpu.csv")

        return self.current_cpu, self.current_gpu, self.cpus, self.cpu_scores, self.gpus, self.gpu_scores