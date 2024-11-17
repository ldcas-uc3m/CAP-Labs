# Laboratorio de Apache Spark

1. Install [docker](https://docs.docker.com/engine/install/)
2. Execute the spark container
    ```bash
    docker compose up
    ```
    This should output at the end an URL like `http://127.0.0.1:8888/lab?token=<token>`
3. Open the Jupyter lab notebook [`notebook/CAP_Spark_2024.ipynb`](notebook/CAP_Spark_2024.ipynb) on the previous URL.
> [!NOTE]
> Alternatively, open the notebook in VsCode and connect to a remote Jupyter (`Select Kernel` → `Existing Jupyter Server`), using `http://127.0.0.1:8888` as URL and `<token>` as password.

You can monitor spark in [localhost:4040](http://localhost:4040/).