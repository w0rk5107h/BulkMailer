# BulkMailer
A bulk mailer to send bulk emails


## INTRO
This is just a simple bulk mailer built using flask and flask-mail. It can send messages to multiple people and message templates can also be used.

## USAGE
   1. You need to put in your gmail creds in the `email-creds.json` file.
   
   2. Then you need to make the message template by editing `message.json`.  
      `a.` First, edit the subject.  
      `b.` Second, edit the sender.  
      `c.` Third, edit the message content. For this you need to make a template message, and make variables for the dynamic part.  
         FOR EXAMPLE : If this is my message  
         ```
         Hello ##NAME##
         This is your covid report - ##result##
         ```
         Here `NAME` and `result` are the variables making them the dynamic part of the message.
         Make sure to and `##` at the start and end of the variable in the message.  
      `d.` Fourth, make the user list by editting the `users.json`.  
         Here, you need to supply the email of the recivers and the values of the variables that we made in the message template.  
         FOR EXAMPLE : Considering the above example, my `users.json` should look like this.  
         ```
         {
             "1":{
                 "email":"user1@gmail.com",
                 "NAME":"USER1",
                 "result":"positive"
                 },
             "2":{
                 "email":"user2@gmail.com",
                 "NAME":"USER2",
                 "result":"negative"
                 }
         }                 
         ```
         **IMPORTANT - THE ID IN THE JSON SHOULD BE SAME AS THE VARIABLE NAME (CASE SENSITIVE)**  
         
   3. `pip install -r requirements.txt`  
   
   4. `python main.py`  
   
   5. Just go to http://localhost:1911 **OR** Make a curl request : `curl http://localhost:1911`


## FULL EXAMPLE

**`message.json`** should be :
```
{
    "subject":"Covid-19 Report",
    "sender":"XYZ Hospital",
    "content":"Hello ##name##,\nHere is you covid report - ##result##."
}
```
*In this all three prams are mandatory.*
  

**`users.json`** should be :
```
{
    "1":{
        "email":"user1@gmail.com",
        "name":"User 1",
        "result":"positive"
        },
    "2":{
        "email":"user2@gmail.com",
        "name":"User 2",
        "result":"negative"
        }
}
```
*In this only `email` param is mandatory, unless you have created some variables in the message.*
*Also, you can add as many users as you want.*

### Attachment support comming soon
