import java.io.*;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CleanMubiListMapper extends Mapper<LongWritable, Text, Text, Text> {
	private static final int MISSING = 9999;

	@Override
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
		String line = value.toString();
		String[] lines = line.split(",");
		Boolean isNumber = true;
		if(lines.length >= 9) {
			try {
				Integer.parseInt(lines[0]);
			}
			catch(NumberFormatException e){
				isNumber = false;
			}
			if(isNumber) {
				String toReduce = lines[0] + "," + lines[2] + "," + lines[3] + "," + lines[6] + "," + lines[7] + "," + lines[8];
				context.write(new Text(toReduce), new Text(""));
			}
		}

	}
}
