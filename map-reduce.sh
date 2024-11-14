git clone https://github.com/chsu2023/14848project.git && \
cd 14848project && \
hadoop fs -put input_data.txt / && \
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -file mapper.py -mapper '/opt/conda/default/bin/python mapper.py' -file reducer.py -reducer '/opt/conda/default/bin/python reducer.py' -input /input_data.txt -output /final_output && \
hadoop fs -getmerge /final_output final_result && \
cat final_result
