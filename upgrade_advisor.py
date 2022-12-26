import get_info
import sys


class UpgradeAdvisor:
    def __init__(self, filename, num):
        self.filename = filename
        self.num = num
        self.cpu_upgrades = []
        self.gpu_upgrades = []

    @staticmethod
    def get_upgrades(current_part, parts, scores, num):
        index = parts.index(current_part)
        score = scores[index]

        new_score = ((100 + num) / 100) * score

        recommended = []

        for i in range(index):
            if scores[i] >= new_score:
                recommended.append(parts[i])

        return recommended

    def run_advisor(self):
        info = get_info.InfoTool(self.filename)
        current_cpu, current_gpu, cpus, cpu_scores, gpus, gpu_scores = info.get_info()
        self.cpu_upgrades = self.get_upgrades(current_cpu, cpus, cpu_scores, self.num)
        self.gpu_upgrades = self.get_upgrades(current_gpu, gpus, gpu_scores, self.num)

        return self.cpu_upgrades, self.gpu_upgrades


def main():
    filename = sys.argv[1]
    num = int(sys.argv[2])
    advisor = UpgradeAdvisor(filename, num)
    cpu_upgrades, gpu_upgrades = advisor.run_advisor()
    print(cpu_upgrades)
    print(gpu_upgrades)


main()