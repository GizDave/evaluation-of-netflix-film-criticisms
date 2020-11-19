import java.io.*;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CleanMubiMovieMapper extends Mapper<LongWritable, Text, Text, Text> {
        private static final int MISSING = 9999;

        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
                String line = value.toString();
                String[] lines = line.split(",");
                if(lines.length >= 9) {
                    String toReduce = lines[0] + "," + lines[1] + "," + lines[2] + "," + lines[4] + "," + lines[5] + "," + lines[8];
                    context.write(new Text(toReduce), new Text(" "));
                }
				
        }
}
