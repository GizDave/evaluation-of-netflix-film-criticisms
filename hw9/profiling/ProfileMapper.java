import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class ProfileMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private IntWritable result = new IntWritable(0);
    
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {


//UNTESTED CODE
//        int count=0;
//        for(IntWritable v : values){
//            count+=1; //add 1 per line found
//        }
//        //set result to the count (int => IntWritable)
//        result.set(count);
//        //write to output
//        context.write(key, result);
    }
}

