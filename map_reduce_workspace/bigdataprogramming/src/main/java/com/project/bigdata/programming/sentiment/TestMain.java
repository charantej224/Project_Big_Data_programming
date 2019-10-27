package com.project.bigdata.programming.sentiment;

public class TestMain {

	public static void main(String[] args) {
		String value = "yo, \"I'm charan, I'm also hunter\",w ,wer";
		String[] stringArray = value.split("[,|\"| ]");
		for (String val : stringArray) {
			System.out.println(val);
		}
	}
}
