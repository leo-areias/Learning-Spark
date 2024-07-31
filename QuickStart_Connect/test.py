from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.master("spark://localhost:7077").appName("ExampleApp").getOrCreate()

# Sample data
columns = ["id", "name"]
data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]

# Create DataFrame
df = spark.createDataFrame(data).toDF(*columns)

# Show DataFrame
df.show()

# Stop the Spark session
spark.stop()


#IMPORTANT COMMANDS
#Navigate to spark folder to initialize teh server
#./sbin/start-master.sh to start the master
#./sbin/start-worker.sh spark://localhost:7077 to start the worker

##./sbin/stop-master.sh
##./sbin/stop-worker.sh