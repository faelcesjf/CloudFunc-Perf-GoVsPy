#!/bin/bash


num_iterations=5000

image_name="teste_cloud_function"

output_file="metrics.csv"


echo "Container ID, CPU %, Mem Usage / Limit, Mem %, Net I/O, Block I/O, PIDs, Execution Time (s)" > "$output_file"

for i in $(seq 1 $num_iterations); do
  echo "Iniciando execução $i de $num_iterations"
  
  
  start_time=$(date +%s)
  
  
  container_id=$(sudo docker run -d -p 8080:8080 $image_name)
  
  
  sleep 5
  
  
  curl -X POST http://localhost:8080 -H "Content-Type: application/json" -d '{"size":5000}'
  
  
  end_time=$(date +%s)
  
  execution_time=$((end_time - start_time))
  
  
  docker_stats=$(sudo docker stats --no-stream --format "{{.ID}}, {{.CPUPerc}}, {{.MemUsage}}, {{.MemPerc}}, {{.NetIO}}, {{.BlockIO}}, {{.PIDs}}" $container_id)
  
  sudo docker stop $container_id > /dev/null
  sudo docker rm $container_id > /dev/null
  
  
  echo "$docker_stats, $execution_time" >> "$output_file"
done

echo "Simulação concluída. Métricas coletadas em $output_file."

