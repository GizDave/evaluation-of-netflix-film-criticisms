import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class CleanMubiRatings {
    public static void main(String[] args) throws Exception {
    if (args.length != 2) {
        System.err.println("Usage: CleanMubiRatings <input path> <output path>");
        System.exit(-1);
    }

        Job job = new Job();
        job.setJarByClass(CleanMubiRatings.class);
        job.setJobName("CleanMubiRatings");
        job.setNumReduceTasks(0);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        job.setMapperClass(CleanMubiRatingsMapper.class);
        job.setOutputKeyClass(NullWritable.class);
        job.setOutputValueClass(Text.class);

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}