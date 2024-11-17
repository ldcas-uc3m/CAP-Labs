# Example of use of hadoop

## Installation and execution
1. Install [docker](https://docs.docker.com/engine/install/)
2. Execute the haddoop container
    ```bash
    docker compose up
    ```
3. Enter the container:
    ```bash
    docker exec -it hadoop /bin/bash
    ```
4. Put the books in the HDFS:
    ```bash
    cd /tmp
    hdfs dfs -put books /tmp
    ```
5. Compile and run the app:
    ```bash
    cd scripts/
    sh compile.sh
    hadoop jar wc.jar WordCount /tmp/books /tmp/salida
    ```
6. Check the output in `/tmp/salida` (inside HDFS)
    ```
    hdfs dfs -cat /tmp/salida/part-r-00000
    ```

## URLs
It will launch several webpages:
- [localhost:9870](https://localhost:9870): Namenode information (HDFS)
