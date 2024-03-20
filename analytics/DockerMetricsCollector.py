import docker
import threading
import os
import csv
from metrics_utils import process_stat  
from time import sleep
class DockerMetricsCollector:
    def __init__(self, container_id):
        self.container_id = container_id
        self.client = docker.from_env()
        self.metrics = []
        self.stop_event = threading.Event()

    def collect_metrics(self):
        count = 1
        while not self.stop_event.is_set():
            stats = self.client.containers.get(self.container_id).stats(stream=False)

            data_point = process_stat(stats,self.container_id )
            self.metrics.append(data_point)
            sleep(0.5)
            print(f'Extraindo container {self.container_id} {count}')
            count = count + 1

    def start(self):
        self.thread = threading.Thread(target=self.collect_metrics)
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        self.thread.join()

    def export_to_csv(self, filename):
        if not self.metrics:
            print("Nenhuma métrica coletada para exportar.")
            return

        file_exists = os.path.isfile(filename)

        with open(filename, 'a', newline='') as file:
            fieldnames = self.metrics[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            for data_point in self.metrics:
                writer.writerow(data_point)