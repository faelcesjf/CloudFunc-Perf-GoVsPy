from datetime import datetime

def process_stat(stat,container_id):
    cpu_delta = stat["cpu_stats"]["cpu_usage"]["total_usage"] - \
                stat["precpu_stats"]["cpu_usage"]["total_usage"]
    system_cpu_delta = stat["cpu_stats"]["system_cpu_usage"] - \
                       stat["precpu_stats"]['system_cpu_usage']
    number_cpus = stat["cpu_stats"]["online_cpus"]
    cpu_usage_percent = (cpu_delta / system_cpu_delta) * number_cpus * 100.0 if system_cpu_delta > 0 else 0.0

    mem_usage = stat["memory_stats"]["usage"] / (1024 ** 2)
    mem_limit = stat["memory_stats"]["limit"] / (1024 ** 2)
    print(mem_usage)
    net_input = stat["networks"]["eth0"]["rx_bytes"] / (1024 ** 2) if "eth0" in stat["networks"] else 0
    net_output = stat["networks"]["eth0"]["tx_bytes"] / (1024 ** 2) if "eth0" in stat["networks"] else 0

    block_input = sum(
        [blk["value"] for blk in stat["blkio_stats"]["io_service_bytes_recursive"] if blk["op"] == "Read"]) / (
                                 1024 ** 2)
    block_output = sum(
        [blk["value"] for blk in stat["blkio_stats"]["io_service_bytes_recursive"] if blk["op"] == "Write"]) / (
                                  1024 ** 2)

    data_point = {
        'container_id':container_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage": cpu_usage_percent,
        "mem_usage": mem_usage,
        "mem_limit": mem_limit,
        "net_input": net_input,
        "net_output": net_output,
        "block_input": block_input,
        "block_output": block_output
    }

    return data_point
