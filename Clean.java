import org.apache.hadoop.fs.Path;
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

class CleanMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private static final int MISSING = 9999;  
    
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {    
        String line = value.toString();        
        String[] tokens= line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)"); // parse csv
    }
}

class CleanReducer extends Reducer<Text, IntWritable, Text, IntWritable> {  
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

    }
}

public class Clean {
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: MaxTemperature <input path> <output path>");
            System.exit(-1);
        }
        
        Job job = new Job();
        job.setJarByClass(Clean.class);
        job.setJobName("Max temperature");
        
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        
        job.setMapperClass(CleanMapper.class);
        job.setReducerClass(CleanReducer.class);
    	    
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
	    job.setNumReduceTasks(1);        

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}