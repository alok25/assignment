$(document).ready(function() {   
    var apiKey = '45624122';
    var token = 'T1==cGFydG5lcl9pZD00NTYyNDEyMiZzaWc9MWYzNGNkY2RiMjZkMzViYWFlMjRkNTAzZmU3YzdjOGZkNjZhY2E0MjpzZXNzaW9uX2lkPTJfTVg0ME5UWXlOREV5TW41LU1UUTJPVEF3TWpReU16Z3dPWDVWUm5sbmNGSjFUMEpLWTB0NFdGRmlPRlpST0haTUx5OS1mZyZjcmVhdGVfdGltZT0xNDY5MDgwNDQ2Jm5vbmNlPTAuNjY3NzgxNzU1NzkzODM5NyZyb2xlPXB1Ymxpc2hlciZleHBpcmVfdGltZT0xNDcxNjcyNDQ2';
    var api_secret = 'fa2712a516b88a2cd1f0a4a6579288a90a0a89d3';
    var sessionId = '2_MX40NTYyNDEyMn5-MTQ2OTAwMjQyMzgwOX5VRnlncFJ1T0JKY0t4WFFiOFZROHZMLy9-fg';
    var session;
    var connect_session;
    var connectionCount = 0;
 
    function connect() {
        session = TB.initSession(sessionId);
        // Initialize a Publisher, and place it into the element with id="publisher"
        publisher = TB.initPublisher(apiKey, 'publisher', {
            style: {buttonDisplayMode: 'on'},
            showControls: true,
            name: "AUDETEMI"
        });
        // Attach event handlers
        session.on({
          // This function runs when session.connect() asynchronously completes
          sessionConnected: function(event) {
            // Publish the publisher we initialzed earlier (this will trigger 'streamCreated' on other
            // clients)
            console.log("Connected")
            session.publish(publisher);
          },
          // This function runs when another client publishes a stream (eg. session.publish())
          streamCreated: function(event) {
            // Create a container for a new Subscriber, assign it an id using the streamId, put it inside
            // the element with id="subscribers"
            var subContainer = document.createElement('div');
            subContainer.id = 'stream-' + event.stream.streamId;
            document.getElementById('subscribers').appendChild(subContainer);
            // Subscribe to the stream that caused this event, put it inside the container we just made
            session.subscribe(event.stream, subContainer);
          }
        });
        publisher.on('streamCreated', function (event) {
            console.log('The publisher started streaming.');
        });
        session.on('connectionCreated', function (event) {
            console.log('The connection started.');
        });
        session.connect(apiKey, token);
    }
    // Connect to the Session using the 'apiKey' of the application and a 'token' for permission
    $("#StopVideoChat").click(function() {
       console.log("Clicked Stop");
        publisher.destroy();
        session.disconnect();
        $("#StopVideoChat").hide();
        $("#StartVideoChat").show();
        $("#videoChatPanel").hide();
    });
    $("#StartVideoChat").click(function() {
        console.log("Clicked Start");
        /*session.connect(apiKey, token);*/
        connect();
        $("#StopVideoChat").show();
        $("#StartVideoChat").hide();
        $("#videoChatPanel").show();
    });
/*    session.connect(apiKey, token);*/
})
