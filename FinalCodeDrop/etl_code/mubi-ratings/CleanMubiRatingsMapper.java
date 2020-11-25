import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CleanMubiRatingsMapper extends Mapper<LongWritable, Text, NullWritable, Text> {
    
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException,InterruptedException {
        String line = value.toString();        
        String[] tokens= line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)"); // parse csv
        //13 columns
        if(tokens.length==13){
            if(!tokens[0].equals("movie_id")){ //trim header
                //set flag to check if booleans are proper booleans, ie. True or False entries only
                boolean isValid = true;
                for(int i=9;i<=12;i++) {
                    isValid = tokens[i].equals("True")||tokens[i].contentEquals("False");
                }

                if(isValid){
                    //build csv row
                    String retStr="";
                    //do nothing to tokens (for now)
                    for(int i=0;i<13;i++){
                        //rebuild the string
                        retStr+=tokens[i];
                        if(i<12){
                            retStr+="|";
                        }
                    }
                    context.write(NullWritable.get(),new Text(retStr));
                }
            }
        }
    }
}

