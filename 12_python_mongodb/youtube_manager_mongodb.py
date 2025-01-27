from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://shouryadubey:shouryadubey@cluster0.stocpho.mongodb.net/")

db = client["ytmanager"]
video_collection = db["videos"]

print(client)


def list_video():
    for video in video_collection.find({}):
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)}, 
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List All Videos")
        print("2. Add New Videos")
        print("3. Update Videos")
        print("4. Delete a Videos")
        print("5. Exit the app")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter Video name: ")
            video = input("Enter Video time: ")
            add_video(name, video)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter updated Video name: ")
            video = input("Enter updated Video time: ")
            update_video(video_id, name, video)
        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")



if __name__ == "__main__":
    main()