import os
import time
from dotenv import load_dotenv
load_dotenv()

import docker
import requests

from DockerMetricsCollector import DockerMetricsCollector


def send_request():
    session = requests.session()
    start_time = time.time()

    response = session.post("http://localhost:8080", json={
        "login": os.getenv("LOGIN"),
        "senha": os.getenv("SENHA")
    }, )

    end_time = time.time()

    print(f"Resposta da solicitação: {response.text} - Tempo: {end_time - start_time}s")


def main():
    client = docker.from_env()
    for i in range(10):
        print("Iniciando o contêiner...")
        mem_limit = '128m'
        cpu_period = 100000
        cpu_quota = 20000
        container_img_name = "img-python"
        container = client.containers.run(container_img_name,
                                          detach=True,
                                          ports={'8080/tcp': 8080},
                                          mem_limit=mem_limit,
                                          cpu_period=cpu_period,
                                          cpu_quota=cpu_quota
                                          )

        print("Contêiner executando com ID:", container.id)
        try:
            time.sleep(8)
            collector = DockerMetricsCollector(container.id)
            collector.start()
            time.sleep(5)
            send_request()

            collector.stop()

            collector.export_to_csv(f'container_metrics_{container_img_name}.csv')
            print(f"Métricas exportadas para container_metrics_{container_img_name}.csv.")
        except Exception as ex:
            print(ex)
        finally:
            container.stop()
            container.remove()


if __name__ == "__main__":
    main()
