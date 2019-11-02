package com.project.bigdata.programming.sentiment;

import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.filecache.DistributedCache;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class SentimentAnalysisMain {

	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		if (args.length != 3) {
			System.err.println("Usage: Parse <in> <out>");
			System.exit(2);
		}
		//DistributedCache.addCacheFile(new URI("hdfs://localhost:9000/user/sentiment_analysis/reference/AFINN.txt"), conf);
		conf.addResource(new Path("/Users/saiaravindreddymannem/hadoop/hadoop-2.8.1/etc/hadoop/core-site.xml"));
		DistributedCache.addCacheFile(new Path(args[2]).toUri(), conf);
		Job job = new Job(conf, "SentimentAnalysis");
		job.setJarByClass(SentimentAnalysisMain.class);
		job.setMapperClass(SentimentAnalysisMapper.class);
		job.setReducerClass(SentimentAnalysisReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		System.exit(job.waitForCompletion(true) ? 0 : 1);
		// return 0;
	}
}
