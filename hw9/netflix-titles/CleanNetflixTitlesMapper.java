import java.io.IOException;
//import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CleanNetflixTitlesMapper extends Mapper<LongWritable, Text, NullWritable, Text> {
    
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException,InterruptedException {
        String line = value.toString();        
        String[] tokens= line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)"); // parse csv
        //12 columns
//        if(tokens.length==12){
        if(tokens.length==12){
            if(!tokens[0].equals("show_id")){
                String retStr="";
                for(int i=0;i<13;i++) {
                    retStr+=tokens[i];
                    if(i<12) {
                        retStr+=",";
                    }
                }
                System.out.println(retStr);
            }
        }
    }
}

