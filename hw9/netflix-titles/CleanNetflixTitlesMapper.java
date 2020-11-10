import java.io.IOException;
//import org.apache.hadoop.io.IntWritable;
//import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CleanNetflixTitlesMapper extends Mapper<LongWritable, Text, NullWritable, Text> {
    
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException,InterruptedException {
        //TODO
        String line = value.toString();        
        String[] tokens= line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)"); // parse csv
        //int cols = 12;
        //todo: delete first row? add: (|| tokens[0].equals("show_id"))
        if(tokens.length==12){
            //build csv row
            String retStr="";
            //remove 1st col
            for(int i=1;i<12;i++){
                retStr+=tokens[i];
                if(i<11){
                    retStr+=",";
                }
            }
            context.write(NullWritable.get(),new Text(retStr));
        }
    }
}

