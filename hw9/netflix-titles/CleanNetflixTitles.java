import org.apache.hadoop.fs.Path;
//import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class CleanNetflixTitles {
    public static void main(String[] args) throws Exception {
    if (args.length != 2) {
        System.err.println("Usage: CleanNetflixTitles <input path> <output path>");
        System.exit(-1);
    }

        Job job = new Job();
        job.setJarByClass(CleanNetflixTitles.class);
        job.setJobName("CleanNetflixTitles");
        job.setNumReduceTasks(1);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        job.setMapperClass(CleanNetflixTitlesMapper.class);
//        job.setReducerClass(CleanNetflixTitlesReducer.class);
//        job.setOutputKeyClass(Text.class);
        job.setOutputKeyClass(NullWritable.class);
        job.setOutputValueClass(Text.class);
//        job.setOutputValueClass(IntWritable.class);

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}