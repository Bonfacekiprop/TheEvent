TheEvent    
'''''                                                                                                                                                                                                                                                                                                         
Step 1: Clone the Repository	                                                                                                                                                                                                                                                    
Open your terminal and run the following command to clone this repository:	                                                                                                                                                                                    
git clone https://github.com/Bonfacekiprop/TheEvent.git	                                                                                                                                                                                                                                
''''''	                                                                                                                                                                                                                                                                
Step 2: Navigate to the Project Directory	                                                                                                                                                                                                                                        
cd TheEvent	                                                                                                                                                                                                                                                                        
''''''	                                                                                                                                                                                                                                                    
Step 3: Create a Virtual Environment	                                                                                                                                            
Create a virtual environment to isolate proj    ect dependencies    :	                                                                                                                                                                        
python -m venv venv	                                                                        
Activate the virtual environment:	                                                                                                                                                                        
On Windows:	                                                                                                                                                                                                        
venv\Scripts\activate	                                                                                                                                                                                    
On macOS and Linux:	                                                                                                                                                                
source venv/bin/activate	                                                                                                                                                                            
''''''	                                                                                                                                                            
Step 4: Install Dependencies	                                                                                                                                
pip install -r requirements.txt	                                                                                                                                                        
''''''	                                                                                                                                                                                    
Step 5: Configure Environment Variables	                                                                                                                                                                    
DEBUG=True	                                                                                                                                            
SECRET_KEY=your_secret_key_here	                                                                                                                                                                            
DATABASE_URL=sqlite:///db.sqlite3  # Or configure for your database	                                                                                                                                                
''''''	                                                                                                                                                                                                                
Step 6: Start the Development Server	                                                                                                                            
python manage.py runserver	
