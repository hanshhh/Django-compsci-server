
// Only for testing:
async function fetchRoomsJSON() {
    let rooms;
    try {
        const response = await fetch('127.0.0.1:8000/api/rooms/');
        if(response.ok) {
            rooms = await response.json();
        } else {
            throw new Error(JSON.stringify({ code: response.status, message: response.statusText }))
        }
        return rooms;
    } catch(error) {
        alert(error)
    }
}
  
async function fetchRoomJSON(id) {
    let room;
    try {
        const response = await fetch('127.0.0.1:8000/api/rooms/');
        if(response.ok) {
            room = await response.json();
        } else {
            throw new Error(JSON.stringify({ code: response.status, message: response.statusText }))
        }
        return room;
    } catch(error) {
        alert(error)
    }
}

async function fetchTopicsJson();
async function fetchTopicJson(id);
async function fetchParticipantsJson(room_id);
async function fetchRoomHostJson(room_id);
async function fetchRoomParticipantsByID(room_id, user_id);