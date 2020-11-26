import org.apache.hadoop.fs.Path;
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

class CleanReducer extends Reducer<Text, IntWritable, Text, Text> {
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        // nothing has to be done
    }
}