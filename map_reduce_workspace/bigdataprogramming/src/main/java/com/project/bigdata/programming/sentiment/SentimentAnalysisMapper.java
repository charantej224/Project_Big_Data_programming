package com.project.bigdata.programming.sentiment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.util.HashMap;

import org.apache.hadoop.filecache.DistributedCache;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class SentimentAnalysisMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

	private URI[] files;
	private HashMap<String, String> AFINN_map = new HashMap<String, String>();

	@Override
	public void setup(Context context) throws IOException, InterruptedException {
		try {
			files = DistributedCache.getCacheFiles(context.getConfiguration());
			System.out.println("files:" + files);
			Path path = new Path(files[0]);
			FileSystem fs = FileSystem.get(context.getConfiguration());
			FSDataInputStream in = fs.open(path);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));
			String line = "";
			while ((line = br.readLine()) != null) {
				String splits[] = line.split("\t");
				AFINN_map.put(splits[0], splits[1]);
			}
			br.close();
			in.close();
		} catch(Exception exception) {
			exception.printStackTrace();
			throw exception;
		}
		
	}

	@Override
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
		String line = value.toString();
		line = line.toLowerCase().trim();
		if("".equalsIgnoreCase(line))
			return;
		String[] tuple = line.split("[,|\"| ]");
		int sentimentAnalysis = 0;
		for (int i = 0; i < tuple.length; i++) {
			if (AFINN_map.containsKey(tuple[i])) {
				Integer x = new Integer(AFINN_map.get(tuple[i]));
				sentimentAnalysis += x;
			}
		}
		context.write(value, new IntWritable(sentimentAnalysis));
	}
}