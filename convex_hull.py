from pyspark.sql import SparkSession
from pyspark.sql.types import StructField,StructType,IntegerType
from modules.generate_random_2d_points import generate_random_2d_points

spark = SparkSession.builder.appName("Assignment 07082024").getOrCreate()

points = generate_random_2d_points(number_of_particle=4,n=300)

point_schema = StructType([
    StructField("particle_id", IntegerType(), False),
    StructField("x", IntegerType(), False),
    StructField("y", IntegerType(), False)
])

df = spark.createDataFrame(points,schema=point_schema)

def create_df_by_particle_id(df):
    df_dict = {}
    number_of_particle_id = df.select("particle_id").distinct().count()
    for particle_id in range(1,number_of_particle_id+1):
        df_dict[f"df_{particle_id}"] = df.filter(f"particle_id = {particle_id}")
    return df_dict

df_dict = create_df_by_particle_id(df=df)

for value in df_dict.values():
    print(value.show())