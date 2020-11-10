import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CleanNetflixTitlesMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException,InterruptedException {
        //TODO
        String line = value.toString();        
        String[] tokens= line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)"); // parse csv
//        int cols = 12;
        /*
        check tokens.length==12
        remove tokens[0]
        
        */
        
        
    }
}

