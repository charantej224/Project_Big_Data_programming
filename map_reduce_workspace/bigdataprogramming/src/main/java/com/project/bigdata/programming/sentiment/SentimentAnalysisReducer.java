package com.project.bigdata.programming.sentiment;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class SentimentAnalysisReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

	@Override
	public void reduce(Text inputKey, Iterable<IntWritable> inputValues, Context context)
			throws IOException, InterruptedException {
		String outputKey = inputKey.toString();
		int outputValue = 0;
		for (IntWritable eachValue : inputValues) {
			outputValue += eachValue.get();
		}
		if (!outputKey.trim().equalsIgnoreCase("")) {
			context.write(new Text(outputKey.trim()), new IntWritable(outputValue));
			System.out.println(outputKey + outputValue);
		}

	}
}
