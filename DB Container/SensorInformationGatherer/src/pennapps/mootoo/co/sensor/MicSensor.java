package pennapps.mootoo.co.sensor;

import org.bson.Document;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

public class MicSensor extends Sensor {

	private double micVoltage; //idk lol
	
	//Adafruit Huzza
	
	public MicSensor(String uniqueName, String location, double micVoltage, MongoClient client) {
		super(uniqueName, location);
		this.micVoltage = micVoltage;
	}

	public void addSensorInfoToDocument(String database, String roomName, MongoClient client) {
		Document doc = new Document("location", roomName)
				.append("mic. voltage", micVoltage);
		
		MongoDatabase db = client.getDatabase(database);
		
		MongoCollection<Document> collections = db.getCollection("sensors");
		collections.insertOne(doc);
	}
	
	public void setMicStatus(double micVolt) {
		micVoltage = micVolt;
	}

}
